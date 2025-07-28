from app import create_app
from app.extensions import cache
from app.auth.auth_utils import generate_jwt_token
import flask_monitoringdashboard as dashboard

app = create_app()
dashboard.config.init_from(file='config.cfg')

if __name__ == "__main__":
    dashboard.bind(app)
    cache.init_app(app, config={'CACHE_TYPE': 'simple'})

    with app.app_context():
        token = generate_jwt_token({"user": "main"})
        cache.clear()

    app.run(host='0.0.0.0', port=5000, debug=True)

# docker-compose run web flask db init       # only once
# docker-compose run web flask db migrate -m "initial schema"
# docker-compose run web flask db upgrade