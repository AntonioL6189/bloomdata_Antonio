from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import openaq


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(app)
api = openaq.OpenAQ()


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String)
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return f'datetime={self.datetime},value={self.value}'


def get_results():
    city = 'Los Angeles'
    parameter = 'pm25'
    status, body = api.measurements(city=city, parameter=parameter)
    measurements = body['results']
    results_list = [(entry['date']['utc'], entry['value'])
                    for entry in measurements]
    return results_list


@app.route('/')
def root():
    potentially_risky = Record.query.filter(Record.value >= 18).all()
    potentially_risky_strings = str(potentially_risky)
    return potentially_risky_strings


@app.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    results = get_results()

    for utc_datetime, value in results:
        record = Record(datetime=utc_datetime, value=value)
        DB.session.add(record)

    DB.session.commit()
    return 'Data refreshed'
