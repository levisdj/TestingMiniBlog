# Main application module; creates a shell context that adds the database instance and models to the shell session
from app import app, db, cli
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

