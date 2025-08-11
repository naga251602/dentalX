from flask import Flask, send_from_directory, request
from llm.gemini import getResponse

app = Flask(__name__, static_folder="dist", static_url_path="")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def static_proxy(path):
    try:
        return send_from_directory(app.static_folder, path)
    except:
        return send_from_directory(app.static_folder, "index.html")

@app.post('/llm')
def llmQuery():
    data = request.get_json()
    res = getResponse(
        f"take this content '{data['notes']}' and make it '{data['type']}' and translate to this language '{data['lang']}'. give only sentence nothing else not special chars like \\n \\t"
    )
    message_text = res.candidates[0].content.parts[0].text
    return {"response": message_text}

# Entry point for Google Cloud Function
def flask_app(request):
    return app(request)
