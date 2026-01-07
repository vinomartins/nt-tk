# nt-tk: Ferramentas para teoria dos números

Instale o textual com 

``pip install textual``

e execute com ` python3 app.py `.

Para transformar em interface web, instale o textual-dev com 
``pip install textual``

e crie um arquivo, por exemplo `webapp.py`, com

```
from textual_serve.server import Server

def main():
    server = Server(
        command="python3 -m app",
        host="127.0.0.1",
        port=8000,
    )
    
    # Run the server
    server.serve()

if __name__ == "__main__":
    main()

