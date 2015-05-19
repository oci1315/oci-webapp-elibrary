from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>E-Library</h1> <p>Un paragraphe</p>'
    

@app.route('/hello')
def hello():
    return '<h1>Salut, tout le monde</h1> <p><a href="/">Retour à la page d\'accueil</a></p>'
    


if __name__ == '__main__':
    # permet de servir vers l'extérieur sur Cloud9
    app.run(debug=True, host='0.0.0.0', port=8080)
