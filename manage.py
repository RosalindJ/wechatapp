# -*- coding: utf-8 -*-

import os

from flask.ext.script import Manager, Server
from flask.ext.script.commands import ShowUrls, Clean
from app import app
from app.models import db

manager = Manager(app)
manager.add_command("runserver", Server(host="127.0.0.1", port=5000))
manager.add_command("server", Server(host="0.0.0.0", port=5000))
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())


@manager.shell
def make_shell_context():
    """ Creates a python REPL with several default imports
        in the context of the app
    """

    return dict(app=app, db=db)


@manager.command
def createdb():
    """ Creates a database with all of the tables defined in
        your SQLAlchemy models
    """
    pass
    #db.create_all()


if __name__ == "__main__":
    manager.run()
