import streamlit as st
from forms.contact import contact_form

@st.dialog("Contact me")
def show_contact_form():
    contact_form()

st.title("About Me Section")

st.subheader("Experience and Qualification")
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/daveworld.jpg" , width=200)

with col2:
    st.title("Eniola Ademola")
    st.write("Data Scientist | Frontend Engineer")
    if st.button("🧾 Contact me"):
        show_contact_form()




st.write(
    """
        - 3 years of experience in Frontend Development and Data Science
        - B.Sc. in Computer Science
        - i am a self-taught programmer
        - Excellent team-player and problem-solver
    """
)


# Skills
st.write("## Skills")
st.write(
    """
       - Programming: Python, JAvascript, Typescript, SQL
       - Data Visualization: Matplotlib, Seaborn, Plotly, Tableau, PowerBI
       - Modeling: Logistic Regression, Random Forest, XGBoost, Neural Networks
       - Database: MySQL
       - LLM: GPT, BERT, Transformer
    """
)
