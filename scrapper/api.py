from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load the unified JSON data
with open("camisas_unificadas.json", "r", encoding="utf-8") as archivo_unificado:
    camisas_unificadas = json.load(archivo_unificado)

@app.route('/api/camisas', methods=['GET'])
def get_camisas():
    return jsonify(camisas_unificadas)

if __name__ == '__main__':
    app.run(debug=True)