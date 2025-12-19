from fastapi import FastAPI
from model.recommender import recommend_jobs

app=FastAPI(title="job recommendation system")
@app.get("/")
def home():
    return {"message":"job recommendation api is running"}
@app.get("/recommend/{user_id}")
def get_recommendation(user_id:int,top_k:int=5):
    result=recommend_jobs(user_id,top_k)

    if isinstance(result, str):
        return {"message": result}
    
    return {
        "user_id": user_id,
        "recommendations": result.to_dict(orient="records")
    }