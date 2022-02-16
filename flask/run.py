from app import app, create_app
from api.data import data
from api.analyze import analyze
from api.finance import finance

app.register_blueprint(data, url_prefix="/api/data")
app.register_blueprint(analyze, url_prefix="/api/analyze")
app.register_blueprint(finance, url_prefix="/api/finance")

if __name__ == '__main__':
    create_app().run(debug=True, port="5001", host="0.0.0.0")
