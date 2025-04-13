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

df = pd.DataFrame(data)

# Function to generate the HTML table
def generate_html_table(df):
    # Define consistent widths
    first_col_width = 160
    second_col_width = 220
    base_cell_width = 150
    cell_height = 50

    def style(width):
        return f"text-align: left; padding: 10px; border: 1px solid #ccc; width: {width}px; height: {cell_height}px;"

    # Define colspans
    colspan_2 = {
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
                    html += f"<td rowspan='5' style='{style(first_col_width)}'>{val}</td>"
                elif i == 5:
                    html += f"<td rowspan='5' style='{style(first_col_width)}'>{val}</td>"
                elif i == 10:
                    html += f"<td rowspan='2' style='{style(first_col_width)}'>{val}</td>"
                else:
                    continue
            elif j == 1:
                html += f"<td style='{style(second_col_width)}'>{val}</td>"
            elif (i, j) in colspan_3:
                html += f"<td colspan='3' style='{style(base_cell_width * 3)}'>{val}</td>"
            elif (i, j) in colspan_2:
                html += f"<td colspan='2' style='{style(base_cell_width * 2)}'>{val}</td>"
            else:
                html += f"<td style='{style(base_cell_width)}'>{val}</td>"
        html += "</tr>"

    html += "</table>"
    return html

# Apply CSS to center the table with zoom and a slight left margin for better alignment
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
            margin-left: 50px; /* Add left margin for better alignment */
        }
        table {
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Render the table in Streamlit within the centered container
st.markdown('<div class="center-table">' + generate_html_table(df) + '</div>', unsafe_allow_html=True)
