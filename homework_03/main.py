import uvicorn
from view import ping
pip
if __name__ == '__main__':
    uvicorn.run("view:app", reload=True)