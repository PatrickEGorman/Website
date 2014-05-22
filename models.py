from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String, unique=True)
    video_name = db.Column(db.String, unique=True)

    def __init__(self, video_id, video_name):
        self.video_id = video_id
        self.video_name = video_name

    def __repr__(self):
        return "Video name: %s, Video_ID: %s" % (self.video_name, self.video_id)