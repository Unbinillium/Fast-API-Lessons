import uvicorn
from fastapi import FastAPI
from src.routers import router

app = FastAPI(docs_url='/api/docs')


@app.get('/hello')
def hello():
    return 'hello'

@app.post('/dataset')
def dataset(data: list[dict], x_from: float, x_to: float, y_from: float, y_to: float):
    print(data)
    count = 0
    for count_data in data:
        if count_data["lat"] > x_from and count_data["lat"] < x_to: 
            print(count_data)
            count += 1
    return count

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True,
    )
