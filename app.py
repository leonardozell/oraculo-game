from flask import (
    Flask,
    render_template,
    request,
    session,
    redirect
)
import json

app = Flask(__name__)
app.secret_key = "oraculo_secreto_123"

def carregar_personagens():
    with open(
        "data/personagens.json",
        encoding="utf-8"
    ) as arquivo:
        return json.load(arquivo)
    
def carregar_perguntas():
    with open(
        "data/perguntas.json",
        encoding="utf-8"
    ) as arquivo:

        return json.load(arquivo)

def filtrar_personagens(
    personagens,
    atributo,
    resposta
):

    valor = resposta == "sim"

    filtrados = []

    for personagem in personagens:

        if personagem.get(atributo) == valor:
            filtrados.append(personagem)

    return filtrados

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/game", methods=["GET", "POST"])
def game():

    perguntas = carregar_perguntas()

    if "indice" not in session:
        session["indice"] = 0

    if "personagens" not in session:
        session["personagens"] = carregar_personagens()

    if "nao_encontrado" not in session:
        session["nao_encontrado"] = False

    if request.method == "POST":

        indice = session["indice"]

        # acabou perguntas antes de processar
        if indice >= len(perguntas):
            return redirect("/guess")

        resposta = request.form.get("resposta")

        atributo = perguntas[indice]["atributo"]

        filtrados = filtrar_personagens(
            session["personagens"],
            atributo,
            resposta
        )

        session["personagens"] = filtrados
        session["indice"] += 1

        print("Restaram:")
        print(session["personagens"])

        # nenhum personagem
        if len(filtrados) == 0:
            session["nao_encontrado"] = True
            return redirect("/guess")

        session["nao_encontrado"] = False

        # achou exatamente um
        if len(filtrados) == 1:
            return redirect("/guess")

        # terminou perguntas
        if session["indice"] >= len(perguntas):
            return redirect("/guess")

    # proteção extra
    if session["indice"] >= len(perguntas):
        return redirect("/guess")

    pergunta_atual = perguntas[session["indice"]]

    return render_template(
        "game.html",
        pergunta=pergunta_atual
    )

@app.route("/guess")
def guess():

    personagens = session.get("personagens", [])

    # nenhum personagem encontrado
    if len(personagens) == 0:

        return render_template(
            "guess.html",
            personagem=None
        )

    personagem = personagens[0]

    return render_template(
        "guess.html",
        personagem=personagem
    )

@app.route("/result", methods=["POST"])
def result():

    acertou = request.form.get("acertou")

    # jogador confirmou
    if acertou == "sim":

        session.clear()

        return render_template(
            "result.html",
            mensagem="O Oráculo acertou!"
        )

    # jogador negou
    session.clear()

    return render_template(
        "result.html",
        mensagem=(
            "O Oráculo ainda está aprendendo..."
        )
    )

@app.route("/learn")
def learn():

    return render_template("learn.html")

@app.route("/restart")
def restart():

    session.clear()

    return redirect("/game")

if __name__ == "__main__":
    app.run(debug=True)