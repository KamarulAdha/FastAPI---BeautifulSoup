import uvicorn
from app import app


if __name__ == '__main__':
    uvicorn.run("debug_server:app", host='127.0.0.1', port=8000, reload=True)
