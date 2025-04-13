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

    # Calculate a rough cell width based on the number of columns to aim for a square
    # Adjust the base_width as needed to control the overall size
    base_width = 100  # Base width for the first two columns
    dynamic_width_percentage = (100 - 2 * (base_width / (base_width + (max_cols - 2) * (base_width / 2)))) if max_cols > 2 else 100
    if max_cols > 2:
        dynamic_cell_width_percentage = dynamic_width_percentage / (max_cols - 2)
    else:
        dynamic_cell_width_percentage = 0

    html = "<table style='border-spacing: 2px; width: 100%; border-collapse: collapse; border: 1px solid black; aspect-ratio: 1 / 1;'>"
    for i, row in df.iterrows():
        html += "<tr>"
        for j, val in enumerate(row):
            if pd.notna(val):
                style = f"text-align: left; padding: 10px; border: 1px solid #ddd;"
                if j == 0:
                    if i == 0:
                        html += f"<td rowspan='5' style='{style} width: {base_width / (base_width + (max_cols - 2) * (base_width / 2)) * 100}%;'>{val}</td>"
                    elif i == 5:
                        html += f"<td rowspan='5' style='{style} width: {base_width / (base_width + (max_cols - 2) * (base_width / 2)) * 100}%;'>{val}</td>"
                    elif i == 10:
                        html += f"<td rowspan='2' style='{style} width: {base_width / (base_width + (max_cols - 2) * (base_width / 2)) * 100}%;'>{val}</td>"
                    elif i not in [0, 5, 10]:
                        continue
                elif j == 1:
                    html += f"<td style='{style} width: {base_width / (base_width + (max_cols - 2) * (base_width / 2)) * 100}%;'>{val}</td>"
                elif j >= 2:
                    html += f"<td style='{style} width: {dynamic_cell_width_percentage}%;'>{val}</td>"
            elif j >= 2:
                html += "<td style='border: 1px solid #ddd;'></td>" # Add empty cells for alignment
        html += "</tr>"

    # Fill remaining cells in shorter rows for a more square look
    for i in range(len(df)):
        row_length = df.iloc[i].notna().sum()
        if row_length < max_cols:
            html += "<tr>"
            # Skip the first two columns as they are already present or merged
            for j in range(max_cols):
                if j < 2 and df.iloc[i, j] is None:
                    continue
                elif j >= 2 and (j >= row_length or pd.isna(df.iloc[i, j])):
                    html += "<td style='border: 1px solid #ddd;'></td>"
            html += "</tr>"
            # Remove the extra closing </tr> and opening <tr> from the next iteration
            # as we are manually adding cells within the current row

    html += "</table>"
    return html

# Display the table in Streamlit
st.write(generate_html_table(df), unsafe_allow_html=True)
