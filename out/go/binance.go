package jsondef

// BinanceDepth is auto-generated
type BinanceDepth struct {
	Symbol string `json:"symbol"`
	Price float64 `json:"price"`
	Size float64 `json:"size"`
}

// TypeDefBinanceDepth is auto-generated
var TypeDefBinanceDepth = []byte("{\"symbol\": \"symbol\", \"price\": \"price\", \"size\": \"size\"}")

// BinanceRestDepth is auto-generated
type BinanceRestDepth struct {
	Symbol string `json:"symbol"`
	OrderID int64 `json:"orderId"`
	Price float64 `json:"price"`
	Size float64 `json:"size"`
}

// TypeDefBinanceRestDepth is auto-generated
var TypeDefBinanceRestDepth = []byte("{\"symbol\": \"symbol\", \"orderId\": \"int\", \"price\": \"price\", \"size\": \"size\"}")

// BinanceTrade is auto-generated
type BinanceTrade struct {
	Symbol string `json:"symbol"`
	Price float64 `json:"price"`
	Timestamp string `json:"timestamp"`
	Size float64 `json:"size"`
	TradeID int64 `json:"tradeID"`
	BuyerOrderID int64 `json:"buyerOrderID"`
	SellterOrderID int64 `json:"sellterOrderID"`
	Eventtime string `json:"eventtime"`
}

// TypeDefBinanceTrade is auto-generated
var TypeDefBinanceTrade = []byte("{\"symbol\": \"symbol\", \"price\": \"price\", \"timestamp\": \"timestamp\", \"size\": \"size\", \"tradeID\": \"int\", \"buyerOrderID\": \"int\", \"sellterOrderID\": \"int\", \"eventtime\": \"timestamp\"}")

