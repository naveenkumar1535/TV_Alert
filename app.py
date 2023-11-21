from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print('Inside Code')
    try:
        data = request.json#.get_json()
        symbol = data.get('symbol')
        action = data.get('action')
        price = data.get('price')
        timestamp = data.get('timestamp')
        message = data.get('message')
        print(f"Received TradingView alert: Symbol={symbol}, Action={action}, Price={price}, Timestamp={timestamp}, Message={message}")
        print("Received TradingView alert:")
        print(data)
    # Add your custom logic to handle the TradingView alert data here
        return jsonify({'message': 'Webhook received successfully'})
    except Exception as e:
        print(f"Error processing TradingView alert: {e}")
        return jsonify({'error': 'Error processing alert'}), 500

def main():
    webhook()
    
if __name__ == '__main__':
    app.run(debug=True)
