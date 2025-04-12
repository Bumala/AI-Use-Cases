import streamlit as st
import pandas as pd

# Define the data directly (example data)
data = [
    ["Impact (What)", "Column 2", "Column 3", "Column 4"],
    [None, "Row 2, Col 2", "Row 2, Col 3", "Row 2, Col 4"],
    [None, "Row 3, Col 2", "Row 3, Col 3", "Row 3, Col 4"],
    [None, "Row 4, Col 2", "Row 4, Col 3", "Row 4, Col 4"],
    [None, "Row 5, Col 2", "Row 5, Col 3", "Row 5, Col 4"],
    ["Technology (How)", "Row 6, Col 2", "Row 6, Col 3", "Row 6, Col 4"],
    [None, "Row 7, Col 2", "Row 7, Col 3", "Row 7, Col 4"],
    [None, "Row 8, Col 2", "Row 8, Col 3", "Row 8, Col 4"],
    [None, "Row 9, Col 2", "Row 9, Col 3", "Row 9, Col 4"],
    [None, "Row 10, Col 2", "Row 10, Col 3", "Row 10, Col 4"],
    ["Place (Where)", "Row 11, Col 2", "Row 11, Col 3", "Row 11, Col 4"],
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

# Generate styled HTML table with proper error handling
def generate_html_table(df, styles):
    html = "<table style='border-collapse: collapse; width: 100%;'>"
    for i, row in df.iterrows():
        html += "<tr>"
        for j, value in row.items():
            try:
                # Get the style for the current cell
                style = styles[i][j]
                
                # Safely extract font color
                font_color = f"color: #{style['font_color'][:6]};" if style.get('font_color') else "color: #000000;"  # Default to black
                
                # Handle other styles
                background_color = f"background-color: #{style['background_color'][:6]};" if style.get('background_color') else ""
                font_weight = "font-weight: bold;" if style.get("bold") else ""
                font_style = "font-style: italic;" if style.get("italic") else ""
                
                # Combine styles
                cell_style = f"{background_color} {font_color} {font_weight} {font_style} padding: 5px; border: 1px solid #ddd;"
                html += f"<td style='{cell_style}'>{value if value is not None else ''}</td>"
            except IndexError as e:
                # Log or handle the mismatch gracefully
                html += f"<td style='color: red;'>Error: {str(e)}</td>"
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
st.info("This morphological box is displayed with the predefined data and formatting.")
