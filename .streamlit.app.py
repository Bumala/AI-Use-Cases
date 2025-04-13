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
    num_rows = len(df)
    html = f"<table style='border-spacing: 2px; width: 100%; border-collapse: collapse; border: 1px solid black; aspect-ratio: 1 / 1;'>"
    for i, row in df.iterrows():
        non_empty_cells = row.dropna().size
        html += "<tr>"
        for j, val in enumerate(row):
            if pd.notna(val):
                style = f"text-align: left; padding: 10px; border: 1px solid #ddd;"
                if non_empty_cells == 2:
                    if j == 0:
                        html += f"<td style='{style} width: 50%;' colspan='1'>{val}</td>"
                    elif j == 1:
                        html += f"<td style='{style} width: 50%;' colspan='{df.iloc[i].size - 1}'>{val}</td>"
                elif non_empty_cells > 2:
                    if j == 0:
                        html += f"<td rowspan='{df.iloc[i].isnull().sum() + 1 if i in [0, 5, 10] else 1}' style='{style}'>{val}</td>"
                    elif pd.notna(df.iloc[i, j-1]) or j == 1: # Ensure we don't add a new cell if the previous was merged
                        # Calculate dynamic width for columns from the third onwards
                        if j >= 1:
                            num_remaining_cols = non_empty_cells - (1 if i not in [0, 5, 10] else 1) # Adjust for the first merged column
                            if num_remaining_cols > 0:
                                width_percent = 100 / non_empty_cells
                                html += f"<td style='{style} width: {width_percent}%;'>{val}</td>"
                elif non_empty_cells == 1:
                    html += f"<td style='{style} width: 100%;' colspan='{df.iloc[i].size}'>{val}</td>"
        html += "</tr>"
    html += "</table>"
    return html

# Display the table in Streamlit
st.write(generate_html_table(df), unsafe_allow_html=True)
