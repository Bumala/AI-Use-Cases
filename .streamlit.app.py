import streamlit as st
import pandas as pd
from streamlit.components.v1 import html
import json

# Set Streamlit page layout
st.set_page_config(layout="wide")

# ---------- Data for the HTML table ----------
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

# ---------- Load analysis table ----------
analysis_table_data = {
    # ... (your existing analysis table data) ...
}
analysis_table = pd.DataFrame(analysis_table_data)
analysis_table.set_index("Use Case", inplace=True)

# ======= SESSION STATE =======
if "selected" not in st.session_state:
    st.session_state.selected = set()

if "attr_multiselect" not in st.session_state:
    st.session_state.attr_multiselect = []

# Initialize selected_attributes from session state
selected_attributes = list(st.session_state.selected)

# ---------- Selectable attribute list ----------
attribute_columns = list(analysis_table.columns)

# Create container for the display
with st.container():
    # Display-only multiselect to show selected attributes
    selected_display = st.multiselect(
        "Selected attributes (select in table below):",
        attribute_columns,
        default=st.session_state.attr_multiselect,
        disabled=True,  # Make it display-only
        key="attr_display"
    )
    
    # ---------- Calculate and show top use case ----------
    if selected_attributes:
        summed = analysis_table[selected_attributes].sum(axis=1)
        top_use_case = summed.idxmax()
        st.success(f"🚀 **Top Use Case:** {top_use_case}")
    else:
        st.info("👆 Select attributes in the table below to see the top use case.")

# ======= PERFECT TABLE LAYOUT GENERATION =======
def generate_html_table(data, selected):
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
            click_attr = f"onclick='handleCellClick(this, event)' data-attr='{val}'" if is_attribute else ""
            cell_class = " class='selected'" if val in selected and is_attribute else ""
           
            # Base cell style
            bg_color = "#92D050" if val in selected and is_attribute else "#f1fbfe"
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

# ======= JAVASCRIPT FOR INTERACTIVITY =======
interaction_js = f"""
<script>
// Track selected items globally
let selectedItems = new Set({json.dumps(list(st.session_state.selected))});

function updateStreamlit() {{
    // Convert to array for Streamlit
    const selections = Array.from(selectedItems);
    
    // Send selected items to Streamlit
    window.parent.postMessage({{
        isStreamlitMessage: true,
        type: 'updateSelections',
        data: selections
    }}, '*');
}}

function handleCellClick(element, event) {{
    const attr = element.getAttribute('data-attr');
    const isSelected = element.style.backgroundColor === 'rgb(146, 208, 80)';
    
    // Allow multiple selection with Ctrl/Cmd key
    if (!event.ctrlKey && !event.metaKey && !isSelected) {{
        // If not holding Ctrl/Cmd and selecting new item, clear others
        document.querySelectorAll('td[data-attr]').forEach(cell => {{
            cell.style.backgroundColor = cell.dataset.originalColor;
        }});
        selectedItems.clear();
    }}
    
    // Toggle selection
    if (!isSelected) {{
        element.style.backgroundColor = '#92D050';
        selectedItems.add(attr);
    }} else {{
        element.style.backgroundColor = element.dataset.originalColor;
        selectedItems.delete(attr);
    }}
    
    updateStreamlit();
}}

document.addEventListener("DOMContentLoaded", function() {{
    // Store original background color of each cell
    const cells = document.querySelectorAll('td[data-attr]');
    cells.forEach(cell => {{
        const original = getComputedStyle(cell).backgroundColor;
        cell.dataset.originalColor = original;
        
        // Initialize selected cells
        const attr = cell.getAttribute('data-attr');
        if (selectedItems.has(attr)) {{
            cell.style.backgroundColor = '#92D050';
        }}
    }});
    
    document.getElementById('resetButton').addEventListener('click', function() {{
        // Clear selections
        selectedItems.clear();
        
        // Restore each cell's original background color
        cells.forEach(cell => {{
            cell.style.backgroundColor = cell.dataset.originalColor;
        }});
        
        updateStreamlit();
    }});
}});
</script>
"""

# ======= HANDLE MESSAGES FROM JAVASCRIPT =======
def handle_js_messages():
    if hasattr(st.session_state, 'js_message') and st.session_state.js_message:
        message = st.session_state.js_message
        if message['type'] == 'updateSelections':
            # Update both the selected set and dropdown list
            new_selections = set(message['data'])
            if new_selections != st.session_state.selected:
                st.session_state.selected = new_selections
                st.session_state.attr_multiselect = message['data']
                st.experimental_rerun()  # Force update

# Initialize message handling
if 'js_message' not in st.session_state:
    st.session_state.js_message = None
handle_js_messages()

# ======= SELECTED BAR AND TABLE =======
selected_bar_html = """
<div id="resetButtonContainer" style="padding: 10px; background-color: #f1fbfe; text-align: center;">
    <button id="resetButton" style="padding: 10px 20px; background-color: #61cbf3; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">
        Reset Selection
    </button>
</div>
<div id="selectedBar" style="margin-bottom: 10px; padding: 10px; background-color: #dceefc; border: 2px solid #61cbf3; border-radius: 8px; font-weight: bold;">
    Selected Attributes: <span id="selectedItems">None</span>
</div>
"""

# Generate the full HTML
html_code = selected_bar_html + f"""
<div style="overflow-x: auto; width: 100%; padding: 10px; box-sizing: border-box;">
    <div class="zoomed-table">
        {generate_html_table(data, st.session_state.selected)}
    </div>
</div>
""" + interaction_js

# Add styling
html_code += """
<style>
.zoomed-table {
    transform: scale(0.75);
    transform-origin: top center;
    width: 100%;
}
td:hover {
    box-shadow: 0 0 5px rgba(0,0,0,0.3);
    transform: scale(1.02);
    transition: all 0.2s ease;
}
</style>
"""

# Display the HTML
html(html_code, height=1200)
