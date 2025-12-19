import pandas as pd
import numpy as np
jobs=pd.read_csv("C:/Users/udayi/Downloads/jobs.csv")
users=pd.read_csv("C:/Users/udayi/Downloads/users.csv")
jobs["text"]=jobs["title"]+" "+jobs["description"]+" "+jobs["required_skills"]

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer(stop_words="english")
job_vectors=vectorizer.fit_transform(jobs["text"])

def get_user_profile(user_id):
    user=users[users["user_id"]==user_id].iloc[0]
    return user
def context_filter_jobs(user,jobs):
    filtered=jobs[(jobs["location"]==user["preferred_location"]) & (jobs["job_type"]==user["preferred_job_type"]) 
                     &(jobs["experience_level"]==user["experience_level"])]
    return filtered

from sklearn.metrics.pairwise import cosine_similarity
def recommend_jobs(user_id,top_k=5):
    user=get_user_profile(user_id)

    filtered_jobs=context_filter_jobs(user,jobs)
    if filtered_jobs.empty:
        return " No jobs found for this context"
    filtered_vectors=vectorizer.transform(filtered_jobs["text"])
    user_vector=vectorizer.transform([user["skills"]])

    scores=cosine_similarity(user_vector,filtered_vectors)[0]

    top_indices=np.argsort(scores)[ ::-1][:top_k]

    recommendations=filtered_jobs.iloc[top_indices][["job_id","title","location","job_type"]]
    return recommendations
print(recommend_jobs(user_id=1, top_k=7))




