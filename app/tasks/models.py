from app.helpers.extensions import db
from datetime import datetime

class Task(db.Model):
    __tablename__ = "task"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), default="To Do")
    est_time = db.Column(db.Float)
    due_date = db.Column(db.DateTime)
    priority = db.Column(db.String(20)) #low, medium, high
    assignee_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    project_id = db.Column(db.Integer)
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)