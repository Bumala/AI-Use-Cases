import streamlit as st
import pandas as pd

# Morphological Box Data
data = [
    ["Impact (What)", "Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"],
    [None, "Focus within Business Model Navigator", "Customer Segments", "Value Proposition", "Value Chain", "Revenue Model"],
    [None, "Innovation Type", "Incremental", "Radical", "Sustaining", "Disruptive"],
    [None, "Aim", "Product Innovation", "Process Innovation", "Business Model Innovation"],
    [None, "Ambidexterity", "Exploration", "Exploitation"],
    ["Technology (How)", "AI Role", "Automaton", "Assistant", "Partner"],
    [None, "AI Concepts", "Machine Learning", "Deep Learning", "Artificial Neural Networks", "Natural Language Processing", "Computer Vision", "Robotics"],
    [None, "Analytics Focus", "Descriptive", "Diagnostic", "Predictive", "Prescriptive" ],
    [None,"Analytics Problem", "Description/Summary", "Clustering", "Classification", "Dependency Analysis", "Regression"],
    [None,"Data Type", "Customer Data", "Machine Data", "Business Data (Internal Data)", "Market Data", "Public & Regulatory Data", "Synthetic Data"],
    ["Place (Where)", "Innovation Phase", "Front End", "Development", "Market Introduction"],
    [None, "R&D", "Manufacturing", "Marketing & Sales", "Customer Service"],
]

df = pd.DataFrame(data)

# Add CSS for grid-based styling
st.markdown("""
    <style>
    .box-container {
        display: flex;
        flex-direction: column;
        border: 2px solid #000;
        border-radius: 6px;
        overflow: hidden;
        font-family: sans-serif;
    }
    .box-row {
        display: grid;
        grid-auto-columns: 1fr;
        border-top: 1px solid #ccc;
        min-height: 50px;
    }
    .box-label {
        background: #e6f0ff;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 10px;
        border-right: 1px solid #ccc;
        min-width: 160px;
    }
    .box-cell {
        background: #f9f9f9;
        padding: 10px;
        border-right: 1px solid #eee;
        display: flex;
        align-items: center;
    }
    .box-row:last-child {
        border-bottom: none;
    }
    </style>
""", unsafe_allow_html=True)

# Function to generate grid rows with dynamic column count
def generate_morphological_box(df):
    html = "<div class='box-container'>"

    label_map = {
        0: ("Impact (What)", 5),
        5: ("Technology (How)", 5),
        10: ("Place (Where)", 2),
    }

    for i, row in df.iterrows():
        if i in label_map:
            label, rowspan = label_map[i]
            label_html = f"<div class='box-label' style='grid-row: span {rowspan};'>{label}</div>"
        elif row[0] is None:
            label_html = ""
        else:
            label_html = f"<div class='box-label'>{row[0]}</div>"

        cells = [str(cell) for cell in row[1:] if pd.notna(cell)]
        num_cells = len(cells)
        grid_template = f"grid-template-columns: {('1fr ' * (num_cells + (1 if label_html else 0))).strip()};"

        html += f"<div class='box-row' style='{grid_template}'>"
        if label_html:
            html += label_html
        for cell in cells:
            html += f"<div class='box-cell'>{cell}</div>"
        html += "</div>"

    html += "</div>"
    return html

# Show in Streamlit
st.markdown("### Adaptive Morphological Box", unsafe_allow_html=True)
st.markdown(generate_morphological_box(df), unsafe_allow_html=True)
