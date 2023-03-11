# pylint: disable=missing-module-docstring
from flask import Flask, render_template, request
from machinetranslation import translator
# import json

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    '''test'''
    textToTranslate = request.args.get('textToTranslate')
    # textToTranslate = "hi how are you"
    # # Write your code here
    translated_text = translator.english_to_french(textToTranslate)
    print("translated_text---> " + translated_text)
    return translated_text


@app.route("/frenchToEnglish")
def frenchToEnglish():
    '''test'''
    textToTranslate = request.args.get('textToTranslate')
    # textToTranslate = "Bonjour"
    # Write your code here
    translated_text = translator.french_to_english(textToTranslate)
    return translated_text


@app.route("/")
def render_index_page():
    '''docstring'''
    # Write the code to render template
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
