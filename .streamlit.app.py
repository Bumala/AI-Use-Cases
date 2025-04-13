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

# Generate HTML table with flexible row lengths and square aspect ratio
def generate_html_table(df):
    num_rows = len(df)
    max_cols = df.apply(lambda row: row.notna().sum(), axis=1).max()

    # Define a base width for the first two columns (as a percentage)
    base_width_percent = 20
    remaining_width_percent = 100 - 2 * base_width_percent

    if max_cols > 2:
        dynamic_col_width_percent = remaining_width_percent / (max_cols - 2)
    else:
        dynamic_col_width_percent = 0

    html = f"<table style='border-spacing: 2px; width: 100%; border-collapse: collapse; border: 1px solid black; aspect-ratio: 1 / 1;'>"
    for i, row in df.iterrows():
        html += "<tr>"
        for j, val in enumerate(row):
            if pd.notna(val):
                style = f"text-align: left; padding: 10px; border: 1px solid #ddd;"
                if j == 0:
                    if i == 0:
                        html += f"<td rowspan='5' style='{style} width: {base_width_percent}%;'>{val}</td>"
                    elif i == 5:
                        html += f"<td rowspan='5' style='{style} width: {base_width_percent}%;'>{val}</td>"
                    elif i == 10:
                        html += f"<td rowspan='2' style='{style} width: {base_width_percent}%;'>{val}</td>"
                    elif i not in [0, 5, 10]:
                        continue
                elif j == 1:
                    html += f"<td style='{style} width: {base_width_percent}%;'>{val}</td>"
                elif j >= 2:
                    html += f"<td style='{style} width: {dynamic_col_width_percent}%;'>{val}</td>"
            elif j >= 2:
                html += "<td style='border: 1px solid #ddd;'></td>" # Add empty cells for alignment
        html += "</tr>"
    html += "</table>"
    return html

# Display the table in Streamlit
st.write(generate_html_table(df), unsafe_allow_html=True)
