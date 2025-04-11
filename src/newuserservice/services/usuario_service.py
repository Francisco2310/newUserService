from extensions import db
from flask import jsonify
from flask import request
from sqlalchemy import desc

def listar_usuarios():
    from models.usuario import usuario
    usuarios = usuario.query.all()
    usuarios_json = [usuario.json() for usuario in usuarios]
    return jsonify(usuarios_json)

def filtrar_usuarioid(id):
    from models.usuario import usuario
    id = int(id)
    usuario = usuario.query.filter_by(id=id).first()
    return jsonify(usuario.json())

def retornar_id(dados):
    usuarios = achar_usuario(dados)
    return jsonify({"id": [usuario.id for usuario in usuarios]})


def filtrar_usuariogeral(dados):
    usuarios = achar_usuario(dados)
    usuarios_dict = [usuario.to_dict() for usuario in usuarios]
    return jsonify(usuarios_dict)

def criar_usuario(dados):
    from models.usuario import usuario
    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")
    usuario = usuario(nome=nome, email=email, senha=senha)
    db.session.add(usuario)
    db.session.commit()
    return jsonify({"mensagem:":"usuario adicionado com sucesso"}), 201

def achar_usuario(dados):
    from models.usuario import usuario
    usuarios = []
    for campo, valor in dados.items():
        if hasattr(usuario, campo):
            query = usuario.query.filter(getattr(usuario, campo) == valor).order_by(desc(usuario.criado_em)).all()
            usuarios.extend(query)
    return usuarios

def excluir_usuario(id):
    from models.usuario import usuario
    usuario = usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({"mensagem": "Usuario excluido com sucesso"}), 200
    else:
        return jsonify({"mensagem": "Usuario nao encontrado"}), 404
    
def atualizar_usuario(id, dados):
    from models.usuario import usuario
    usuario = usuario.query.get(id)
    if usuario:
        for campo, valor in dados.items():
            if hasattr(usuario, campo) and valor is not None:
                setattr(usuario, campo, valor)
        db.session.commit()
        return jsonify({"mensagem": "Usuario atualizado com sucesso"}), 200
    else:
        return jsonify({"mensagem": "Usuario nao encontrado"}), 404