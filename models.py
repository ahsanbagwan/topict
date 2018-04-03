from topict import db

class Entries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(64), index=True, unique=True)
    
    def __repr__(self):
        return '<Entries {}>'.format(self.entry)    