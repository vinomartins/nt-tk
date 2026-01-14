def render(result: dict) -> str:
    lines = []

    lines.append(f"[b]{result['title']}[/b]")
    lines.append("")

    lines.append("[b]Entrada[/b]")
    lines.append(result["input"])
    lines.append("")

    lines.append("[b]Passos[/b]")
    if result["steps"]:
        lines.extend(result["steps"])
    else:
        lines.append("(sem passos intermediários)")
    lines.append("")

    lines.append("[b]Resultado[/b]")
    lines.append(result["result"])
    lines.append("")
    
    if result["theory"]:
        lines.append("[b]Teoria[/b]")
        lines.append(result["theory"])

    return "\n".join(lines)

