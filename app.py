
from flask import Flask, render_template, request, session, redirect, url_for
import os

# Inicializa o aplicativo Flask
app = Flask(__name__)


app.secret_key = os.urandom(24)



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


@app.route('/', methods=['GET', 'POST'])
def index():
    
    if 'email_usuario' not in session:
        return redirect(url_for('login'))

    
    resultado_final = ''
    texto_original = ''
    chave = 0

    if request.method == 'POST':
        texto_original = request.form['texto']
        chave = int(request.form['chave'])
        modo = request.form['modo'] # 'c' ou 'd'
        resultado_final = cifra_de_cesar(texto_original, chave, modo)

    
    return render_template('index.html', resultado=resultado_final, texto_inserido=texto_original, chave_inserida=chave)


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        
        email = request.form['email']
        
        
        session['email_usuario'] = email
        
        
        return redirect(url_for('index'))

    
    return render_template("login.html")


@app.route('/logout')
def logout():
    
    session.pop('email_usuario', None)

if __name__ == '__main__':

    app.run(debug=True)
    