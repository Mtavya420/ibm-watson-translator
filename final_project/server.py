from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")


@app.route("/")
def renderIndexPage():
    return render_template('index.html')

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return translator.english_to_french(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return translator.french_to_english(textToTranslate)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)