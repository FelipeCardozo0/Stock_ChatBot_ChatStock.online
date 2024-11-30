from flask import Flask, request, jsonify
import yfinance as yf
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS


@app.route("/stock", methods=["POST"])
def get_stock_data():
    data = request.json
    ticker = data.get("ticker")

    if not ticker:
        return jsonify({"error": "Ticker symbol is required"}), 400

    try:
        stock = yf.Ticker(ticker)
        stock_info = stock.info

        # Use currentPrice as a fallback for regularMarketPrice
        current_price = stock_info.get(
            "regularMarketPrice") or stock_info.get("currentPrice")

        return jsonify({
            "ticker": ticker.upper(),
            "current_price": current_price,
            "currency": stock_info.get("currency"),
            "name": stock_info.get("shortName"),
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def home():
    return "API is running!"


@app.before_request
def log_request():
    print(f"Received request at {request.path}")


if __name__ == "__main__":
    app.run(debug=True)
