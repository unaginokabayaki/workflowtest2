from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "でぷろいかんりょうしました"

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200