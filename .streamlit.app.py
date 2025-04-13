import streamlit as st
import pandas as pd

# Data
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

df = pd.DataFrame(data)

# CSS styling to simulate morphological box using flex
st.markdown("""
    <style>
    .morph-box { border: 1px solid black; border-collapse: collapse; width: 100%; }
    .morph-row { display: flex; border-bottom: 1px solid #ddd; }
    .morph-cell {
        padding: 10px;
        border-right: 1px solid #ddd;
        flex: 1;
        text-align: left;
        font-size: 14px;
        background-color: #f9f9f9;
    }
    .morph-label {
        background-color: #e6f0ff;
        font-weight: bold;
        min-width: 150px;
        text-align: center;
        flex: 0 0 150px;
    }
    </style>
""", unsafe_allow_html=True)

# Render morphological box
def render_morphological_box(df):
    html = "<div class='morph-box'>"

    for i, row in df.iterrows():
        cells = row.dropna().tolist()

        # Skip continuation rows for merged vertical labels
        if i in [1, 2, 3, 4, 6, 7, 8, 9, 11]:
            continue

        html += "<div class='morph-row'>"

        # Left label (merged vertically)
        if i == 0:
            html += f"<div class='morph-label' style='height: 200px;'>Impact (What)</div>"
        elif i == 5:
            html += f"<div class='morph-label' style='height: 200px;'>Technology (How)</div>"
        elif i == 10:
            html += f"<div class='morph-label' style='height: 100px;'>Place (Where)</div>"

        # Content cells (equally spaced)
        for val in cells[1:]:
            html += f"<div class='morph-cell'>{val}</div>"

        html += "</div>"

    html += "</div>"
    return html

# Display the result
st.markdown("### Morphological Box", unsafe_allow_html=True)
st.markdown(render_morphological_box(df), unsafe_allow_html=True)
