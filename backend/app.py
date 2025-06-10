from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/messages', methods=['GET'])
def get_messages():
    messages = Message.query.order_by(Message.created_at).all()
    return jsonify([message.to_dict() for message in messages])

@app.route('/api/messages', methods=['POST'])
def create_message():
    data = request.json
    if not data or 'content' not in data:
        return jsonify({'error': 'Missing content'}), 400
    
    message = Message(content=data['content'])
    db.session.add(message)
    db.session.commit()
    return jsonify(message.to_dict()), 201

@app.route('/api/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = Message.query.get_or_404(message_id)
    db.session.delete(message)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
