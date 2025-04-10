


![Cena em pixel art de pessoas lendo em um parque ao entardecer](https://i.ibb.co/d4CwRPNW/Chat-GPT-Image-9-de-abr-de-2025-20-12-33.png)


# Doaçao livros

Este projeto é uma API REST desenvolvida com **Python** e **Flask**, com o objetivo de facilitar a doação e o compartilhamento de livros.  
Ela permite que usuários cadastrem livros para doação, armazenando as informações em um banco de dados **SQLite** leve e local.

A aplicação é ideal para iniciativas sociais, escolas, bibliotecas comunitárias ou projetos independentes que visam incentivar a leitura e promover o acesso gratuito a livros.

## Stack utilizada Front-end :


```bash
🛠️ Tecnologias Utilizadas :
```


| Tecnologia | Badge |
|------------|--------|
| Vite       | ![Vite](https://img.shields.io/badge/Vite-%2335495e?style=for-the-badge&logo=vite&logoColor=FFD62E) |
| React      | ![React](https://img.shields.io/badge/React-%2320232a?style=for-the-badge&logo=react&logoColor=61DAFB) |
| Axios      | ![Axios](https://img.shields.io/badge/Axios-%230072C6?style=for-the-badge&logo=axios&logoColor=white) |
| SASS       | ![SASS](https://img.shields.io/badge/SASS-%23CC6699?style=for-the-badge&logo=sass&logoColor=white) |



## Demonstração:



![Demonstração do Projeto](https://i.ibb.co/XxFv7FnY/V-deo-Demostracao.gif)



Segue projeto relacionado

[Link Acesso ao repositorio Front end ](https://github.com/Marlonsouto/doacao_livros_VNW)





# 🧱 Stack Utilizada 🔙 Backend :
```bash
Abaixo estão as principais tecnologias e ferramentas utilizadas na API:
```


| **Linguagem :**         | ![Python](https://img.shields.io/badge/Python-blue?logo=python&logoColor=white)  |
|------------------|-------------|
|**Framework :**          | ![Flask](https://img.shields.io/badge/Flask-%23000?logo=flask)                        | 
|**Gerenciamento de dependências :**|  `pip + requirements.txt`



## 🗄️ Banco de Dados

| **Sistema :**  | ![SQLite](https://img.shields.io/badge/SQLite-lightgrey?logo=sqlite)    |
|------------------|-------------|




-  **SQLite** (utilizado em todo o projeto)


### ⚙️ Outras Tecnologias

|**Postman**|[![Run in Postman](https://img.shields.io/badge/Run%20in-Postman-orange?logo=postman)](https://www.postman.com/your-username/workspace/api-doacao/collection/123456-abcdef)|
|------------------|-------------|

- **Postman :** Para testar e documentar os endpoints da API




# Instalação :


1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/meu_projeto.git
   cd meu_projeto

2. Crie um ambiente virtual:

    ```bash
    python -m venv venv
      # No Windows use   
    venv\Scripts\activate

3. Instale as dependencias:

    ```bash
    pip install -r requirements.txt

4. Execute o projeto
    ```bash
    python src/app.py

## 🗂️ Fluxo da API e Estrutura do Banco

Abaixo está um diagrama ilustrando o funcionamento das rotas da API e sua relação com o banco de dados SQLite:

![Demonstração das Rotas da API](https://i.ibb.co/bjPjpFrp/demonstra-ao-rotas-api.png)

## Demonstração API

#### 📡 Endpoints da API :

Abaixo estão as principais rotas disponíveis na API, incluindo exemplos de uso para facilitar testes via Postman, Insomnia ou outras ferramentas.

---

### 🏠 `GET /`

Retorna uma mensagem simples de boas-vindas (rota de teste).

**Exemplo de resposta:**
```html
<h1> Hello, VAI NA WEB!! <h1>
```
### 📘 `POST /doar `

**Exemplo de resposta:**

```json
{
  "titulo": "O Senhor dos Anéis",
  "categoria": "Fantasia",
  "autor": "J.R.R. Tolkien",
  "imagem_url": "https://exemplo.com/imagem.jpg"
}
````

### 🧾 `GET /livros`

**Exemplo de resposta:**

```json
[
  {
    "id": 1,
    "titulo": "O Pequeno Príncipe",
    "categoria": "Ficção",
    "autor": "Antoine de Saint-Exupéry",
    "imagem_url": "https://link-da-imagem.com/capa.jpg"
  },
  {
    "id": 2,
    "titulo": "Dom Casmurro",
    "categoria": "Romance",
    "autor": "Machado de Assis",
    "imagem_url": "https://link-da-imagem.com/domcasmurro.jpg"
  }
]

```



## Melhorias futuras 
- docker
- implementar filtro
- disponibilizar pdf

# Autor

- [@Marlonsouto](https://github.com/Marlonsouto)

## Desafio proposto por :

[![Postman](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQKnPTRTiEyydv3UWzyDyH5gRiM0iy48nRSw&s)](https://www.postman.com/)



## Crédito aos tutores 

- [@silvajpedro](https://github.com/silvajpedro)
- [@NandaCorreaa](https://github.com/NandaCorreaa)