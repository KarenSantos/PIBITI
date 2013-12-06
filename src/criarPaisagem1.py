import flask, flask.views
import os


class CriarPaisagem1(flask.views.MethodView):
    
    global musicas, numDaMusica

    def get(self):
        global musicas, numDaMusica
        musicas = []
        numDaMusica = 1
        return flask.render_template("criarPaisagem1.html", musicas=musicas, numDaMusica=numDaMusica)

    def post(self):
        
        global musicas, numDaMusica
        
        tamanho = len(musicas)
        tamanhoOk = False
        
        musica = flask.request.form['musica']
        nomeDaMusica = flask.request.form['nomeDaMusica']
        
        infoMusica = []
        if musica == "":
            flask.flash("Insira o link da musica.")
            return flask.render_template("criarPaisagem1.html", numDaMusica=numDaMusica, tamanhoOk=tamanhoOk, musicas=musicas)
        else:
            if nomeDaMusica == "":
                infoMusica.append("Musica " + str(numDaMusica))
            else:
                infoMusica.append(nomeDaMusica)
            
            infoMusica.append(musica.split("=")[-1])

            musicas.append(infoMusica)
            
            paisagem1 = open("static/paisagem1.txt", "w")
            
            for info in musicas:
                paisagem1.write(info[0] + '\n')
                paisagem1.write(info[1] + '\n')

            paisagem1.close()
            
            numDaMusica += 1
            tamanho += 1
            if len(musicas) >= 3:
                tamanhoOk = True
            
            return flask.render_template("criarPaisagem1.html", 
                                         numDaMusica=numDaMusica, 
                                         musicas=musicas, 
                                         tamanho=tamanho,
                                         tamanhoOk=tamanhoOk)        
