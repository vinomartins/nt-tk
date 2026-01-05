from math import sqrt, floor

def primo(p: int):
    fsp = floor(sqrt(p))
    n = 2
    steps = []

    steps.append(f"""Raiz de {p} =~ {sqrt(p)}
----- \n
[b]Testando se {p} possui divisores[/b]\n""")
    composto = False    
    while n <= fsp:
        steps.append(f"Testando se {n} divide {p}")

        if p % n == 0:
            steps.append(f"-> {n} divide {p}")
            result = f"{p} não é primo" 
            composto = True
            break
        n += 1
    if not composto:
        steps.append(f"-> limite {sqrt(p)} atingido")
        result = f"{p} é primo"
    return {
        "title": "Teste de primalidade",
        "input": f"p = {p}",
        "steps": steps,
        "result": result,  
        "theory": (
            "Testamos se n | p para n de 2 até" + 
            " a raiz de p"
        ),
    }

if __name__ == "__main__":
    print(primo(8013))
