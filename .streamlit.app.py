import streamlit as st

# Set the page title
st.set_page_config(page_title="Letter A Box")

# Display a title
st.title("Streamlit Web App")

# Display a box with the letter "A"
st.markdown(
    """
    <div style="
        display: flex;
        align-items: center;
        justify-content: center;
        height: 200px;
        width: 200px;
        border: 2px solid black;
        background-color: lightgray;
        font-size: 50px;
        font-weight: bold;
        color: black;
        margin: auto;
    ">
        A
    </div>
    """,
    unsafe_allow_html=True
)
