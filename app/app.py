from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # V1: Formato técnico para monitoreo
    return jsonify({
        "status": "online",
        "message": "¡Servidor Flask en Docker funcionando, Nuevo commit de clase!",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "version": "1.0.0",
        "developer": "Roy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)