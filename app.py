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
    
@app.route('/erreur')
def erreur():
    # erreur volontaire
    a = 3 / 0


@app.route('/demo')
def demo_templates():
    booleen = False
    montagnes = ['Moléson', 'Vanil Noir', 'Dent de Broc']
    pays = {'Suisse' : 'Bern', 'France' : 'Paris'}

    return render_template('demo-jinja2.html', 
        booleen=booleen,
        montagnes=montagnes,
        pays=pays
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    # permet de servir vers l'extérieur sur Cloud9
    app.run(debug=True, host='0.0.0.0', port=8080)
