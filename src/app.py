import flask, flask.views
import settings

# Views
from main import Main
from criar import Criar
from criarStart import CriarStart
from criarMusicas import CriarMusicas
from criarDados import CriarDados
from listas import Listas
from ouvir import Ouvir
from criarPaisagem1 import CriarPaisagem1
from criarPaisagem2 import CriarPaisagem2
from criarTransicao import CriarTransicao

app = flask.Flask(__name__)
app.secret_key = settings.secret_key

# Routes
app.add_url_rule('/',
                 view_func = Main.as_view('main'),
                 methods=['GET'])

app.add_url_rule('/criar/',
                 view_func=Criar.as_view('criar'),
                 methods=['GET'])

app.add_url_rule('/criar/start/',
                 view_func=CriarStart.as_view('criarStart'),
                 methods=['GET', 'POST'])

app.add_url_rule('/criar/paisagem1/',
                 view_func=CriarPaisagem1.as_view('criarPaisagem1'),
                 methods=['GET', 'POST'])

app.add_url_rule('/criar/transicao/',
                 view_func=CriarTransicao.as_view('criarTransicao'),
                 methods=['GET', 'POST'])

app.add_url_rule('/criar/paisagem2/',
                 view_func=CriarPaisagem2.as_view('criarPaisagem2'),
                 methods=['GET', 'POST'])

app.add_url_rule('/criar/musicas/',
                 view_func=CriarMusicas.as_view('criarMusicas'),
                 methods=['GET', 'POST'])

app.add_url_rule('/criar/dados/',
                 view_func=CriarDados.as_view('criarDados'),
                 methods=['GET', 'POST'])

app.add_url_rule('/listas/',
                 view_func=Listas.as_view('listas'),
                 methods=['GET'])

app.add_url_rule('/ouvir/',
                 view_func=Ouvir.as_view('ouvir'),
                 methods=['POST'])

@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404

app.debug = True
app.run()