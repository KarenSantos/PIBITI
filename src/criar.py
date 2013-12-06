import flask, flask.views
import os

class Criar(flask.views.MethodView):

    def get(self):
        
        return flask.render_template("criar.html")

    