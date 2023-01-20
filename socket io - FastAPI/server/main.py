import uvicorn
from fastapi import FastAPI

from socket_app import sio_app




app = FastAPI()
app.mount('/', app = sio_app)



@app.get('/')
async def home():
    return {'message': 'Hello World'}






if __name__ == '__main__':
    uvicorn.run('main:app', reload = True)

