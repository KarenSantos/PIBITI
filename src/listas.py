import flask, flask.views
import os


class Listas(flask.views.MethodView):
            
    def get(self):
        
        playFiles = os.listdir("static/playlists/")

        playlists = {}
        
        for file in playFiles:
            playlist = []
            fileInfo = open("static/playlists/" + file, "r").readlines()
            
            playlist.append(fileInfo[0]) #Name
            playlist.append(fileInfo[1]) #Image
            playlist.append(fileInfo[4]) #First Video
            
            playlists[file] = playlist
        
        return flask.render_template("listas.html", playlists=playlists)