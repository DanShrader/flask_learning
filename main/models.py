from main import db


class Another(db.Model):
    id = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True)
    title = db.Column(db.String(80), nullable=False )
    grouping = db.Column(db.Integer(), nullable=False )

    def __repr__(self):
        return self.title


class Entry(db.Model):
    id = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True)
    title = db.Column(db.String(80), nullable=False )
    grouping = db.Column(db.Integer(), nullable=False )

    def __repr__(self):
        return "<title: {}>".format(self.title)
