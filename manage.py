from reddit_backend.application import create_app
from flask_script import Manager
from flask_script import Server


app = create_app('development')

manager = Manager(app)
manager.add_command('runserver', Server('0.0.0.0', 7000))


if __name__ == "__main__":
    manager.run()

