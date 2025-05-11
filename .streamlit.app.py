import streamlit as st
import pandas as pd
from streamlit.components.v1 import html
from st_aggrid import AgGrid, GridOptionsBuilder

# Set page layout
st.set_page_config(layout="wide")

# ======= TABLE DATA =======
data = [
   ["Category", "Dimension", "Attributes"],
   ["Impact (What)", "Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"],
   [None, "Focus within Business Model Navigator", "Customer Segments", "Value Proposition", "Value Chain", "Revenue Model"],
   [None, "Aim", "Product Innovation", "Process Innovation", "Business Model Innovation"],
   [None, "Ambidexterity", "Exploration", "Exploitation"],
   ["Technology (How)", "AI Role", "Automaton", "Helper", "Partner"],
   [None, "AI Concepts", "Machine Learning", "Deep Learning", "Artificial Neural Networks", "Natural Language Processing", "Computer Vision", "Robotics"],
   [None, "Analytics Focus", "Descriptive", "Diagnostic", "Predictive", "Prescriptive"],
   [None, "Analytics Problem", "Description/ Summary", "Clustering", "Classification", "Dependency Analysis", "Regression"],
   [None, "Data Type", "Customer Data", "Machine Data", "Business Data (Internal Data)", "Market Data", "Public & Regulatory Data", "Synthetic Data"],
   ["Context (Where/When)", "Innovation Phase", "Front End", "Development", "Market Introduction"],
   [None, "Department", "R&D", "Manufacturing", "Marketing & Sales", "Customer Service"],
]

# ======= SESSION STATE =======
if "selected" not in st.session_state:
   st.session_state.selected = set()

# ======= AG-GRID TABLE CONFIGURATION =======
# Convert the table data into a DataFrame
df = pd.DataFrame(data)

# Build grid options for AgGrid
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(editable=False, resizable=True)
gb.configure_selection("single", use_checkbox=False)  # Enable single cell selection
gb.configure_grid_options(domLayout='normal')  # Normal layout for the grid
grid_options = gb.build()

# Render the AgGrid table
st.markdown("### Interactive Table (AgGrid)")
grid_response = AgGrid(
    df,
    gridOptions=grid_options,
    theme="streamlit",  # Streamlit theme for AgGrid
    height=400,
    width="100%",
    allow_unsafe_jscode=True,  # Allow custom JS code
)

# ======= HANDLE SELECTED CELL =======
selected_cell = grid_response["selected_rows"]  # Capture the selected cell

# Display the selected cell's details
st.markdown("### Selected Cell Information")
if selected_cell:
    # Extract the row index and selected cell data
    selected_row = selected_cell[0].get("_index", "N/A")
    selected_values = selected_cell[0]
    st.write(f"Row: {selected_row}, Selected Data: {selected_values}")
else:
    st.info("No cell selected yet.")

# ======= PERFECT TABLE LAYOUT GENERATION (CUSTOM HTML) =======
def generate_html_table(data, selected):
    # Custom HTML table generation logic from your original script
    first_col_width = 160
    second_col_width = 200
    base_cell_width = 150
    cell_height = 50

    def style(width, bold=False, border_bottom=False):
        bold_style = "font-weight: bold;" if bold else ""
        border_bottom_style = "border-bottom: 3px solid #000000;" if border_bottom else ""
        return f"text-align: center; vertical-align: middle; padding: 10px; border: 1px solid #000000; width: {width}px; height: {cell_height}px; {bold_style} {border_bottom_style}"

    # Define colspan rules
    colspan_2 = {
        (1, 2), (1, 3), (1, 4),
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

    html = "<table style='border-spacing: 0; width: 100%; border-collapse: collapse; table-layout: fixed; border: 3px solid #000000;'>"

    for i, row in enumerate(data):
        html += "<tr>"
        for j, val in enumerate(row):
            if val is None:
                continue

            # Determine if this is an attribute cell that can be selected
            is_attribute = (i > 0 and j >= 2)
            click_attr = f"onclick='handleCellClick(this)' data-attr='{val}'" if is_attribute else ""
            cell_class = " class='selected'" if val in st.session_state.selected and is_attribute else ""

            # Base cell style
            bg_color = "#92D050" if val in st.session_state.selected and is_attribute else "#f1fbfe"
            if j == 0:
                bg_color = "#61cbf3"
            elif j == 1:
                bg_color = "#94dcf8"

            # Header row
            if i == 0:
                if j == 0:
                    html += f"<td style='{style(first_col_width, bold=True, border_bottom=True)} background-color: #E8E8E8;'>{val}</td>"
                elif j == 1:
                    html += f"<td style='{style(second_col_width, bold=True, border_bottom=True)} background-color: #E8E8E8;'>{val}</td>"
                elif j == 2:
                    html += f"<td colspan='6' style='{style(base_cell_width * 6, bold=True, border_bottom=True)} background-color: #E8E8E8;'>{val}</td>"

            # First column cells with rowspan
            elif j == 0:
                if i == 1:
                    html += f"<td rowspan='4' style='{style(first_col_width, bold=True, border_bottom=True)} background-color: #61cbf3;'>{val}</td>"
                elif i == 5:
                    html += f"<td rowspan='5' style='{style(first_col_width, bold=True, border_bottom=True)} background-color: #61cbf3;'>{val}</td>"
                elif i == 10:
                    html += f"<td rowspan='2' style='{style(first_col_width, bold=True)} background-color: #61cbf3;'>{val}</td>"

            # Special formatting for certain cells
            elif (i == 4 and j == 1) or (i == 9 and j == 1):
                html += f"<td {click_attr}{cell_class} style='{style(base_cell_width, bold=True, border_bottom=True)} background-color: {bg_color}; cursor: pointer;'>{val}</td>"
            elif i == 9 and j in {2, 4, 6}:
                html += f"<td {click_attr}{cell_class} style='{style(base_cell_width)} background-color: {bg_color}; border-bottom: 3px solid #000000; cursor: pointer;'>{val}</td>"
            elif i > 0 and j == 1:
                html += f"<td style='{style(second_col_width, bold=True)} background-color: #94dcf8;'>{val}</td>"

            # Cells with colspan
            elif (i, j) in colspan_3:
                html += f"<td {click_attr}{cell_class} colspan='3' style='{style(base_cell_width * 3)} background-color: {bg_color}; border-bottom: 3px solid #000000; cursor: pointer;'>{val}</td>"
            elif (i, j) in colspan_2:
                html += f"<td {click_attr}{cell_class} colspan='2' style='{style(base_cell_width * 2)} background-color: {bg_color}; cursor: pointer;'>{val}</td>"
            else:
                html += f"<td {click_attr}{cell_class} style='{style(base_cell_width)} background-color: {bg_color}; cursor: pointer;'>{val}</td>"
        html += "</tr>"

    html += "</table>"
    return html

# Render custom HTML table
html_content = generate_html_table(data, st.session_state.selected)
html(f"<div>{html_content}</div>", height=400)
