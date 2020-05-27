import os
import json

DEF_DIR = "defs/"
GO_DIR = "out/go/"

defs = dict()

GO_TYPE_TABLE = dict(
    pair="string",
    price="float64",
    size="float64",
    guid="string",
    timestamp="string",
    duration="string",
    boolean="bool",
    int="int64",
    float="float64",
    string="string"
)

def up_first_letter(string: str):
    while True:
        index = string.find("_")
        if index == -1:
            break
        string = string[:index] + string[index+1].capitalize() + string[index+2:]
    return (string[0].upper() + string[1:]).replace("Id", "ID")

def generate_go(packageName: str):
    # make directory for output
    os.makedirs(GO_DIR, exist_ok=True)

    for deffile, defn in defs.items():
        exc = os.path.splitext(deffile)[0]
        with open(os.path.join(GO_DIR, "%s.go" % exc), "wt") as f:
            f.write("package %s\n\n" % packageName)
            
            for channel, params in defn.items():
                # struct for storing line
                typeName = "%s%s" % (up_first_letter(exc), up_first_letter(channel))
                f.write("// %s is auto-generated\n" % typeName)
                f.write("type %s struct {\n" % typeName)
                for name, typ in params.items():
                    if (typ.endswith("null")):
                        normType = typ[:-len("|null")]
                        # this type is nullable, in go, this parameter will be an pointer
                        f.write("\t%s *%s `json:\"%s\"`\n" % (up_first_letter(name), GO_TYPE_TABLE[normType], name))
                    else:
                        f.write("\t%s %s `json:\"%s\"`\n" % (up_first_letter(name), GO_TYPE_TABLE[typ], name))
                f.write("}\n\n")
                
                # definition json
                varName = "TypeDef%s%s" % (up_first_letter(exc), up_first_letter(channel))
                f.write("// %s is auto-generated\n" % varName)
                f.write("var %s = []byte(\"" % varName)
                defiJson = dict()
                for name, typ in params.items():
                    if (typ.endswith("null")):
                        typ = typ[:-len("|null")]
                    defiJson[name] = typ
                f.write(json.dumps(defiJson).replace("\"", "\\\""))
                f.write("\")\n\n")

def main():
    # load definition files
    deffiles = os.listdir(DEF_DIR)
    for filename in deffiles:
        with open(os.path.join(DEF_DIR, filename)) as f:
            loaded = json.load(f)
            defs[os.path.splitext(filename)[0]] = loaded
    # generates definitions for go
    generate_go("jsondef")

if __name__ == "__main__":
    main()
