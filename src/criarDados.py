import flask, flask.views
import os

class CriarDados(flask.views.MethodView):
    
    def get(self):
        
        image = "0.png"
        
        musicInfo = open("static/songs.txt").readlines()
        songs = []
        for i in range(0, len(musicInfo)-1, 2):
            songs.append([musicInfo[i], musicInfo[i+1]])
        
        return flask.render_template("criarDados.html", songs=songs, image=image)

    def post(self):
        
        musicInfo = open("static/songs.txt").readlines()
        songs = []
        for i in range(0, len(musicInfo)-1, 2):
            songs.append([musicInfo[i], musicInfo[i+1]])
        
        nomeDaPlaylist = flask.request.form['nomeDaPlaylist']
        comentario = flask.request.form['comentario']
        image = flask.request.files['file']

        if nomeDaPlaylist == "":
            flask.flash("A sua playlist precisa ter um nome.")
            return flask.render_template("criarDados.html", comentario=comentario, image=image, songs=songs)
        
        if comentario == "":
            flask.flash("Descreva como voce criou suas paisagens.")
            return flask.render_template("criarDados.html", nomeDaPlaylist=nomeDaPlaylist, image=image, songs=songs)

        if image == "":
            flask.flash("Insira uma imagem valida")
            return flask.render_template("criarDados.html", nomeDaPlaylist=nomeDaPlaylist, comentario=comentario, songs=songs)
            

        ALLOWED_EXTENSIONS = set(["png", "PNG", "jpg", "JPG", "jpeg", "JPEG", "jpe", "JPE"])
        
        imageType = image.filename.rsplit(".", 1)[1]
        
        if imageType in ALLOWED_EXTENSIONS:
                
            images = os.listdir("static/images/")
            for i in range(len(images)-1, -1, -1):
                if images[i] == "Thumbs.db":
                    images.remove(images[i])
                    
            lastImage = images[-1].split(".")[0]
            filename = str(int(lastImage)+1) + "." + imageType
             
            image.save('static/images/' + filename)
                
        os.remove("static/songs.txt")

        playlists = os.listdir("static/playlists/")
        novaPlay = int(playlists[-1].split(".")[0])+1
        novaPlay = str(novaPlay) + ".txt"
                
        playlist = open("static/playlists/" + novaPlay, "w")
        playlist.write(nomeDaPlaylist + "\n" + image + "\n" + comentario + "\n")
    
        for i in range(len(songs)):
            playlist.write(songs[i][0])
            playlist.write(songs[i][1])
        
        playlist.close()
                
        return flask.render_template("criadaComSucesso.html", 
                                     nomeDaPlaylist=nomeDaPlaylist, 
                                     image=filename,
                                     novaPlay=novaPlay, 
                                     songs=songs)
        