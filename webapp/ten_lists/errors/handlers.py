from flask import Blueprint, render_template

errors = Blueprint("errors", "__name__")


@errors.app_errorhandler(400)
def error_400(error):
    return render_template("errors/400.html"), 400


@errors.app_errorhandler(401)
def error_401(error):
    return render_template("errors/401.html"), 401


@errors.app_errorhandler(404)
def error_404(error):
    return render_template("errors/404.html"), 404


@errors.app_errorhandler(403)
def error_403(error):
    return render_template("errors/403.html"), 403


@errors.app_errorhandler(500)
def error_500(error):
    return render_template("errors/500.html"), 500


@errors.app_errorhandler(501)
def error_501(error):
    return render_template("errors/501.html"), 501


@errors.app_errorhandler(502)
def error_502(error):
    return render_template("errors/502.html"), 502


@errors.app_errorhandler(503)
def error_503(error):
    return render_template("errors/503.html"), 503


@errors.app_errorhandler(504)
def error_504(error):
    return render_template("errors/504.html"), 504
