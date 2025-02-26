from .app import db


class Numbers(db.Model):
    """
    Таблица данных humanity<>numbers
    """
    __tablename__ = 'numbers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False, default='')
    font_color = db.Column(db.String, nullable=False, default='#FFFFFF')
    background_color = db.Column(db.String, nullable=False, default='#000000')
