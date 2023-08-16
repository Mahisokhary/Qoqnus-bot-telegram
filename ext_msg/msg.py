import openai
import json
import os

from pathlib import Path
from telegram.ext import CallbackContext
from telegram import Update

def msg(update: Update, context: CallbackContext) -> None:
	with open("var/openai", "r") as f:
		openai.api_key = f.read()
	user_id = update.message.from_user.id
	if not Path(f"var/gpt/{user_id}").exists():
		os.system(f"touch var/gpt/{user_id}")
		with open(f"var/gpt/{user_id}", "w") as f:
			json.dump({"msg": []}, f)
			f.close()
	with open(f"var/gpt/{user_id}", "r") as f:
		full_msg = json.load(f)
		f.close()
	full_msg["msg"] += [{"role": "user", "content": update.message.text}]
	response = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages= full_msg["msg"],
		max_tokens=200,
		temperature=1.2
	)
	msg = response.choices[0]["message"]["content"]
	update.message.reply_text(msg)
	full_msg["msg"] += [{"role": "assistant", "content": msg}]
	with open(f"var/gpt/{user_id}", "w") as f:
		json.dump(full_msg, f)
		