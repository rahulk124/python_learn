import streamlit as st

st.title("My First Streamlit App")
st.header("Welcome to my app")
st.subheader("This is a subheader")
st.write("Hello, Rahul!")
st.text("This is a text element")
st.markdown("This is a **markdown** element")
st.button("Click me!")
st.checkbox("Check me!")
st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.text_input("Enter your name")
st.text_area("Enter your message")
 #st.select_box("Choose an option", ["Option 1", "Option 2", "Option 3"]) 
st.slider("Select a value", 0, 100, 50)
st.date_input("Select a date")
st.time_input("Select a time")  
st.file_uploader("Upload a file")   
st.color_picker("Pick a color")
st.error("This is an error message")
st.success("This is a success message")


name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name}!")