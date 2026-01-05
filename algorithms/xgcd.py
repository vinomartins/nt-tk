def xgcd(a: int, b: int):
    steps = []
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1

    while r1 != 0:
        q = r0 // r1
        steps.append(
            f"q={q}, r={r0}-{q}·{r1}={r0-q*r1}"
        )
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1

    return {
        "title": "Extended Euclidean Algorithm",
        "input": f"a = {a}, b = {b}",
        "steps": steps,
        "result": (
            f"gcd = {r0}\n"
            f"Coefficients: x = {s0}, y = {t0}\n"
            f"{a}·({s0}) + {b}·({t0}) = {r0}"
        ),
        "theory": (
            "The extended Euclidean algorithm finds integers x, y\n"
            "such that ax + by = gcd(a, b)."
        ),
    }

