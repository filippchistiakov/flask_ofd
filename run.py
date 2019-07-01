import flask_monitoringdashboard as dashboard
from werkzeug.contrib.fixers import ProxyFix

from flask_app.config import dash_cfg
from flask_app.views import app

dashboard.config.init_from(file=dash_cfg)
dashboard.bind(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == "__main__":
    app.run(debug=True)
