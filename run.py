from werkzeug.contrib.fixers import ProxyFix
from flask_app.app import app
import flask_monitoringdashboard as dashboard
from flask_app.config import dash_cfg
dashboard.config.init_from(file=dash_cfg)
dashboard.bind(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == "__main__":
    app.run(debug=True)