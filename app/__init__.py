try:
    from app import config_private as app_ofd_config
except ImportError:
    from app import config_publ as app_ofd_config
from werkzeug.contrib.fixers import ProxyFix
from app.app import app
import flask_monitoringdashboard as dashboard
dashboard.config.init_from(file=app_ofd_config.dashcfg)
dashboard.bind(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == "__main__":
    app.run(debug=True)