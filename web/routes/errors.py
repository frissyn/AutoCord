import flask

from web import app


@app.errorhandler(404)
def _handle_404(e: str):
    # print("FRE:::", e)
    return flask.render_template("errors/404.html")


@app.errorhandler(500)
def _handle_500(e: str):
    # print("FRE:::", e)
    return flask.render_template("errors/500.html")
