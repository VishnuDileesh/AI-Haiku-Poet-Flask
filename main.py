from flask import Flask, jsonify, request, render_template

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate)

import os 

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

app = Flask(__name__)

chatllm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.9, model="gpt-3.5-turbo")

human_template = ("Write me a haiku about {theme}")

human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

system_template = ("You are an expert haiku poet who is in love with nature")

system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])




@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get-haiku", methods=['POST'])
def get_haiku():
    theme = request.form.get('theme', None)
    haiku = chatllm.invoke(chat_prompt.format_prompt(theme=theme).to_messages())
    formatted_haiku = haiku.content.replace("\n", "<br>")
    return f"<h3 style='white-space: pre-wrap;'>{formatted_haiku}</h3>"


@app.route("/health")
def read_health():
    return jsonify({"Health": "Ok"})

if __name__ == "__main__":
    app.run(debug=True)



