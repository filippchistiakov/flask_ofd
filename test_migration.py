from flask_app.app import app
from flask_app.models_old import  CloseshiftModel, OpenshiftModel, ReceiptModel
#from flask_app.models import  CloseshiftModel, OpenshiftModel, ReceiptModel
db = app.extensions['sqlalchemy'].db
print([cls for cls in db.Model._decl_class_registry.values()
 if isinstance(cls, type) and issubclass(cls, db.Model)])