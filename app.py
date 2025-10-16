# app.py

from flask import Flask, render_template, request

# Inicializa o aplicativo Flask
app = Flask(__name__)


# Função para criptografar ou descriptografar usando a cifra de César
def cifra_de_cesar(texto, chave, modo):
    
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    resultado = ''

    for char in texto.lower():
        if char in alfabeto:
            posicao = alfabeto.find(char)
            if modo == 'c':
                nova_posicao = (posicao + chave) % 26
            else: # modo == 'd'
                nova_posicao = (posicao - chave) % 26
            resultado += alfabeto[nova_posicao]
        else:
            resultado += char
    return resultado

# Define a rota principal da aplicação
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado_final = ''
    texto_original = ''
    chave = 0

    # Se o formulário for enviado (método POST)
    if request.method == 'POST':
        texto_original = request.form['texto']
        chave = int(request.form['chave'])
        modo = request.form['modo'] # 'c' ou 'd'
        
        resultado_final = cifra_de_cesar(texto_original, chave, modo)

    # Renderiza a página HTML passando o resultado
    return render_template('index.html', resultado=resultado_final, texto_inserido=texto_original, chave_inserida=chave)

# Executa o aplicativo
if __name__ == '__main__':
    app.run(debug=True)