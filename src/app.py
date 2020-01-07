from flask import Flask

from src.controllers.home import home
from src.controllers.notes import notes

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(notes, url_prefix='/notes')


if __name__ == '__main__':
    app.run()
