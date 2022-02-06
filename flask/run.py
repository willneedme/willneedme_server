from app import app, create_app
from api.data import finance
from api.analyze import analyze

app.register_blueprint(finance, url_prefix="/api/finance")
app.register_blueprint(analyze, url_prefix="/api/analyze")

if __name__ == '__main__':
    create_app().run(debug=True, port="5001", host="0.0.0.0")
