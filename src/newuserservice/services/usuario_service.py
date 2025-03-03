from extensions import db
from flask import jsonify

def listar_usuarios():
    from models.usuario import usuario
    usuarios = usuario.query.all()
    usuarios_json = [usuario.json() for usuario in usuarios]
    return jsonify(usuarios_json)



def criar_usuario(dados):
    from models.usuario import usuario
    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")
    usuario = usuario(nome=nome, email=email, senha=senha)
    db.session.add(usuario)
    db.session.commit()
    return jsonify({"mensagem:":"usuario adicionado com sucesso"}), 201