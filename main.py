#!/usr/bin/env python
import os, requests, json, mammoth, time
from rich import print
from rich.markdown import Markdown
from dotenv import load_dotenv
from lib.openlib import OpenAI
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_openai.llms import OpenAI
from tools.functions import handle_user_input, save_conversation


app = Flask(__name__)
# app.debug = True
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024
CORS(app)


# Get API key
load_dotenv()
api_key = os.getenv("open_ai_key")
# brave_api = os.getenv("brave_api")
llm = OpenAI(model="gpt-3.5-turbo-instruct",api_key=api_key, temperature=0.9)
print("api_key-----", api_key)

@app.route('/api/proprietary-assistant', methods = ['POST'])
def proprietary_assistant():
    prompt = request.json["prompt"]
    gpt_output = llm(prompt)
    markdown = Markdown(gpt_output, code_theme="one-dark")
    print('-------------------MARK-----------------', markdown)

    return jsonify({'result': gpt_output})

if __name__ == "__main__":
    print("kkk")
    app.run(port=5050)
