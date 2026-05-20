# 🔮 O Oráculo

Um jogo de adivinhação inspirado em experiências como Akinator, onde o Oráculo tenta descobrir em quem o jogador está pensando através de perguntas de "Sim" ou "Não".

O projeto foi desenvolvido em Python utilizando Flask, com interface web simples em HTML + CSS e sistema de perguntas baseado em JSON.

---

# ✨ Demonstração

O jogador pensa em uma pessoa ou personagem e responde às perguntas do Oráculo.

Exemplo:

- É uma pessoa real?
- Está ligado ao esporte?
- Está ligado à música?

Com base nas respostas, o Oráculo filtra as possibilidades até tentar adivinhar.

---

# 🚀 Tecnologias Utilizadas

- Python 3.13
- Flask
- HTML5
- CSS3
- JSON
- Gunicorn (deploy)

---

# 📁 Estrutura do Projeto

```text
oraculo-game/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── .gitignore
│
├── data/
│   ├── personagens.json
│   └── perguntas.json
│
├── static/
│   └── css/
│       └── style.css
│
└── templates/
    ├── index.html
    ├── game.html
    ├── guess.html
    └── result.html
```

---

# ⚙️ Como Rodar Localmente

Clone o projeto:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd oraculo-game
```

Crie e ative o ambiente Conda:

```bash
conda create -n oraculo python=3.13
conda activate oraculo
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python app.py
```

Abra no navegador:

```text
http://127.0.0.1:5000
```

---

# 🎮 Funcionalidades do MVP

✅ Interface temática do Oráculo  
✅ Sistema de perguntas Sim / Não  
✅ Filtragem de personagens por atributos  
✅ Sessão de jogo com memória temporária  
✅ Reiniciar partida  
✅ Tratamento de erros e casos sem resultado  
✅ Tentativa automática de adivinhação  
✅ Interface web simples e responsiva  

---

# 🧠 Como o Oráculo Funciona

O jogo utiliza dois arquivos JSON:

### personagens.json

Contém:

- nome
- atributos
- características

Exemplo:

```json
{
  "nome": "Neymar",
  "real": true,
  "esporte": true,
  "musica": false
}
```

### perguntas.json

Contém:

- pergunta
- atributo correspondente

Exemplo:

```json
{
  "pergunta": "É uma pessoa real?",
  "atributo": "real"
}
```

O Flask utiliza as respostas do jogador para filtrar os candidatos até chegar ao melhor palpite possível.

---

# 🔮 Futuras Atualizações

Este projeto continuará evoluindo após a conclusão do MVP.

Roadmap planejado:

## 1. Aprendizado com erros

Quando o Oráculo errar:

- jogador informa quem era
- novo personagem é salvo
- o banco cresce com o tempo

Objetivo:

Tornar o Oráculo progressivamente mais inteligente.

---

## 2. Perguntas orgânicas / aleatórias

Hoje as perguntas seguem uma ordem fixa.

Atualização futura:

- ordem dinâmica
- comportamento menos previsível
- sensação mais natural de "pensamento"

Possíveis abordagens:

- randomização simples
- priorização por relevância

---

## 3. Expansão do banco de personagens

Adicionar:

- personalidades históricas
- celebridades
- personagens fictícios
- figuras internacionais

---

## 4. Personalidade do Oráculo

Versão futura poderá incluir:

- humor
- frases próprias
- identidade narrativa
- respostas mais imersivas

---

# 📌 Status do Projeto

🟣 MVP em desenvolvimento e evolução contínua.

---

# 👨‍💻 Autor

Projeto desenvolvido por Leonardo Zell como estudo e experimento de desenvolvimento web, lógica de decisão e jogos de adivinhação em Python.