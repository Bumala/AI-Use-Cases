import streamlit as st
import pandas as pd

# Set the page layout to "wide"
st.set_page_config(layout="wide")

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
    [None, "Analytics Problem", "Description/ Summary", "Clustering", "Classification", "Dependency Analysis", "Regression"],
    [None, "Data Type", "Customer Data", "Machine Data", "Business Data (Internal Data)", "Market Data", "Public & Regulatory Data", "Synthetic Data"],
    ["Place (Where)", "Innovation Phase", "Front End", "Development", "Market Introduction"],
    [None, "Department", "R&D", "Manufacturing", "Marketing & Sales", "Customer Service"],
]

df = pd.DataFrame(data)

# Function to generate the HTML table
def generate_html_table(df):
    # Define consistent widths
    first_col_width = 160
    second_col_width = 220
    base_cell_width = 150
    cell_height = 50

    def style(width, bold=False):
        bold_style = "font-weight: bold;" if bold else ""
        return f"text-align: center; vertical-align: middle; padding: 10px; border: 1px solid #ccc; width: {width}px; height: {cell_height}px; {bold_style}"

    # Define colspans
    colspan_2 = {
        (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 5),
        (2, 2), (2, 5),
        (3, 2), (3, 3), (3, 4),
        (5, 2), (5, 3), (5, 4),
        (7, 2), (7, 5),
        (8, 4),
        (10, 2), (10, 3), (10, 4),
        (11, 2), (11, 5), 
    }

    colspan_3 = {
        (4, 2), (4, 3)
    }

    html = "<table style='border-spacing: 0; width: 100%; border-collapse: collapse; table-layout: fixed;'>"

    for i, row in df.iterrows():
        html += "<tr>"
        for j, val in enumerate(row):
            if pd.isna(val):
                continue

            if j == 0:
                if i == 0:
                    html += f"<td rowspan='5' style='{style(first_col_width, bold=True)} background-color: #F1FBFE;'>{val}</td>"
                elif i == 5:
                    html += f"<td rowspan='5' style='{style(first_col_width, bold=True)} background-color: #b0c4de;'>{val}</td>"
                elif i == 10:
                    html += f"<td rowspan='2' style='{style(first_col_width, bold=True)} background-color: #b0c4de;'>{val}</td>"
                else:
                    continue
            elif j == 1:
                html += f"<td style='{style(second_col_width, bold=True)}'>{val}</td>"
            elif (i, j) in colspan_3:
                html += f"<td colspan='3' style='{style(base_cell_width * 3)}'>{val}</td>"
            elif (i, j) in colspan_2:
                html += f"<td colspan='2' style='{style(base_cell_width * 2)}'>{val}</td>"
            else:
                html += f"<td style='{style(base_cell_width)}'>{val}</td>"
        html += "</tr>"

    html += "</table>"
    return html

# Apply CSS to center the table with zoom and ensure proper alignment
st.markdown("""
    <style>
        .center-table {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 100%;
            margin: 0 auto;
            transform: scale(0.9); /* Zoom out slightly to fit the table on the screen */
            transform-origin: top center;
        }
        table {
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Render the table in Streamlit within the centered container
st.markdown('<div class="center-table">' + generate_html_table(df) + '</div>', unsafe_allow_html=True)
