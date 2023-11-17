"""Seed file to make sample data for db"""


from models import Pet, db
from app import app

#Create all tables
db.drop_all()
db.create_all()

sammy = Pet(name="Sammy", species="dog", photo_url="https://rpiathletics.com/images/2016/9/1/Singletary,%20Keith.jpg", age=3, available=True)
scruff = Pet(name="Scruff", species="dog", photo_url="https://static.wixstatic.com/media/cf773f_79dabb25fec44ed6bbf768342b8e547c~mv2.jpg/v1/fill/w_256,h_256,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/Kristoff%202022%20-%201_edited.jpg", age=8, available=False)
molly = Pet(name="Molly", species="dog", photo_url="https://i.pinimg.com/474x/87/b6/f7/87b6f79d997b5532858a731507a45d9c.jpg", age=4, available=True)
fido = Pet(name="Fido", species="dog", photo_url="https://i.pinimg.com/474x/7a/96/0e/7a960e82ce21363fe44ac6eceab4935e.jpg", age=2, available=True)

db.session.add_all([sammy, scruff, molly, fido])
db.session.commit()