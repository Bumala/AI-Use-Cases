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

# Inject CSS
st.markdown("""
<style>
.morph-box {
    display: flex;
    flex-direction: column;
    border: 2px solid black;
    border-radius: 6px;
    overflow: hidden;
    font-family: sans-serif;
}
.morph-row {
    display: grid;
    grid-template-columns: 180px 220px auto;
    border-top: 1px solid #ccc;
    min-height: 50px;
}
.morph-label {
    background: #e6f0ff;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px;
    border-right: 1px solid #ccc;
    border-bottom: 1px solid #ccc;
}
.morph-cell-second {
    background: #f2f2f2;
    padding: 10px;
    border-right: 1px solid #ccc;
    border-bottom: 1px solid #ccc;
    display: flex;
    align-items: center;
}
.morph-flexcells {
    display: flex;
    flex-grow: 1;
    border-bottom: 1px solid #ccc;
}
.morph-flexcell {
    flex: 1;
    padding: 10px;
    border-right: 1px solid #eee;
    display: flex;
    align-items: center;
    background: #f9f9f9;
}
</style>
""", unsafe_allow_html=True)

# Generate the layout
def render_box(df):
    html = "<div class='morph-box'>"

    # First column merge map
    label_map = {
        0: ("Impact (What)", 5),
        5: ("Technology (How)", 5),
        10: ("Place (Where)", 2),
    }

    rowspan_tracker = {}  # to track which row to print label

    for i, row in df.iterrows():
        html += "<div class='morph-row'>"

        # First column: merged labels
        if i in label_map:
            label, span = label_map[i]
            rowspan_tracker[i] = span
            html += f"<div class='morph-label' style='grid-row: span {span};'>{label}</div>"
        elif any(i >= k and i < k + v for k, v in label_map.items()):
            pass  # skip cell, since it's merged
        else:
            html += "<div></div>"  # fallback

        # Second column (always present)
        second_col = row[1] if pd.notna(row[1]) else ""
        html += f"<div class='morph-cell-second'>{second_col}</div>"

        # Third column onwards — flexible
        flex_cells = [c for c in row[2:] if pd.notna(c)]
        html += "<div class='morph-flexcells'>"
        for cell in flex_cells:
            html += f"<div class='morph-flexcell'>{cell}</div>"
        html += "</div>"

        html += "</div>"  # end of row

    html += "</div>"
    return html

# Render it
st.markdown("### Final Morphological Box", unsafe_allow_html=True)
st.markdown(render_box(df), unsafe_allow_html=True)
