import streamlit as st
import pandas as pd

# Define the data directly (with content and merged cells)
data = [
    ["Impact (What)", "Column 2", "Column 3", "Column 4"],  # Merged rows 1-5 for "Impact (What)"
    [None, "Row 2, Col 2", "Row 2, Col 3", "Row 2, Col 4"],
    [None, "Row 3, Col 2", "Row 3, Col 3", "Row 3, Col 4"],
    [None, "Row 4, Col 2", "Row 4, Col 3", "Row 4, Col 4"],
    [None, "Row 5, Col 2", "Row 5, Col 3", "Row 5, Col 4"],
    ["Technology (How)", "Row 6, Col 2", "Row 6, Col 3", "Row 6, Col 4"],  # Merged rows 6-10 for "Technology (How)"
    [None, "Row 7, Col 2", "Row 7, Col 3", "Row 7, Col 4"],
    [None, "Row 8, Col 2", "Row 8, Col 3", "Row 8, Col 4"],
    [None, "Row 9, Col 2", "Row 9, Col 3", "Row 9, Col 4"],
    [None, "Row 10, Col 2", "Row 10, Col 3", "Row 10, Col 4"],
    ["Place (Where)", "Row 11, Col 2", "Row 11, Col 3", "Row 11, Col 4"],  # Merged rows 11-12 for "Place (Where)"
    [None, "Row 12, Col 2", "Row 12, Col 3", "Row 12, Col 4"],
]

# Define the styles directly
styles = [
    [{"background_color": None, "font_color": "#000000", "bold": True, "italic": False}] * 4,
    [{"background_color": None, "font_color": "#000000", "bold": False, "italic": False}] * 4,
    [{"background_color": None, "font_color": "#000000", "bold": False, "italic": False}] * 4,
    [{"background_color": None, "font_color": "#000000", "bold": False, "italic": False}] * 4,
    [{"background_color": None, "font_color": "#000000", "bold": False, "italic": False}] * 4,
    [{"background_color": None, "font_color": "#000000", "bold": True, "italic": False}] * 4,
    [{"background_color": None, "font_color": "#000000", "bold": False, "italic": False}] * 4,
    [{"background_color": None, "font_color": "#000000", "bold": False, "italic": False}] * 4,
    [{"background_color": None, "font_color": "#000000", "bold": False, "italic": False}] * 4,
    [{"background_color": None, "font_color": "#000000", "bold": False, "italic": False}] * 4,
    [{"background_color": None, "font_color": "#000000", "bold": True, "italic": False}] * 4,
    [{"background_color": None, "font_color": "#000000", "bold": False, "italic": False}] * 4,
]

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Generate styled HTML table with rowspan for merged cells
def generate_html_table_with_rowspans(df, styles):
    html = "<table style='border-collapse: collapse; width: 100%;'>"
    for i, row in df.iterrows():
        html += "<tr>"
        for j, value in row.items():
            if j == 0:  # First column
                # Merge rows 1-5 for "Impact (What)"
                if i == 0:
                    style = styles[i][j]
                    background_color = f"background-color: #{style['background_color'][:6]};" if style.get('background_color') else ""
                    font_color = f"color: #{style['font_color'][:6]};" if style.get('font_color') else "color: #000000;"
                    font_weight = "font-weight: bold;" if style.get("bold") else ""
                    font_style = "font-style: italic;" if style.get("italic") else ""
                    cell_style = f"{background_color} {font_color} {font_weight} {font_style} padding: 5px; border: 1px solid #ddd;"
                    html += f"<td rowspan='5' style='{cell_style}'>Impact (What)</td>"
                elif i < 5:
                    continue  # Skip rows 2 to 5

                # Merge rows 6-10 for "Technology (How)"
                elif i == 5:
                    style = styles[i][j]
                    background_color = f"background-color: #{style['background_color'][:6]};" if style.get('background_color') else ""
                    font_color = f"color: #{style['font_color'][:6]};" if style.get('font_color') else "color: #000000;"
                    font_weight = "font-weight: bold;" if style.get("bold") else ""
                    font_style = "font-style: italic;" if style.get("italic") else ""
                    cell_style = f"{background_color} {font_color} {font_weight} {font_style} padding: 5px; border: 1px solid #ddd;"
                    html += f"<td rowspan='5' style='{cell_style}'>Technology (How)</td>"
                elif 5 < i < 10:
                    continue  # Skip rows 7 to 10

                # Merge rows 11-12 for "Place (Where)"
                elif i == 10:  # Second to last row
                    style = styles[i][j]
                    background_color = f"background-color: #{style['background_color'][:6]};" if style.get('background_color') else ""
                    font_color = f"color: #{style['font_color'][:6]};" if style.get('font_color') else "color: #000000;"
                    font_weight = "font-weight: bold;" if style.get("bold") else ""
                    font_style = "font-style: italic;" if style.get("italic") else ""
                    cell_style = f"{background_color} {font_color} {font_weight} {font_style} padding: 5px; border: 1px solid #ddd;"
                    html += f"<td rowspan='2' style='{cell_style}'>Place (Where)</td>"
                elif i == 11:  # Last row
                    continue  # Skip the last row in the first column

                # Render remaining cells in the first column
                else:
                    style = styles[i][j]
                    background_color = f"background-color: #{style['background_color'][:6]};" if style.get('background_color') else ""
                    font_color = f"color: #{style['font_color'][:6]};" if style.get('font_color') else "color: #000000;"
                    font_weight = "font-weight: bold;" if style.get("bold") else ""
                    font_style = "font-style: italic;" if style.get("italic") else ""
                    cell_style = f"{background_color} {font_color} {font_weight} {font_style} padding: 5px; border: 1px solid #ddd;"
                    html += f"<td style='{cell_style}'>{value if value is not None else ''}</td>"
            else:  # Other columns
                style = styles[i][j]
                background_color = f"background-color: #{style['background_color'][:6]};" if style.get('background_color') else ""
                font_color = f"color: #{style['font_color'][:6]};" if style.get('font_color') else "color: #000000;"
                font_weight = "font-weight: bold;" if style.get("bold") else ""
                font_style = "font-style: italic;" if style.get("italic") else ""
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
html_table = generate_html_table_with_rowspans(df, styles)
st.markdown(html_table, unsafe_allow_html=True)

st.markdown("---")
st.info("This morphological box is displayed with the predefined data and formatting.")
