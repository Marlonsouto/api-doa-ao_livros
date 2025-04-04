from flask import Flask, request, jsonify
import sqlite3 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route("/")
def primeira_mensagem():
    return "<h1> Hello, VAI NA WEB!! <h1>" 

def init_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS LIVROS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,  
                    titulo TEXT NOT NULL,  
                    categoria TEXT NOT NULL,  
                    autor TEXT NOT NULL,  
                    imagem_url TEXT NOT NULL  
                )
            """
        )  

init_db() 

@app.route("/doar", methods=["POST"])
def doar_livro():
    
    if (not request.is_json):
        return jsonify ({"erro": "a solicitaçao deve ser em JSON"},400)
    dados = request.get_json()
    
    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    imagem_url = dados.get("imagem_url")
    
    if not titulo or not categoria or not autor or not imagem_url:
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400
    
    with sqlite3.connect("database.db") as conn:
        conn.execute(
            """
                INSERT INTO LIVROS (titulo, categoria, autor, imagem_url) 
                VALUES (?, ?, ?, ?)
            """,
            (titulo, categoria, autor, imagem_url)
        )
        conn.commit()
    
    return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 200
    

@app.route("/livros", methods=["GET"])
def buscarLivro():
    with sqlite3.connect("database.db") as conn:
        livros = conn.execute(
            """
                SELECT * FROM LIVROS ORDER BY titulo
            """
        ).fetchall()  
    
    livros_retornados = []
        
    for livro in livros:
        livros_retornados.append({
            "id": livro[0],
            "titulo": livro[1],
            "categoria": livro[2], 
            "autor": livro[3],
            "imagem_url": livro[4]  
        })    
       
    return jsonify(livros_retornados)

if __name__ == "__main__":
    app.run(debug=True)