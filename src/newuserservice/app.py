from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from extensions import db  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:francisco02699@localhost:5432/postgres'

db.init_app(app)
migrate = Migrate(app, db)


with app.app_context():
    from models import usuario

@app.route('/', methods=['POST'])  
def index():
    dados = request.get_json()
    novo_usuario = usuario(
        nome=dados['nome'],
        email=dados['email'], 
        senha=dados.get('senha')  
    )
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário adicionado com sucesso!'}), 201



if __name__ == "__main__":
    app.run(debug=True)

