from datetime import datetime
from azuretext import db


class comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(5000), unique = False, nullable = False)
    time = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f"comment('{self.text}', '{self.time}')"


class textanalysis(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(5000), unique = False, nullable = False)
    detectedLanguage = db.Column(db.String(50), unique = False, nullable = False)
    language_iso639Name = db.Column(db.String(4), unique = False, nullable = False)
    sentiment = db.Column(db.Float, unique = False, nullable = False)
    translation = db.Column(db.String(5000), unique = False, nullable = True)
    KeyPhrase = db.Column(db.String(5000), unique = False, nullable = False)

    def __repr__(self):
        return f"textanalysis('{self.text}', '{self.detectedLanguage}', '{self.language_iso639Name}', '{self.sentiment}, '{self.translation}', '{self.KeyPhrase}')"


# text_analysis_1 = textanalysis(text = 'Joensuussa monipuolista ohjelmaa on tarjolla 28.9.2018 klo 15-20 I', detectedLanguage = 'fi', language_iso639Name = 'fi', sentiment = 0.69921875, translation = 'orning traffic, when t', KeyPhrase = str(['Researchers','and']))