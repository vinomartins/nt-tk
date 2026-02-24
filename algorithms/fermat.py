from math import sqrt, floor, ceil


def fermat(p: int):
    fsp = floor(sqrt(p))
    n = 2
    steps = []


    if p % 2 == 0:
        return  {
            "title": "Algoritmo de Fermat para primalidade",
            "input": f"n = {p}",
            "steps": None,  
            "result": f"O input tem que ser ímpar",
            "theory": None 
        }

    steps.append(f"""Raiz de {p} =~ {sqrt(p)}
----- \n
[b]Testando se {p} é quadrado perfeito[/b]\n""")
    if fsp ** 2 == p:
        steps.append(f"{p} é quadrado perfeito, {p} = {fsp}^2")
        return  {
            "title": "Algoritmo de Fermat para primalidade",
            "input": f"n = {p}",
            "steps": None,  
            "result": f"{p} é composto",
            "theory": None 
        }
    a = ceil(sqrt(p))
    steps.append(f"Tomando a como  próximo inteiro após {fsp}: a = {a}") 
    b2 = a**2 - p
    steps.append(f"Testando se b = a^2 - p = {b2} é quadrado perfeito")

    while not is_square(b2):
        a = a + 1
        b2 = a**2 - p
        steps.append(f"Incrementando a --> {a}")
        steps.append(f"Testando se b = a^2 - p = {b2} é quadrado perfeito")

    if int(a- sqrt(b2)) == 1:
        result = f"a^2 - b^2 =1, logo p primo"
    else:
        result = f"p = {a- sqrt(b2)} * {a + sqrt(b2)}"
    
    return {
        "title": "Teste de primalidade",
        "input": f"p = {p}",
        "steps": steps,
        "result": result,  
        "theory": (
            "Verificamos se a^2 - p é quadrado perfeito " + 
            "para escrever p = a^2 - b^2 = (a-b)(a+b)"
        ),
    }

def is_square(n):
    return floor(sqrt(n)) ** 2 == n

if __name__ == "__main__":
    print(fermat(7*19))

