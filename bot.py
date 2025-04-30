
import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from utils import carregar_arquivo, formatar_jogos, escolher_aleatorio, formatar_teclado_opcoes

load_dotenv()

# Carregamento de dados externos
curiosidades = carregar_arquivo("data/curiosidades.json")
frases_motivacionais = carregar_arquivo("data/motivacao.json")
jogos = carregar_arquivo("data/jogos.json")


# Quiz
quiz = [
    {"pergunta": "Em que ano a FURIA foi fundada?", "opcoes": ["2015", "2017", "2019"], "correta": 1},
    {"pergunta": "Qual jogador ficou conhecido como ‘The Professor’ ?", "opcoes": ["arT", "FalleN", "KSCERATO"], "correta": 1},
    {"pergunta": "Qual dessas é uma marca registrada do estilo da FURIA no CS?", "opcoes": ["Jogo defensivo", "Estratégias lentas", "Agressividade"], "correta": 2},
    {"pergunta": "Qual dessas organizações já foi rival marcante da FURIA?", "opcoes": ["INTZ", "MIBR", "Sharks"], "correta": 1},
    {"pergunta": "Qual é o lema que a FURIA costuma divulgar para a torcida?", "opcoes": ["Gritar, correr e vencer!", "Do Brasil pro topo!", "Carregar com garra, vencer com honra!"], "correta": 2}
]

user_quiz_data = {}

# Comandos
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Fala, torcedor da FURIA! Bem-vindo ao Fan Club Bot!\nUse /menu para ver as opções.")

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = [
        [InlineKeyboardButton("📆 Jogos", callback_data="jogos")],
        [InlineKeyboardButton("🧠 Curiosidades", callback_data="curiosidades")],
        [InlineKeyboardButton("🔥 Motivação", callback_data="motivacao")],
        [InlineKeyboardButton("🎮 Quiz FURIA", callback_data="quiz_start")],
        [InlineKeyboardButton("🚪 Encerrar conversa", callback_data="encerrar")]
    ]
    await update.message.reply_text("Escolha uma opção abaixo:", reply_markup=InlineKeyboardMarkup(teclado))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if query.data == "jogos":
        await query.message.reply_text("📆 Próximos jogos da FURIA:\n\n" + formatar_jogos(jogos))
        await mostrar_menu(query)
    elif query.data == "curiosidades":
        await query.message.reply_text(escolher_aleatorio(curiosidades))
        await mostrar_menu(query)
    elif query.data == "motivacao":
        await query.message.reply_text(escolher_aleatorio(frases_motivacionais), parse_mode=ParseMode.MARKDOWN)
        await mostrar_menu(query)
    elif query.data == "quiz_start":
        user_quiz_data[user_id] = {"pontos": 0, "pergunta_atual": 0}
        await enviar_pergunta(query, user_id)
    elif query.data.startswith("quiz_resposta_"):
        await processar_resposta(query, user_id, int(query.data.split("_")[-1]))
    elif query.data == "encerrar":
        await query.message.reply_text("👋 Foi incrível ter você aqui, torcedor! Continue rugindo forte com a FURIA! Até a próxima! 🔥🖤")

async def mostrar_menu(query):
    teclado = [
        [InlineKeyboardButton("📆 Jogos", callback_data="jogos")],
        [InlineKeyboardButton("🧠 Curiosidades", callback_data="curiosidades")],
        [InlineKeyboardButton("🔥 Motivação", callback_data="motivacao")],
        [InlineKeyboardButton("🎮 Quiz FURIA", callback_data="quiz_start")],
        [InlineKeyboardButton("🚪 Encerrar conversa", callback_data="encerrar")]
    ]
    await query.message.reply_text("⚡ O que você quer fazer agora?", reply_markup=InlineKeyboardMarkup(teclado))


async def enviar_pergunta(query, user_id):
    dados = user_quiz_data[user_id]
    pergunta = quiz[dados["pergunta_atual"]]
    teclado = formatar_teclado_opcoes(pergunta["opcoes"], "quiz_resposta")
    await query.message.reply_text(pergunta["pergunta"], reply_markup=InlineKeyboardMarkup(teclado))

async def processar_resposta(query, user_id, resposta):
    dados = user_quiz_data[user_id]
    correta = quiz[dados["pergunta_atual"]]["correta"]

    if resposta == correta:
        dados["pontos"] += 1
        await query.message.reply_text("✅ Resposta correta!")
    else:
        await query.message.reply_text("❌ Resposta errada!")

    dados["pergunta_atual"] += 1

    if dados["pergunta_atual"] < len(quiz):
        await enviar_pergunta(query, user_id)
    else:
        await query.message.reply_text(f"🎉 Fim do quiz! Você acertou {dados['pontos']} de {len(quiz)} perguntas!")
        del user_quiz_data[user_id]
        await mostrar_menu(query)

# Inicialização do bot
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN não encontrado. Verifique o arquivo .env")
    
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CallbackQueryHandler(button_handler))
app.run_polling()
