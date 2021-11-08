from api.database import db, migrate
from api.views import app
from config import Config

app.config.from_object(Config)

db.init_app(app)

migrate.init_app(app, db)

if __name__ == '__main__':
    app.run()
