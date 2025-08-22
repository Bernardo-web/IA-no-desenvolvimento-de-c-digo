"""
Projeto: Inteligência Artificial no Desenvolvimento de Código
Descrição: Exemplo prático de como um modelo de linguagem pode gerar código automaticamente.
Integrantes:
- Arthur Santos Almeida
- Bernardo Santana Gomes Corrêa
- Fernando Figueiredo Gois
- João Guilherme Santos Lima
- Luiz Henrique Silva Neto
- Milton de Souza Santos Júnior
"""

from transformers import pipeline

def gerar_codigo(prompt):
    """
    Função que utiliza o modelo CodeGen para gerar código a partir de uma instrução em linguagem natural.
    """
    # Criando um gerador de código
    generator = pipeline("text-generation", model="Salesforce/codegen-350M-multi")

    # Geração do código com base no prompt
    result = generator(prompt, max_length=120, num_return_sequences=1)

    return result[0]["generated_text"]

if __name__ == "__main__":
    print("🤖 IA no Desenvolvimento de Código")
    print("--------------------------------\n")

    # Prompt em linguagem natural
    prompt = "Escreva uma função em Python que calcule a soma de uma lista de números"

    # Gerando código
    codigo_gerado = gerar_codigo(prompt)

    print("🚀 Prompt utilizado:")
    print(prompt)
    print("\n💻 Código gerado pela IA:\n")
    print(codigo_gerado)
