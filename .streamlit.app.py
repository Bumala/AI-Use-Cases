import streamlit as st
import pandas as pd
from openpyxl import load_workbook

# Load the Excel file
uploaded_file = "Use Cases.xlsx"

# Load workbook using openpyxl
wb = load_workbook(uploaded_file, data_only=True)
sheet = wb.worksheets[1]  # Load the second sheet (0-based index)

# Extract the data and formatting
data = []
styles = []

# Iterate through rows and columns to extract values and styles
for row in sheet.iter_rows():
    row_data = []
    row_styles = []
    for cell in row:
        row_data.append(cell.value)
        cell_style = {
            "background_color": cell.fill.fgColor.rgb if cell.fill.fgColor.type == "rgb" else None,
            "font_color": cell.font.color.rgb if cell.font.color and cell.font.color.type == "rgb" else "#000000",
            "bold": cell.font.bold,
            "italic": cell.font.italic,
        }
        row_styles.append(cell_style)
    data.append(row_data)
    styles.append(row_styles)

# Remove the first 3 rows and last 7 rows
data = data[3:-7]
styles = styles[3:-7]

# Distribute content in the first row starting from the third column
first_row = data[0]  # Get the first row
first_row_styles = styles[0]  # Get the corresponding styles for the first row

# Extract non-empty content and styles starting from the third column
non_empty_content = [value for value in first_row[2:] if value is not None]
non_empty_styles = [style for value, style in zip(first_row[2:], first_row_styles[2:]) if value is not None]

# Update the first row with the non-empty content
data[0] = first_row[:2] + non_empty_content  # Keep columns 1 and 2, then add non-empty content
styles[0] = first_row_styles[:2] + non_empty_styles  # Update corresponding styles

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Generate styled HTML table
def generate_html_table(df, styles):
    html = "<table style='border-collapse: collapse; width: 100%;'>"
    for i, row in df.iterrows():
        html += "<tr>"
        for j, value in row.items():
            style = styles[i][j]
            background_color = f"background-color: #{style['background_color'][:6]};" if style['background_color'] else ""
            font_color = f"color: #{style['font_color'][:6]};" if style['font_color'] else ""
            font_weight = "font-weight: bold;" if style["bold"] else ""
            font_style = "font-style: italic;" if style["italic"] else ""
            cell_style = f"{background_color} {font_color} {font_weight} {font_style} padding: 5px; border: 1px solid #ddd;"
            html += f"<td style='{cell_style}'>{value if value is not None else ''}</td>"
        html += "</tr>"
    html += "</table>"
    return html

# Streamlit app
st.set_page_config(layout="wide", page_title="Morphological Box Viewer")
st.title("Morphological Box Viewer")

# Display the styled morphological box
st.markdown("### Morphological Box")
html_table = generate_html_table(df, styles)
st.markdown(html_table, unsafe_allow_html=True)

st.markdown("---")
st.info("This morphological box is displayed with the formatting extracted from the Excel file.")
