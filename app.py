from flask import Flask
import sqlite3 

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

@app.route("/doar", method=["POST"])
def doar_livro():
    
    


@app.route("/livros" method=["POST"])
def livro




if __name__ == "__main__":
    app.run(debug=True)