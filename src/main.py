import flask, flask.views
import os
import random


class Main(flask.views.MethodView):
    def get(self):
        playFiles = os.listdir("static/playlists/")
        random.shuffle(playFiles)
        
        playlists = {}
        
        sample = 3;
        if len(playFiles) < sample:
            sample = len(playFiles)
             
        for i in range(sample):
            playlist = []
            fileInfo = open("static/playlists/" + playFiles[i], "r").readlines()
            
            playlist.append(fileInfo[0]) #Name
            playlist.append(fileInfo[1]) #Image
            playlist.append(fileInfo[4]) #First Video
            
            playlists[playFiles[i]] = playlist
        
        return flask.render_template("main.html", playlists=playlists)
        flask.abort(404)