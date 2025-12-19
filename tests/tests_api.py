from fastapi.testclient import TestClient
from api.app2 import app
client=TestClient(app)
def health_test_check():
    response=client.grt("/")
    assert response.statuscode == 200

def test_recommendation_endpoint():
    response=client.get("/recommend/1?top_k=5")
    assert response.statuscode == 200
    data=response.json()
    assert isinstance(data,list)
    assert len(data)==5
