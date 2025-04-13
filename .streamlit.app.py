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

# Generate HTML table with flexible row lengths and adjusted column widths
def generate_html_table(df):
    html = f"<table style='border-spacing: 2px; width: 100%; border-collapse: collapse; border: 1px solid black; aspect-ratio: 1 / 1;'>"
    for i, row in df.iterrows():
        non_empty_cells = row.dropna().size
        html += "<tr>"
        for j, val in enumerate(row):
            if pd.notna(val):
                style = f"text-align: left; padding: 10px; border: 1px solid #ddd;"
                if j == 0:
                    rowspan = df.iloc[i:].apply(lambda r: r.iloc[0] is None).take_while(lambda x: x).size + 1 if i in [0, 5, 10] else 1
                    html += f"<td rowspan='{rowspan}' style='{style}'>{val}</td>"
                elif pd.notna(df.iloc[i, j-1]) or j == 1:
                    width_percent = f'{100 / (non_empty_cells - (1 if i not in [0, 5, 10] and j > 0 else 0)) if non_empty_cells > 1 else 100}%'
                    colspan = 1
                    if non_empty_cells == 2:
                        colspan = df.iloc[i].notna().sum() -1 if j == 1 else 1

                    html += f"<td style='{style} width: {width_percent};' colspan='{colspan}'>{val}</td>"
            elif non_empty_cells > 0 and j > 0 and pd.isna(df.iloc[i, j-1]):
                pass # Don't add empty cells if the previous was a value in a shorter row
        html += "</tr>"
    html += "</table>"
    return html

# Display the table in Streamlit
st.write(generate_html_table(df), unsafe_allow_html=True)
