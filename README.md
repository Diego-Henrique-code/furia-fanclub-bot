# FURIA Fan Club Bot

🔥 Um bot de Telegram feito para os fãs da FURIA!  
Traz jogos, curiosidades, frases motivacionais e quiz divertido.

---

## Funcionalidades

- 📆 Ver agenda de jogos (carregados de um arquivo JSON)
- 🧠 Receber curiosidades aleatórias sobre a FURIA
- 🔥 Mensagens motivacionais para a torcida
- 🎮 Quiz interativo sobre a história da FURIA
- 🗨️ Encerrar a conversa de forma amigável

---

## Estrutura de Pastas

furia-bot/  
├── data/ 
   ├── curiosidades.json  
   ├── jogos.json 
   └── motivacao.json
├── .env.example
├── .gitignore 
├── bot.py
├── README.md   
├── requirements.txt
└──utils.py

---

## Requisitos

- Python 3.13+
- Bibliotecas:
  - python-telegram-bot
  - requests
  - `python-dotenv`

---

## Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/furia-bot.git
   cd furia-bot

2. Instale as dependências:
pip install -r requirements.txt

3. Crie um arquivo .env com:
BOT_TOKEN=seu-token-do-telegram

4. Rode o bot:
python bot.py

## 📄.gitignore (recomendado)
.env
__pycache__/
*.py[cod]
data/*.json

## 📥 Como usar o requirements.txt
### Depois de clonar o projeto, basta rodar:
pip install -r requirements.txt
#### Isso irá instalar todas as bibliotecas necessárias exatamente nas versões corretas.

## Explicação Técnica
### Este projeto utiliza:

* Modularização: Separação de utilitários (utils.py) e dados (data/).

* Leitura de Arquivos Externos: Arquivos JSON com dados dinâmicos.

* Manipulação de Mensagens Inline: Uso de botões e menus no Telegram.

* Persistência Temporária: Pontuação do quiz armazenada em tempo de execução.

* Organização: Estrutura de pastas clara e separação por responsabilidade.

* Segurança: Token do bot carregado com dotenv.

## 🎥 Demonstração

O vídeo `furia-tech-challenge-diego.mp4` mostra o bot em ação no Telegram (desktop e mobile), incluindo:

- Execução do comando /start
- Interações com menu
- Mensagens Motivacionais e Curiosidades
- Quiz completo 
- Encerramento de conversa

## Autor
### Diego Henrique— Bot criado para desafio técnico da FURIA 🐾
