#!/usr/bin/env python
import sys
from textual_serve.server import Server


def main():
    server = Server(
        command="python3 -m app",
        host="127.0.0.1",
        port=8000,
        public_url="https://vino.xyz.br/nt-tk" # Para rodar no servidor
    )
    
    # Run the server
    server.serve()

if __name__ == "__main__":
    main()
