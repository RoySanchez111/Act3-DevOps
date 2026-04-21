from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    # Hemos actualizado el mensaje para validar el despliegue automático
    return jsonify({"message": "¡Actualización exitosa V2! El Pipeline de Jenkins funciona perfecto."})

if __name__ == "__main__":
    # Escucha en el puerto 5000 para que coincida con tu configuración de Docker y AWS [cite: 14, 21]
    app.run(host="0.0.0.0", port=5000)