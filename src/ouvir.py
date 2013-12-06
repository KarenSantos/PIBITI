import flask, flask.views
import os

class Ouvir(flask.views.MethodView):
    
    def post(self):
        playlistName = flask.request.form['playlist']
        video = flask.request.form['video']
        
        fileInfo = open("static/playlists/" + playlistName, "r").readlines()
        
        playlist = []
        musicas = []
        
        playlist.append(fileInfo[0]) #Nome
        playlist.append(fileInfo[1]) #Figura
            
        for i in range(3, len(fileInfo)-1, 2):
            musicas.append([fileInfo[i], fileInfo[i+1]])
        
        return flask.render_template("ouvir.html", playlistName=playlistName, playlist=playlist, musicas=musicas, video=video)