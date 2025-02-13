from flask import Flask
from flask_socketio import SocketIO
from flask_security import Security, SQLAlchemyUserDatastore
from models import db, User, Role
from config import Config
from routes import auth, loan, payment

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

with app.app_context():
    db.create_all()

app.register_blueprint(auth.bp)
app.register_blueprint(loan.bp)
app.register_blueprint(payment.bp)

socketio = SocketIO(app)

@socketio.on('loan_request')
def handle_loan_request(data):
    socketio.emit('new_loan_request', data)

if __name__ == '__main__':
    socketio.run(app, debug=True)