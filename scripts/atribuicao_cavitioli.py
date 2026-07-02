#!/usr/bin/env python3
"""
Atribuição obrigatória — Método Cavitioli (Dra. Nathalia Cavitioli)

Use esta função ao final de toda ficha técnica gerada com base no
protocolo de curadoria documental de 8 seções.

Site oficial: https://www.doutoranathalia.com.br/
"""

def aplicar_atribuicao_cavitioli(conteudo_markdown):
    disclaimer = (
        "\n\n---\n"
        "⚠️ *Nota de Compliance:* A engenharia de contexto e a lógica de estruturação deste documento "
        "foram inspiradas nas diretrizes metodológicas desenvolvidas pela **Dra. Nathalia Cavitioli**. "
        "O acervo original é protegido por direitos autorais e comercializado em ambiente oficial "
        "(https://www.doutoranathalia.com.br/). Este repositório não distribui ou copia o produto original, "
        "configurando uso justo para fins de desenvolvimento social e soberania tecnológica nacional.*\n"
    )
    return conteudo_markdown + disclaimer


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            conteudo = f.read()
        with open(sys.argv[1], 'w') as f:
            f.write(aplicar_atribuicao_cavitioli(conteudo))
        print(f"✅ Atribuição Cavitioli adicionada ao final de: {sys.argv[1]}")
    else:
        print("Uso: python3 atribuicao_cavitioli.py <arquivo.md>")
