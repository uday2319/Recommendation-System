import streamlit as st
import pandas as pd
import requests


users = pd.read_csv("C:/Users/udayi/Downloads/users.csv")

st.set_page_config(page_title="Job Recommender", layout="centered")
st.title("💼 Job / Internship Recommendation System")


user_id = st.selectbox(
    "Select User",
    users["user_id"],
    format_func=lambda x: f"User {x}"
)

top_k = st.slider("Number of recommendations", 1, 5, 10)

if st.button("Get Recommendations"):
    with st.spinner("Finding best jobs for you..."):
        response = requests.get(
            f"http://127.0.0.1:8000/recommend/{user_id}",
            params={"top_k": top_k}
        )

    if response.status_code == 200:
        data = response.json()

        if "recommendations" in data:
            st.success("Recommended Jobs!")

            for job in data["recommendations"]:
                st.markdown(
                    f"""
                    ### {job['title']}
                    📍 **Location:** {job['location']}  
                    💼 **Type:** {job['job_type']}
                    ---
                    """
                )
        else:
            st.warning(data["message"])
    else:
        st.error("Backend API not reachable")
