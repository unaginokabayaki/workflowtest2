from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Cloud Run Flask App</h1><p>修正しました！</p>"

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200