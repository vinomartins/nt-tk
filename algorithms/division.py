def division(a: int, b: int):
    steps = []
    x, y = a, b

    if (a < 0) or (b< 0):
        return  {
            "title": "Algoritmo de Euclides para o MDC",
            "input": f"a = {x}, b = {y}",
            "steps": None,  
            "result": f"Implementado apenas para a,b >0",
            "theory": None 
        }
    if b > a:
        return {
            "title": "Algoritmo de Euclides para o MDC",
            "input": f"a = {x}, b = {y}",
            "steps": [f"{a} < {b}, logo q = 0 e r = a"],
            "result": f"{a} = {0}*{b} + {a}",
            "theory": None 
        }

    q = 1
    r = a 

    steps.append("Iniciamos com q = 1")
    while a - q*b > b:
        steps.append(f"q*b = {q}*{b} = {q*b} <  {a} \nIncrementando q -> {q+1}\n---")
        q = q+1
        r = a - q*b
    steps.append(f"q*b = {q}*{b} = {q*b} <  {a}\n---")
    steps.append(f"{q+1}*{b} = {(q+1)*b} >=  {a} \nQuociente = {q}\nCalculando r  = a-q*b = {a}-{q}*{b} = {a-q*b}")


    return {
        "title": "Algoritmo de Euclides para o MDC",
        "input": f"a = {x}, b = {y}",
        "steps": steps,
        "result": f"{a} = {q}*{b} + {r}",
        "theory": None 
    }
if __name__ == "__main__":
        print(division(13,30))
