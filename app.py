from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

##############################
## initialisation des extensions
##############################

bootstrap = Bootstrap(app)


##############################
## Définition des routes (endpoints)
##############################

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name='Anonyme'):
    return render_template('hello.html', name=name)
    




if __name__ == '__main__':
    # permet de servir vers l'extérieur sur Cloud9
    app.run(debug=True, host='0.0.0.0', port=8080)
