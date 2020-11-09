from try_database import seed_features
from starter_app.models import User, Property
from starter_app import app, db
from dotenv import load_dotenv
load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()

    ian = User(username='Ian', email='ian@aa.io')
    javier = User(username='Javier', email='javier@aa.io')
    dean = User(username='Dean', email='dean@aa.io')
    angela = User(username='Angela', email='angela@aa.io')
    soonmi = User(username='Soon-Mi', email='soonmi@aa.io')
    alissa = User(username='Alissa', email='alissa@aa.io')

    db.session.add(ian)
    db.session.add(javier)
    db.session.add(dean)
    db.session.add(angela)
    db.session.add(soonmi)
    db.session.add(alissa)

    db.session.commit()

    properties = seed_features()

    for prop in properties:
        prop_db = Property(**prop)
        db.session.add(prop_db)
    db.session.commit()

    # prop = Property(Latitude=50.1234567890, Longitude=-90.12345678901234567890)
    # db.session.add(prop)
    # db.session.commit()
