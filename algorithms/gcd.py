def gcd_with_steps(a: int, b: int):
    steps = []
    x, y = a, b

    while b != 0:
        q = a // b
        r = a % b
        steps.append(f"{a} = {b}·{q} + {r}\t\t" +
                     f"mdc({a},{b}) = mdc({b},{r})")
        a, b = b, r

    return {
        "title": "Algoritmo de Euclides para o MDC",
        "input": f"a = {x}, b = {y}",
        "steps": steps,
        "result": f"mdc({x}, {y}) = {a}",
        "theory": (
            "O algoritmo é baseado no fato" + 
            " de que se a = bq+r, então mdc(a,b) = mdc(b,r)"
        ),
    }

