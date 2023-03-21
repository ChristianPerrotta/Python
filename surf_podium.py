# code and UI uses Portuguese instead of English
# prints the final placing of participants in a surf contest

def colocacao(part: dict) -> str:
    """Função que determina as colocações dos participantes.

    Args:
        part (dict): Dicionário com as pontuações (chave)
            de cada participante (valor).

    Returns:
        str: String com as colocações de cada participante e sua pontuação.

    """

    pontos = list(part.keys())
    pontos.sort(reverse=True)
    resultado = f"O primeiro colocado é {part[pontos[0]]}, com {pontos[0]} pontos.\n"
    resultado += f"O segundo colocado é {part[pontos[1]]}, com {pontos[1]} pontos.\n"
    resultado += f"O terceiro colocado é {part[pontos[2]]}, com {pontos[2]} pontos.\n"
    return resultado

participantes = {1454: "Lucas", 1243: "Pedro", 1452: "Ricardo"}
resultado = colocacao(participantes)
print(resultado)