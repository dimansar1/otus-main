import uvicorn
from view import ping

if __name__ == '__main__':
    uvicorn.run("view:app", reload=True)