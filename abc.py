from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    singup: datetime | None=None
    friends: list[int]= []
    

external_data = {
    "id": "123",
    "name": "Jhone Bon",
    "signup": "2017-06-01 12:22",
    "friends": [1, '2', '3']
}

user = User(**external_data)
print(user)
print(user.id)