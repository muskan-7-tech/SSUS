import streamlit as st

from database.mongodb import student_collection

st.title("student Registration")

first_name = st.text_input(
    "first Name"
)

last_name = st.text_input(
    "Last Name"
)

email = st.text_input(
    "Email"
)

course = st.text_input(
    "course"
)

if st.button("Register Student"):
    student_collection.insert_one({

    "first_name": first_name,

    "last_name": last_name,

    "email":email,

    "course": course


    })

    st.success(
    "student Registered successfylly"
    )
