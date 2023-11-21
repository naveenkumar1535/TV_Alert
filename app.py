from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received TradingView alert:")
    print(data)
    # Add your custom logic to handle the TradingView alert data here
    return jsonify({'message': 'Webhook received successfully'})

def main():
    webhook()
    
if __name__ == '__main__':
    app.run(debug=True)
