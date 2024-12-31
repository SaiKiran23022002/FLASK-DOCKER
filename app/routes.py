from flask import render_template


def register_routes(app):

    #endpoint which renders the index.html file
    @app.route("/",methods=['GET'])
    def render_home():
        return render_template("index.html")