from flask import Blueprint, request, jsonify
from services.usuario_service import criar_usuario , listar_usuarios, filtrar_usuarioid, filtrar_usuariogeral, request, retornar_id, excluir_usuario, atualizar_usuario

usuarios_bp = Blueprint("usuarios", __name__, url_prefix="/usuarios")

@usuarios_bp.route("/", methods=["GET"])
def user_get():
    return listar_usuarios()

@usuarios_bp.route("/id/<int:id>", methods=["GET"])
def user_get_id(id):
    return filtrar_usuarioid(id)

@usuarios_bp.route("/adicionar", methods=["POST"])
def user_set():
    dados = request.get_json()
    return criar_usuario(dados)

@usuarios_bp.route("/search", methods=["GET"])
def user_search():
    return filtrar_usuariogeral(request.args)

@usuarios_bp.route("/getid", methods=["GET"])
def user_getid():
    return retornar_id(request.args)

@usuarios_bp.route("/deletar/<int:id>", methods=["DELETE"])
def user_delete(id):
    return excluir_usuario(id)

@usuarios_bp.route("/atualizar/<int:id>", methods=["PATCH"])
def user_update(id):
    dados = request.get_json()
    if not id:
        return jsonify({"mensagem": "ID não fornecido"}), 400
    return atualizar_usuario(id, dados)