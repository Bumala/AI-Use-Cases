import streamlit as st

# Set the page title
st.set_page_config(page_title="Letter A Box with Column")

# Display a title
st.title("Streamlit Web App")

# Display a container with the box and column
st.markdown(
    """
    <div style="display: flex; align-items: center; justify-content: center; margin-top: 50px;">
        <!-- Box with letter A -->
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
            margin-right: 20px;
        ">
            A
        </div>
        
        <!-- Column with two rows -->
        <div style="display: flex; flex-direction: column; justify-content: space-between; height: 200px;">
            <div style="
                display: flex;
                align-items: center;
                justify-content: center;
                height: 50%;
                width: 200px;
                border: 2px solid black;
                background-color: lightblue;
                font-size: 20px;
                font-weight: bold;
                color: black;
                margin-bottom: 10px;
            ">
                Row 1
            </div>
            <div style="
                display: flex;
                align-items: center;
                justify-content: center;
                height: 50%;
                width: 200px;
                border: 2px solid black;
                background-color: lightgreen;
                font-size: 20px;
                font-weight: bold;
                color: black;
            ">
                Row 2
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
