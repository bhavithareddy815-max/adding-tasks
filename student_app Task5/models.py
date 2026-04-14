from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Student(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    department=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(150), nullable=False, unique=True)
    def __repr__(self):
      return f"<Student {self.name}>"