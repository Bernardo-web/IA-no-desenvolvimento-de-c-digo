# 🤖 Inteligência Artificial no Desenvolvimento de Código

## 👨‍🏫 Descrição do Projeto
Este projeto tem como objetivo **demonstrar o uso da Inteligência Artificial no desenvolvimento de código**, tema estudado em nossa disciplina.  
A ideia é mostrar como modelos de linguagem modernos conseguem **gerar trechos de código automaticamente** a partir de uma instrução em linguagem natural.

Foram analisados artigos que marcam a evolução dessa área:
- **2017 – Attention Is All You Need (Vaswani et al.)** → introduziu a arquitetura Transformer, base para modelos que entendem e geram código.  
- **2025 – Enhancing Accuracy of AI-Generated Code Across Languages (MIT)** → trouxe métodos de filtragem que aumentam a precisão e confiabilidade do código gerado.

Nosso código é uma aplicação prática que exemplifica essa evolução.

---

## ⚙️ Descrição do Ambiente
- **Sistema Operacional:** Windows 11 (também compatível com Linux/MacOS)  
- **Editor de Código:** Visual Studio Code  
- **Linguagem:** Python 3.12  
- **Bibliotecas Utilizadas:**  
  - `transformers` → para utilizar modelos de IA pré-treinados  
  - `torch` → backend necessário para rodar os modelos  

---

## 🐍 Descrição da Linguagem
Optamos por **Python** por ser a principal linguagem em projetos de Inteligência Artificial.  
Python possui:
- Grande quantidade de bibliotecas (Transformers, TensorFlow, PyTorch).  
- Comunidade ativa e vasta documentação.  
- Simplicidade de sintaxe, o que facilita a prototipação rápida.  

---

## 💻 Código do Projeto

```python
from transformers import pipeline

# Criando um gerador de código
generator = pipeline("text-generation", model="Salesforce/codegen-350M-multi")

# Prompt para o modelo
prompt = "Escreva uma função em Python que calcule a soma de uma lista de números"

# Geração
result = generator(prompt, max_length=100, num_return_sequences=1)

print("🚀 Código gerado pela IA:\n")
print(result[0]["generated_text"])
