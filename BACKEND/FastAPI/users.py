from fastapi import FastAPI

app = FastAPI()

#Entidad user
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users = [User('Mauricio', 'Mao', 'url','https://github.com/fmaovs',26)]

@app.get('/usersjson')
async def usersjson():
    return [{'name': 'Mauricio', 'surname': 'fmaovs', 'url':'https://github.com/fmaovs', 'age': 26},
        {'name': 'Dante', 'surname': 'esenene', 'url':'https://github.com/snene', 'age':1}]