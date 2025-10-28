```markdown
# Criptografador Web com Cifra de César 🔐

Projeto acadêmico (APS) desenvolvido para o 2º semestre do curso de Ciências da Computação da Universidade Paulista (UNIP).

## 🚀 Descrição

Esta é uma aplicação web simples, construída com o framework **Flask** (Python), que implementa a **Cifra de César**.
O projeto permite que um usuário faça login (apenas com um email, para fins de sessão) e, em seguida, possa
criptografar ou descriptografar mensagens de texto fornecendo o texto e uma chave (deslocamento).

## ✨ Funcionalidades

O projeto é composto por duas páginas principais e a lógica de backend:

* **Página de Login** (`/login`):
    * Solicita um email ao usuário para iniciar a sessão.
    * Não há validação de senha, o email é usado apenas para identificar a sessão do usuário.
    * Após o envio, o usuário é redirecionado para a página principal.

* **Página Principal** (`/`):
    * Verifica se o usuário está logado. Caso não esteja, redireciona para a página de login.
    * Exibe um formulário para o usuário inserir o texto, a chave (número de deslocamento) e o modo (Criptografar ou Descriptografar).
    * Processa o texto usando a Cifra de César e exibe o resultado na mesma página.
    * Exibe o email do usuário logado e um botão "Sair" para encerrar a sessão.

* **Lógica da Cifra** (`app.py`):
    * A função `cifra_de_cesar` processa o texto, convertendo-o para minúsculas e aplicando o deslocamento
da chave apenas em caracteres do alfabeto (a-z), preservando espaços, números e outros caracteres.

## 💻 Tecnologias Utilizadas

* **Backend:**
    * ![Python]
    * ![Flask]
* **Frontend:**
    * ![HTML5]
    * ![CSS3]

## ⚙️ Como Executar

Para rodar este projeto localmente, siga os passos:

1.  **Pré-requisitos:**
    * Python 3.x
    * Flask

2.  **Instale o Flask:**
    Se você ainda não tem o Flask instalado, abra seu terminal e execute:
    ```bash
    pip install Flask
    ```

3.  **Execute a Aplicação:**
    Navegue até a pasta raiz do projeto (onde o arquivo `app.py` está localizado) e execute o seguinte comando:
    ```bash
    python app.py
    ```

4.  **Acesse no Navegador:**
    O servidor Flask iniciará em modo de debug. Abra seu navegador e acesse:
    `http://127.0.0.1:5000/`

    Você será direcionado para a página de login. Após inserir um email, você poderá usar o criptografador.
````
