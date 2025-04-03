from flask import Flask, request, jsonify
import sqlite3 
from flask_cors import CORS

app = Flask(__name__)


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
    dados = request.get_json()
    
    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("imagem_url")
    
    if not titulo or not categoria or not autor or not image_url:
        return jsonify ({"erro": "Todos os campos devem ser obrigatorios"}), 400
    
    with sqlite3.connect("database.db") as conn:

        conn.execute("""f
                    INSERT INTO LIVROS (titulo, categoria, autor, image_url ) values ({titulo}, {categoria}, {autor}, {image_url})
        """
    )
    conn.commit()
    
    return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201
    

@app.route("/livros", methods=["GET"])
def buscarLivro():
    
    with sqlite3.connect("database.db") as conn:

        livros = conn.execute("""f
                     SELECT * FROM LIVROS ORDER BY NAME 
        """       
    ).fetchall
        
    
    livros_retornados = []
        
    for livro in livros:
        livros_retornados.append({
             
                                "id" : livro[0],
                                "titulo": livro[1],
                                "cetegoria" : livro[2],
                                "autor" : livro[3],
                                "image_url" : livro[4],
        })    
       
    return jsonify(livros_retornados)



if __name__ == "__main__":
    app.run(debug=True)