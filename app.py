from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá Mundo novo'

@app.route('/contato')
def contato():
    return 'glison.gfo@gmail.com - (84)98844-8288'

@app.route('/alunos')
def alunos():
    return render_template('alunos.html')
    # return '<ul><li>Gilson</li></ul>'

@app.route('/professores')
def professores():
    return render_template('professores.html')