import streamlit as st
import pandas as pd

# Data definition
data = [
    ["Impact (What)", "Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"],
    [None, "Focus within Business Model Navigator", "Customer Segments", "Value Proposition", "Value Chain", "Revenue Model"],
    [None, "Innovation Type", "Incremental", "Radical", "Sustaining", "Disruptive"],
    [None, "Aim", "Product Innovation", "Process Innovation", "Business Model Innovation"],
    [None, "Ambidexterity", "Exploration", "Exploitation"],
    ["Technology (How)", "AI Role", "Automaton", "Assistant", "Partner"],
    [None, "AI Concepts", "Machine Learning", "Deep Learning", "Artificial Neural Networks", "Natural Language Processing", "Computer Vision", "Robotics"],
    [None, "Analytics Focus", "Descriptive", "Diagnostic", "Predictive", "Prescriptive"],
    [None, "Analytics Problem", "Description/Summary", "Clustering", "Classification", "Dependency Analysis", "Regression"],
    [None, "Data Type", "Customer Data", "Machine Data", "Business Data (Internal Data)", "Market Data", "Public & Regulatory Data", "Synthetic Data"],
    ["Place (Where)", "Innovation Phase", "Front End", "Development", "Market Introduction"],
    [None, "R&D", "Manufacturing", "Marketing & Sales", "Customer Service"],
]

# Create the DataFrame
df = pd.DataFrame(data)

# Generate HTML boxes with flexible row lengths
def generate_html_boxes(df):
    # Start the container for boxes
    html = "<div style='display: flex; flex-wrap: wrap; gap: 10px;'>"

    # Generate boxes dynamically
    for i, row in df.iterrows():
        for j, val in enumerate(row):
            if pd.notna(val):  # Only add non-empty cells
                html += f"""
                <div style='
                    display: inline-block;
                    padding: 10px;
                    margin: 5px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    background-color: #f9f9f9;
                    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
                '>
                    {val}
                </div>
                """
    html += "</div>"
    return html

# Display the boxes in Streamlit
st.write(generate_html_boxes(df), unsafe_allow_html=True)
