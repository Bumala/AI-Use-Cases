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

# Generate HTML table without gridlines
def generate_html_table(df):
    # Start the table with fixed layout
    html = """
    <table style='border-spacing: 0; width: 100%; border-collapse: collapse; table-layout: fixed;'>
    """

    # Define cell dimensions
    cell_width = "150px"  # Universal width
    cell_height = "50px"  # Universal height

    # Generate rows dynamically
    for i, row in df.iterrows():
        html += "<tr>"
        for j, val in enumerate(row):
            if pd.notna(val):  # Only add non-empty cells
                if j == 0 and i == 0:  # Merge rows 1 to 5 in the first column
                    html += f"<td rowspan='5' style='text-align: left; padding: 10px; width: {cell_width}; height: {cell_height};'>{val}</td>"
                elif j == 0 and i == 5:  # Merge rows 6 to 10 in the first column
                    html += f"<td rowspan='5' style='text-align: left; padding: 10px; width: {cell_width}; height: {cell_height};'>{val}</td>"
                elif j == 0 and i == 10:  # Merge rows 11 and 12 in the first column
                    html += f"<td rowspan='2' style='text-align: left; padding: 10px; width: {cell_width}; height: {cell_height};'>{val}</td>"
                elif j == 0 and i < 5:  # Skip rows 2 to 5 in the first column
                    continue
                elif j == 0 and 5 < i < 10:  # Skip rows 7 to 10 in the first column
                    continue
                elif j == 0 and i == 11:  # Skip row 12 in the first column
                    continue

                # Define sets for cells with specific colspan requirements
                colspan_2_cells = {
                    (0, 2), (0, 3), (0, 4),
                    (1, 4), (1, 5),
                    (2, 4), (2, 5),
                    (3, 2), (3, 3), (3, 4),
                    (5, 2), (5, 3), (5, 4),
                    (7, 4), (7, 5),
                    (8, 6),
                    (10, 2), (10, 3), (10, 4),
                    (11, 2), (11, 3), (11, 4)
                }

                colspan_3_cells = {
                    (4, 2), (4, 3)
                }

                # Iterate and build the table
                if (i, j) in colspan_2_cells:
                    html += f"<td colspan='2' style='text-align: left; padding: 10px; width: {cell_width}; height: {cell_height};'>{val}</td>"
                elif (i, j) in colspan_3_cells:
                    html += f"<td colspan='3' style='text-align: left; padding: 10px; width: {cell_width}; height: {cell_height};'>{val}</td>"
                else:  # Regular cells
                    html += f"<td style='text-align: left; padding: 10px; width: {cell_width}; height: {cell_height};'>{val}</td>"
        html += "</tr>"

    html += "</table>"
    return html
