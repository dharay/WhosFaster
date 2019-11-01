from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello World from fast api!"}

@app.get("/fib/{amt}")
async def fib(amt: int, q: str = None):
    return calulateFib(amt)

def calulateFib(n):
    if n==0 or n == 1: 
        return n
    else: 
        return calulateFib(n-1)+calulateFib(n-2) 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8090)