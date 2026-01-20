from flask import Flask
from routes.main import main_bp
from routes.questions import questions_bp
from routes.generator import generator_bp
from routes.admin import admin_bp

app = Flask(__name__)
# Secret key is required for flash messages
app.secret_key = 'your-secret-key-here'

app.register_blueprint(main_bp)
app.register_blueprint(questions_bp)
app.register_blueprint(generator_bp)
app.register_blueprint(admin_bp)


# Run app
if __name__ == '__main__':
    app.run(debug=True)
