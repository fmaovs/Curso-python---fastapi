from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return 'Hola FastAPI'

@app.get('/url')
async def getUrl():
    return {'url_repo':'https://github.com/fmaovs'}