# coding: utf-8
import flask, flask.views


class CriarStart(flask.views.MethodView):
    
    def get(self):
        
        paisagem1 = open("static/paisagem1.txt", "r")
        paisagem2 = open("static/paisagem2.txt", "r")
        transicao = open("static/transicao.txt", "r")
        
        if (paisagem1.read() != "") and (paisagem2.read() != "") and (transicao.read() != ""):
            return flask.render_template("criarDados.html")       
        
        if (paisagem2.read() != "") and (transicao.read() != ""):
            return flask.render_template("criarPaisagem1.html")
        
        if (paisagem1.read() != "") and (transicao.read() != ""):
            return flask.render_template("criarPaisagem2.html") 
        
        if (paisagem1.read() != "") and (paisagem2.read() != ""):
            return flask.render_template("criarTransicao.html") 
        
        
        if (paisagem1.read() == "") and (paisagem2.read() == "") and (transicao.read() == ""):
            resp = "all3options"
                    
        if (paisagem1.read() == "") and (paisagem2.read() == "") and (transicao.read() != ""):
            resp = "paisagem1paisagem2"
            
        if (paisagem1.read() == "") and (paisagem2.read() != "") and (transicao.read() == ""):
            resp = "paisagem1transicao"
            
        if (paisagem1.read() != "") and (paisagem2.read() == "") and (transicao.read() == ""):
            resp = "paisagem2transicao"
        
        flask.flash("Resp foi: " + resp)
        return flask.render_template("criarStart.html", resp=resp)

    def post(self):
        
        try:
            start = flask.request.form['start']
        except:
            start = ""
            
        if start == "paisagem1":
            render = flask.render_template("criarPaisagem1.html")
        elif start == "transicao":
            render = flask.render_template("criarTransicao.html")
        elif start == "paisagem2":
            render = flask.render_template("criarPaisagem2.html")
        else:
            flask.flash("Escolha uma das opções acima.")
            render = flask.render_template("criarStart.html")
        
        return render
