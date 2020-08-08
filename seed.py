from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()


Pet.query.delete()

p1 = Pet(name="Fluffy", species="Cat", photo_url="https://assets.rebelmouse.io/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpbWFnZSI6Imh0dHBzOi8vYXNzZXRzLnJibC5tcy81MDc0MTQzL29yaWdpbi5qcGciLCJleHBpcmVzX2F0IjoxNjI3NTE3MjQ4fQ.AUsl3oEmShfpcjkT8PVJTuMozeXph4kpNm5Xi1tlRBk/img.jpg?width=980", age=2, notes="Friendly. Likes other cats and dogs")

p2 = Pet(name="Roger", species="Porcupine",
         photo_url="https://i.ytimg.com/vi/ZphlCdI2yqA/maxresdefault.jpg", age=3)

p3 = Pet(name="Midnight", species="Cat", photo_url="https://www.animalfriends.co.uk/app/uploads/2018/10/31102444/why-isnt-anyone-adopting-black-cats.jpg",
         age=1, notes="Friendly. Likes other cats. Dogs are yucky!")


db.session.add_all([p1, p2, p3])
db.session.commit()
