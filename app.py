from flask import Flask, request, jsonify
from database import GerenciadorDeDados
from auth import configurar_autenticacao, jwt, gerar_hash_senha, verificar_senha
from flask_jwt_extended import create_access_token, jwt_required
import sqlite3

# Inicialização do aplicativo
app = Flask(__name__)
configurar_autenticacao(app)

gerenciador = GerenciadorDeDados()
gerenciador.inicializar_banco()

# Rota de registro de usuário
@app.route('/registro', methods=['POST'])
def registrar():
    dados = request.get_json() or {}
    nome_usuario = dados.get('nome_usuario')
    senha = dados.get('senha')
    
    if not nome_usuario or not senha:
        return jsonify({"mensagem": "Dados incompletos"}), 400
    
    try:
        gerenciador.criar_usuario(nome_usuario, gerar_hash_senha(senha))
        return jsonify({"mensagem": "Usuário criado"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"mensagem": "Nome de usuário já existe"}), 409

# Rota de login
@app.route('/login', methods=['POST'])
def logar():
    dados = request.get_json() or {}
    nome_usuario = dados.get('nome_usuario')
    senha = dados.get('senha')
    
    usuario = gerenciador.obter_usuario_por_nome(nome_usuario)
    if usuario and verificar_senha(senha, usuario[2]):
        return jsonify(token_acesso=create_access_token(identity=str(usuario[1]))), 200
    
    return jsonify({"mensagem": "Credenciais inválidas"}), 401

# Rota protegida para adicionar dado
@app.route('/dados', methods=['POST'])
@jwt_required()
def adicionar_dado():
    dados = request.get_json() or {}
    valor = dados.get('valor')
    
    if not valor or len(valor) > 255:
        return jsonify({"erro": "Dados inválidos"}), 400
    
    return jsonify({"id": gerenciador.criar_dado(valor)}), 201

# Rota protegida para obter dados
@app.route('/dados', methods=['GET'])
@jwt_required()
def obter_dados():
    return jsonify([
        {"id": linha[0], "valor": linha[1], "data_criacao": linha[2]} 
        for linha in gerenciador.obter_todos_dados()
    ]), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
