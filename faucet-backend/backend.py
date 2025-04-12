from flask import Flask, request, jsonify
from flask_cors import CORS  # Enable CORS
from web3 import Web3
from eth_account import Account

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Replace with your R5 Network Testnet provider URL.
WEB3_PROVIDER_URI = "https://rpc-testnet.r5.network"
w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URI))

# Faucet private key for the faucet wallet on the TR5 Testnet.
FAUCET_PRIVATE_KEY = "FAUCET_PRIVATE_KEY_HERE"

# Recover the faucet address from the private key.
FAUCET_ACCOUNT = Account.from_key(FAUCET_PRIVATE_KEY)
FAUCET_ADDRESS = FAUCET_ACCOUNT.address

# Define the amount to send (example: 0.1 TR5)
AMOUNT_IN_TR5 = 0.1

@app.route("/drip", methods=["POST"])
def drip():
    data = request.get_json()
    to_address = data.get("address")

    # Validate that the provided address is a valid address on the R5 Network.
    if not w3.is_address(to_address):
        return jsonify({"error": "Invalid R5 address provided."}), 400

    try:
        # Prepare the transaction details using updated snake_case methods.
        nonce = w3.eth.get_transaction_count(FAUCET_ADDRESS)
        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': w3.to_wei(AMOUNT_IN_TR5, 'ether'),
            'gas': 21000,
            'gasPrice': w3.to_wei('50', 'gwei')
        }

        # Sign the transaction with the faucet's private key.
        signed_tx = w3.eth.account.sign_transaction(tx, FAUCET_PRIVATE_KEY)

        # Broadcast the transaction on the R5 Network using raw_transaction.
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

        return jsonify({
            "status": "success",
            "tx_hash": tx_hash.hex(),
            "to": to_address,
            "amount": AMOUNT_IN_TR5
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Running on all network interfaces on port 5000.
    app.run(host="0.0.0.0", port=5000, debug=True)
