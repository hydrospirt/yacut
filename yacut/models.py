from datetime import datetime as dt

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=dt.utcnow)

    def to_dict(self):
        return dict(
            original=self.original,
            short=self.short
        )

    def from_dict(self, data):
        for field, api_field in zip(('original', 'short'), ('url', 'custom_id')):
            setattr(self, field, data.get(api_field))
