import json
import random
from telegram import InlineKeyboardButton

def carregar_arquivo(nome):
    try:
      with open(nome, "r", encoding="utf-8") as f:
         return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise Exception(f"Erro ao carregar '{nome}': {e}")

def formatar_jogos(lista):
    return "\n".join(lista)

def escolher_aleatorio(lista):
    return random.choice(lista)

def formatar_teclado_opcoes(opcoes, prefixo):
    return [[InlineKeyboardButton(text=opt, callback_data=f"{prefixo}_{i}")] for i, opt in enumerate(opcoes)]
