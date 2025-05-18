import streamlit as st
import pandas as pd
from streamlit.components.v1 import html
import json
import plotly.graph_objects as go
import streamlit.components.v1 as components
 
 
#------------------------------------------------------------------------------------------------------ Streamlit page layout -------------------------------------------------------------------------------------------------------------------
# Set Streamlit page layout
st.set_page_config(layout="wide")
 
 
#-------------------------------------------------------------------------------------------- Table for category, dimension and attributes -----------------------------------------------------------------------------------------------------
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
 
 
#---------------------------------------------------------------------------------------------------------- Analysis table ----------------------------------------------------------------------------------------------------------------------
analysis_table_data = {
            "Use Case": [
    "AI-infused experiments in R&D",
    "AI-powered manufacturing planning in smart factories",
    "AI-driven Human-Machine Collaboration in ideation",
    "AI-enabled idea generation in the Metaverse",
    "AI-optimized patent analysis",
    "AI-powered forecasting of the technology life cycle of EVs (S-Curve)",
    "AI-enabled bionic digital twin production planning",
    "AI-infused Human-Robot Collaboration planning",
    "AI-powered material flow planning",
    "AI-assisted ideation",
    "AI-driven interactive collaborative innovation",
    "AI-based digital twin for lithium-ion battery development",
    "AI- and Genetic Algorithms-based vehicle design",
    "AI-augmented visual inspections",
    "AI-optimized scenario engineering",
    "AI-driven design process",
    "AI- and Bio-inspired Design",
    "AI-assisted quality control of the bumper warpage",
    "AI-enabled predictive maintenance",
    "AI-optimized braking system test",
    "AI-based identification of consumer adoption stage",
    "AI-powered marketing campaign",
    "AI-driven relationship marketing",
    "AI-assisted customer service in after-sales",
    "AI-enabled battery monitoring",
    "AI-assisted staff training",
    "AI-driven predictive quality models for customer defects",
    "AI-powered customer satisfaction analysis",
    "AI-driven competition analysis",
    "AI-driven vehicles sales prediction"
],
 
"Quality/Scope/Knowledge": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
"Time Efficiency": [2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 2, 0, 2, 2, 2, 0, 0],
"Cost": [2, 2, 0, 0, 0, 0, 2, 1, 2, 2, 0, 2, 2, 0, 2, 0, 2, 0, 2, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0],
 
"Customer Segments": [0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2],
"Value Proposition": [2, 0, 0, 2, 0, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 0, 2, 2, 2, 0, 0, 2, 2, 2],
"Value Chain": [2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0],
"Revenue Model": [0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 2],
 
"Product Innovation": [2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 1, 0, 0, 2, 0, 0, 2],
"Process Innovation": [1, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2],
"Business Model Innovation": [0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 2, 0, 2],
 
"Exploration": [2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2],
"Exploitation": [0, 2, 0, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2, 2, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 0, 0, 0, 2, 2],
 
"Automaton": [2, 0, 2, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2],
"Helper": [1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0, 1, 0, 0, 0, 0, 0, 2, 0],
"Partner": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
 
"Machine Learning": [2, 2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2],
"Deep Learning": [2, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
"Artificial Neural Networks": [0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 0, 2],
"Natural Language Processing": [2, 0, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
"Computer Vision": [0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
"Robotics": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 
"Descriptive": [1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 0],
"Diagnostic": [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0],
"Predictive": [2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0, 0],
"Prescriptive": [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0],
 
"Description/ Summary": [1, 0, 0, 0, 2, 2, 0, 0, 1, 2, 0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0],
"Clustering": [0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 2, 0, 2, 2, 2, 2],
"Classification": [2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2],
"Dependency Analysis": [0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 2, 0, 0, 2, 0, 0, 1, 0, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2],
"Regression": [1, 1, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2],
 
"Customer Data": [2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1],
"Machine Data": [0, 1, 2, 2, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 1],
"Business Data (Internal Data)": [2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 2, 2, 0, 0, 2, 2, 2],
"Market Data": [2, 2, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2],
"Public & Regulatory Data": [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 2, 0, 0],
"Synthetic Data": [2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 2, 2, 0, 2, 2, 2, 2],
 
"Front End": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 1, 2, 2, 2, 2, 2],
"Development": [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 0, 0, 1, 1, 1, 2, 2, 1, 0, 1],
"Market Introduction": [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 1],
 
"R&D": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
"Manufacturing": [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0, 0, 1, 0, 1, 0, 2, 2, 0, 1],
"Marketing & Sales": [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1],
"Customer Service": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2]
}
 
 
analysis_table = pd.DataFrame(analysis_table_data)
analysis_table.set_index("Use Case", inplace=True)
 
 
 
 
 
# ------------------------------------------------------------------------------------------------------- Session state ------------------------------------------------------------------------------------------------------------------------
if "selected" not in st.session_state:
 st.session_state.selected = set()
 
if "attr_multiselect" not in st.session_state:
 st.session_state.attr_multiselect = []
 
# Initialize selected_attributes from session state
selected_attributes = list(st.session_state.selected)
 
 
 
 
 
 
#---------------------------------------------------------------------------------------------------------- First drop down list for selectable attributes -------------------------------------------------------------------------------------
attribute_columns = list(analysis_table.columns)
 
 
# Create container for the multiselect
multiselect_container = st.container()
 
 
 
# Display the first drop down list with current selections
with multiselect_container:
   # Add a styled sentence above the dropdown
   st.markdown(
       """
       <p style="font-size:18px; font-weight:bold; color:black;margin-bottom: 0px;">
           Select as many attributes as you like from the dropdown list below to identify relevant AI use cases and clusters in automotive. The more attributes you choose, the more accurately the most relevant AI use case will be displayed. If you select fewer than three attributes, please refer to the section with additional relevant use cases further down this page.
       </p>
       """,
       unsafe_allow_html=True,
   )
 
   # Render the multiselect dropdown
   selected_attributes = st.multiselect(
       "",
       attribute_columns,
       default=st.session_state.attr_multiselect,
       key="attr_multiselect_widget"
   )
 
 
 
 
 
# Update session state when dropdown changes
if set(selected_attributes) != st.session_state.selected:
 st.session_state.selected = set(selected_attributes)
 st.session_state.attr_multiselect = selected_attributes
 
 
 
 
 
#--------------------------------------------------------------------------------------------------------- Table layout ------------------------------------------------------------------------------------------------------------------------
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
         click_attr = f"onclick='handleCellClick(this)' data-attr='{val}'" if is_attribute else ""
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
 
 
 
 
 
#----------------------------------------------------------------------------------------------- Python, Javascript, Streamlit Communication ---------------------------------------------------------------------------------------------------
 
#------------------ Javascript for interactivity ----------------------------------
interaction_js = f"""
<script>
// Track selected items globally
let selectedItems = new Set({json.dumps(list(st.session_state.selected))});
 
function updateStreamlit() {{
 // Send selected items to Streamlit
 const selections = Array.from(selectedItems);
 window.parent.postMessage({{
     isStreamlitMessage: true,
     type: 'updateSelections',
     data: selections
 }}, '*');
}}
 
function handleCellClick(element) {{
 const attr = element.getAttribute('data-attr');
 const isSelected = element.style.backgroundColor === 'rgb(146, 208, 80)';
 
 // Toggle visual selection
 element.style.backgroundColor = isSelected ? element.dataset.originalColor : '#92D050';
 
 if (!isSelected) {{
     selectedItems.add(attr);
 }} else {{
     selectedItems.delete(attr);
 }}
 
 // Update selected items display
 const bar = document.getElementById("selectedItems");
 bar.innerText = selectedItems.size === 0 ? "None" : Array.from(selectedItems).join(", ");
 
 // Update Streamlit
 updateStreamlit();
}}
 
document.addEventListener("DOMContentLoaded", function() {{
 // Store original background color of each cell
 const cells = document.querySelectorAll('td');
 cells.forEach(cell => {{
     const original = getComputedStyle(cell).backgroundColor;
     cell.dataset.originalColor = original;
   
     // Initialize selected cells
     const attr = cell.getAttribute('data-attr');
     if (attr && selectedItems.has(attr)) {{
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
   
     // Update display
     document.getElementById("selectedItems").innerText = "None";
   
     // Update Streamlit
     updateStreamlit();
 }});
 
 // Initialize display
 document.getElementById("selectedItems").innerText =
     selectedItems.size === 0 ? "None" : Array.from(selectedItems).join(", ");
}});
</script>
"""
 
#-------------------------- Handle messages from Javascript --------------------
def handle_js_messages():
 # Check if we have a new message from JavaScript
 if hasattr(st.session_state, 'js_message') and st.session_state.js_message:
     message = st.session_state.js_message
     if message['type'] == 'updateSelections':
         # Update session state with new selections
         new_selections = set(message['data'])
         if new_selections != st.session_state.selected:
             st.session_state.selected = new_selections
             st.session_state.attr_multiselect = message['data']
 
# Initialize message handling
if 'js_message' not in st.session_state:
 st.session_state.js_message = None
handle_js_messages()
 
 
 
 
 
 
 
 
 
#--------------------------- JavaScript to handle Streamlit communication--------
streamlit_js = """
<script>
// Function to handle messages from Streamlit
function handleStreamlitMessage(event) {
 if (event.data.isStreamlitMessage) {
     if (event.data.type === 'updateSelections') {
         window.parent.postMessage({
             isStreamlitMessage: true,
             type: 'js_message',
             data: event.data
         }, '*');
     }
 }
}
 
// Listen for messages from the iframe
window.addEventListener('message', handleStreamlitMessage);
</script>
"""
 
# Generate the full HTML
 
html_code = f"""
<div style="overflow-x: auto; width: 100%; padding: 10px; box-sizing: border-box;">
  <div class="zoomed-table">
      {generate_html_table(data, st.session_state.selected)}
  </div>
</div>
"""
 
# Add styling
html_code += """
<div style="overflow-x: auto; width: 100%; padding: 10px; box-sizing: border-box;">
  <div class="zoomed-table">
 
  </div>
</div>
<style>
.zoomed-table {
  transform: scale(0.75);
  transform-origin: top center;
  width: 100%;
}
 
</style>
"""  
 
 
# Display the HTML
html(html_code, height=700)
 
 
 
#------------------------------------------------------------------------------------------ Top use case selection and display ------------------------------------------------------------------------------------------------------------------
 
#------------------------- AI use case description ---------------------------------
use_case_descriptions = {
   "AI-infused experiments in R&D": "This use case focuses on integrating AI into experimental R&D processes to accelerate discovery and optimize results.",
   "AI-powered manufacturing planning in smart factories": "This use case enables intelligent scheduling, resource allocation, and process optimization using AI in smart factories.",
   "AI-infused experiments in R&D": "This use case balaalalalalalallala.",
}
 
 
 
# ---------------------------- Calculate and show top use case -----------------------
if selected_attributes:
   summed = analysis_table[selected_attributes].sum(axis=1)
   top_use_case = summed.idxmax()
 
   # Combine the title and the paragraph with spacing
   use_case_info = f"<b>{top_use_case}</b><br>{use_case_descriptions.get(top_use_case, '')}"
 
   # Display top use case inside a styled box
   st.markdown(
       f"""
       <div style="margin-top: 1em;">
       <label style="font-weight: 700; color: #000;"> Most relevant AI Use Case </label><br>
       <div style="
           background-color: #A8E060;
           padding: 10px;
           border-radius: 8px;
           border: 1px solid #000;
           font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
           font-size: 14px;
           color: #000;
           white-space: pre-wrap;
          "> {use_case_info}
           </div>
       </div>
       """,
       unsafe_allow_html=True
   )
else:
   top_use_case = None  # Default value if no attributes are selected
   st.info("Please select the attributes above to display relevant information.")
 
 
 
#------------------------------------------------------------------------------------------------- Top use case graph display ------------------------------------------------------------------------------------------------------------------
 
st.markdown(
   "<h3 style='font-size:18px; font-weight:700; margin-bottom:0; margin-top:2em; text-align:center;'>Significance levels of attributes for the most relevant AI use case in automotive, based on the user's selection</h3>",
   unsafe_allow_html=True
)
 
if top_use_case:
   # Get all attribute columns for the selected top use case
   attribute_columns = list(analysis_table.columns)
   all_values = analysis_table.loc[top_use_case, attribute_columns]
 
   fig = go.Figure(data=[
       go.Bar(
           x=attribute_columns,
           y=all_values,
           marker_color=[
               '#92D050' if v == 2 else '#FFD966' if v == 1 else '#D9D9D9'
               for v in all_values
           ],
       )
   ])
 
   fig.update_yaxes(
       tickvals=[0, 1, 2],
       ticktext=["Low", "Moderate", "High"],
       title_text="Significance Level",
       range=[0, 2],
       title_font=dict(family='Arial Bold', color='black'),
       tickfont=dict(color='black'),
       
   )
   fig.update_xaxes(
   title_text="Attributes",
   automargin=True,
   title_standoff=30,  # Lower value brings title closer to axis
   tickangle=50,
   title_font=dict(family='Arial Bold', color='black'),
   tickfont=dict(color='black'),
)
   fig.update_layout(
   margin=dict(t=0, b=40)  # Adjust bottom margin (try 20-60)
)
   st.plotly_chart(fig, use_container_width=True)
 
 
 
#-------------------------------------------------------------------------------------------------------- Cluster Analysis --------------------------------------------------------------------------------------------------------------------
 
# Dictionary mapping use cases to their clusters
use_case_to_cluster = {
   "AI-powered manufacturing planning in smart factories": "Cluster 1: Ideation and Intelligent Planning in Automotive",
   "AI-driven Human-Machine Collaboration in ideation": "Cluster 1: Ideation and Intelligent Planning in Automotive",
   "AI-enabled bionic digital twin production planning": "Cluster 1: Ideation and Intelligent Planning in Automotive",
   "AI-infused Human-Robot Collaboration planning": "Cluster 1: Ideation and Intelligent Planning in Automotive",
   "AI-powered material flow planning": "Cluster 1: Ideation and Intelligent Planning in Automotive",
   "AI-based digital twin for lithium-ion battery development": "Cluster 1: Ideation and Intelligent Planning in Automotive",
   "AI-enabled predictive maintenance": "Cluster 1: Ideation and Intelligent Planning in Automotive",
   "AI-driven predictive quality models for customer defects": "Cluster 1: Ideation and Intelligent Planning in Automotive",
   
   "AI- and Genetic Algorithms-based vehicle design": "Cluster 2: AI-optimized design and quality in Automotive",
   "AI-augmented visual inspections": "Cluster 2: AI-optimized design and quality in Automotive",
   "AI-optimized scenario engineering": "Cluster 2: AI-optimized design and quality in Automotive",
   "AI-driven design process": "Cluster 2: AI-optimized design and quality in Automotive",
   "AI- and Bio-inspired Design": "Cluster 2: AI-optimized design and quality in Automotive",
   "AI-assisted quality control of the bumper warpage": "Cluster 2: AI-optimized design and quality in Automotive",
   "AI-optimized braking system test": "Cluster 2: AI-optimized design and quality in Automotive",
   
   "AI-enabled idea generation in the Metaverse": "Cluster 3: AI-driven Customer-Centric Innovation in Automotive",
   "AI-driven interactive collaborative innovation": "Cluster 3: AI-driven Customer-Centric Innovation in Automotive",
   "AI-based identification of consumer adoption stage": "Cluster 3: AI-driven Customer-Centric Innovation in Automotive",
   "AI-powered marketing campaign": "Cluster 3: AI-driven Customer-Centric Innovation in Automotive",
   "AI-driven relationship marketing": "Cluster 3: AI-driven Customer-Centric Innovation in Automotive",
   "AI-powered customer satisfaction analysis": "Cluster 3: AI-driven Customer-Centric Innovation in Automotive",
   "AI-driven competition analysis": "Cluster 3: AI-driven Customer-Centric Innovation in Automotive",
   
   "AI-assisted customer service in after-sales": "Cluster 4: AI in Automotive Customer Service",
   "AI-enabled battery monitoring": "Cluster 4: AI in Automotive Customer Service",
   "AI-assisted staff training": "Cluster 4: AI in Automotive Customer Service",
   
   "AI-infused experiments in R&D": "Cluster 5: AI in Strategic Forecasting",
   "AI-optimized patent analysis": "Cluster 5: AI in Strategic Forecasting",
   "AI-powered forecasting of the technology life cycle of EVs (S-Curve)": "Cluster 5: AI in Strategic Forecasting",
   "AI-assisted ideation": "Cluster 5: AI in Strategic Forecasting",
   "AI-driven vehicles sales prediction": "Cluster 5: AI in Strategic Forecasting"
}
 
 
#---------------- Dictionary mapping clusters to detailed information -------------------------------------
cluster_details = {
   "Cluster 1: Ideation and Intelligent Planning in Automotive": (
       "Focuses on using AI for ideation and intelligent planning in the automotive industry. "
       "This includes material flow planning, predictive maintenance, and more innovative approaches."
   ),
   "Cluster 2: AI-optimized design and quality in Automotive": (
       "Centers on leveraging AI to optimize design processes and ensure quality. "
       "Examples include visual inspections, bio-inspired designs, and scenario engineering."
   ),
   "Cluster 3: AI-driven Customer-Centric Innovation in Automotive": (
       "Aims at driving customer-centric innovations in the automotive sector using AI. Applications include marketing campaigns, customer satisfaction analysis, and competition analysis "
       "Applications include marketing campaigns, customer satisfaction analysis, and competition analysis."
   ),
   "Cluster 4: AI in Automotive Customer Service": (
       "Focuses on enhancing customer service in automotive with AI tools. "
       "This includes battery monitoring, staff training, and after-sales service improvements."
   ),
   "Cluster 5: AI in Strategic Forecasting": (
       "Involves AI applications in strategic forecasting and planning. "
       "Examples include patent analysis, technology lifecycle forecasting, and sales prediction."
   )
}
 
 
 
 
#-------------------------------- Selection of Clusters ------------------------------------------------
 
if top_use_case:
   cluster_name = use_case_to_cluster.get(top_use_case, "Unknown Cluster")
   cluster_info = cluster_details.get(cluster_name, "Detailed information about this cluster is not available.")
 
   st.markdown(
       f"""
       <div style="margin-top: 1em;">
           <label style="font-weight: 700; color: #000;">Cluster details for the most relevant AI use case</label><br>
           <div style="
               width: 100%;
               background-color: #F5F5F5;
               color: #000;
               padding: 10px;
               border: 1px solid #000;
               border-radius: 8px;
               font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
               font-size: 14px;
           ">
               <span style="font-weight:bold;">{cluster_name}</span><br>
               <span>{cluster_info}</span>
           </div>
       </div>
       """,
       unsafe_allow_html=True
   )
else:
   st.info("Please select the attributes above to display relevant information.")
 
 
 
 
 
# -------------------------------------------------------------------------------------------------- Calculate and show other relevant use case --------------------------------------------------------------------------------------------------
if selected_attributes:
   summed = analysis_table[selected_attributes].sum(axis=1)
   top_6_use_cases = summed.nlargest(6).index[1:]  # Get indices of top 6 use cases
 
   # single string for all use cases, separated by <br><br>
   use_cases_info = ""
   for use_case in top_6_use_cases:
       description = use_case_descriptions.get(use_case, "")
       use_cases_info += f"<b>{use_case}</b><br>{description}<br><br>"
 
   # Strip the trailing <br><br> for a clean finish
   use_cases_info = use_cases_info.rstrip("<br><br>")
 
   st.markdown("---")
   st.markdown(
       f"""
       <div style="margin-top: 1em;">
           <label style="font-weight: 700; color: #000;"> Other relevant AI Use Cases</label><br>
           <div style="
               background-color: #F8CAA0;
               padding: 10px;
               border-radius: 8px;
               border: 1px solid #000;
               font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
               font-size: 14px;
               color: #000;
               white-space: pre-wrap;
           ">{use_cases_info}</div>
       </div>
       """,
       unsafe_allow_html=True
   )
   
else:
   top_6_use_cases = None  # Default value if no attributes are selected
   st.info("Please select the attributes above to display relevant information.")
 
 
 
 
 
 
 
 
#------------------------------------------------------------------------------------------------------------- Funnel image -------------------------------------------------------------------------------------------------------------------
 
html_code = """
<canvas id="funnelCanvas" width="1000" height="450" style="width: 100%; height: auto; background: white;"></canvas>
 
<script>
const canvas = document.getElementById('funnelCanvas');
const ctx = canvas.getContext('2d');
canvas.width = canvas.offsetWidth;
canvas.height = 450;
 
const w = canvas.width;
const h = canvas.height;
 
// Trumpet parameters
const bellLength = w * 0.3;  // Bell takes 30% of width
const tubeLength = w * 0.7;  // Tube takes 70%
const startDiameter = 300;   // Starting diameter at bell
const endDiameter = 80;      // Ending diameter at mouthpiece
 
// Inner funnel points (dark blue)
const innerFunnelPoints = {
bellStart: {x: 0, y: h/2 - startDiameter/2},
bellEnd: {x: bellLength, y: h/2 - (startDiameter * 0.7)/2},
tubeEnd: {x: w, y: h/2 - endDiameter/2},
mouthBottom: {x: w, y: h/2 + endDiameter/2},
bellBottomEnd: {x: bellLength, y: h/2 + (startDiameter * 0.7)/2},
bellBottomStart: {x: 0, y: h/2 + startDiameter/2}
};
 
// Outer funnel points (light blue cloud) - 20px larger
const outerFunnelPoints = {
bellStart: {x: -20, y: 0},
bellEnd: {x: bellLength - 20, y: h/2 - (startDiameter * 0.7 + 40)/2},
tubeEnd: {x: w + 20, y: h/2 - (endDiameter + 20)/2},
mouthBottom: {x: w + 20, y: h/2 + (endDiameter + 20)/2},
bellBottomEnd: {x: bellLength - 20, y: h/2 + (startDiameter * 0.7 + 40)/2},
bellBottomStart: {x: -20, y: 450}
};
 
const sectionColors = ['#3498db', '#2874a6', '#1b4f72'];
const outerColor = 'rgba(135, 206, 250, 0.3)';
 
// Text positions for the sections
const textPositions = [
{text: 'Bell Section', x: w * 0.15, y: h/2 - 60},
{text: 'Tube Section', x: w * 0.65, y: h/2 - 40},
{text: 'Mouthpiece', x: w * 0.9, y: h/2 - 20}
];
 
// Generate random colors for dots
function generateColor() {
const colors = ['#e74c3c', '#2ecc71', '#f1c40f', '#3498db', '#9b59b6', '#1abc9c', '#e67e22', '#d35400', '#34495e', '#7f8c8d'];
return colors[Math.floor(Math.random() * colors.length)];
}
 
// Particle classes
class Dot {
constructor(x, y, dx, dy, radius, color, bounds) {
this.x = x;
this.y = y;
this.dx = dx;
this.dy = dy;
this.radius = radius;
this.color = color;
this.bounds = bounds;
}
 
move() {
this.x += this.dx;
this.y += this.dy;
 
if (this.x - this.radius < this.bounds.xMin || this.x + this.radius > this.bounds.xMax) {
  this.dx = -this.dx;
}
if (this.y - this.radius < this.bounds.yMin || this.y + this.radius > this.bounds.yMax) {
  this.dy = -this.dy;
}
}
 
draw(ctx) {
ctx.beginPath();
ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
ctx.fillStyle = this.color;
ctx.fill();
}
}
 
class SmallDot {
constructor(x, y, dx, dy, radius, color, bounds) {
this.x = x;
this.y = y;
this.dx = dx;
this.dy = dy;
this.radius = radius;
this.color = color;
this.bounds = bounds;
}
 
move() {
this.x += this.dx;
this.y += this.dy;
if (this.x < this.bounds.xMin) this.x = this.bounds.xMax;
if (this.x > this.bounds.xMax) this.x = this.bounds.xMin;
if (this.y < this.bounds.yMin) this.y = this.bounds.yMax;
if (this.y > this.bounds.yMax) this.y = this.bounds.yMin;
}
 
draw(ctx) {
ctx.beginPath();
ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
ctx.fillStyle = this.color;
ctx.fill();
}
}
 
// Section bounds for dots
const sectionBounds = [
{xMin: innerFunnelPoints.bellStart.x, xMax: innerFunnelPoints.bellEnd.x,
yMin: innerFunnelPoints.bellStart.y, yMax: innerFunnelPoints.bellBottomStart.y},
{xMin: innerFunnelPoints.bellEnd.x, xMax: innerFunnelPoints.tubeEnd.x,
yMin: innerFunnelPoints.bellStart.y, yMax: innerFunnelPoints.bellBottomStart.y}
];
 
const marketIntroOuterBounds = {
xMin: outerFunnelPoints.bellEnd.x,
xMax: outerFunnelPoints.tubeEnd.x,
yMin: outerFunnelPoints.bellStart.y,
yMax: outerFunnelPoints.bellBottomStart.y
};
 
let sectionDots = [];
let outerSmallDots = [];
let cloudOffset = 0;
let cloudDirection = 1;
 
function randomBetween(min, max) {
return Math.random() * (max - min) + min;
}
 
// Initialize dots
function initDots() {
sectionDots = [];
for (let i = 0; i < 2; i++) {
for (let j = 0; j < 15; j++) {
  sectionDots.push(new Dot(
    randomBetween(sectionBounds[i].xMin + 10, sectionBounds[i].xMax - 10),
    randomBetween(sectionBounds[i].yMin + 10, sectionBounds[i].yMax - 10),
    (Math.random() - 0.5) * 1.5,
    (Math.random() - 0.5) * 1.5,
    5,
    generateColor(),
    sectionBounds[i]
  ));
}
}
 
outerSmallDots = [];
for (let i = 0; i < 80; i++) {
outerSmallDots.push(new SmallDot(
  randomBetween(marketIntroOuterBounds.xMin, marketIntroOuterBounds.xMax),
  randomBetween(marketIntroOuterBounds.yMin, marketIntroOuterBounds.yMax),
  (Math.random() - 0.5) * 0.15,
  (Math.random() - 0.5) * 0.15,
  1.5,
  'rgba(10, 40, 80, 0.3)',
  marketIntroOuterBounds
));
}
}
 
// Trumpet-shaped drawing function
function drawTrumpetFunnel(points, color) {
ctx.fillStyle = color;
ctx.beginPath();
 
// Bell curve (top)
ctx.moveTo(points.bellStart.x, points.bellStart.y);
ctx.bezierCurveTo(
points.bellStart.x + w * 0.1, points.bellStart.y + 25,
points.bellEnd.x - w * 0.1, points.bellEnd.y - 10,
points.bellEnd.x, points.bellEnd.y
);
 
// Tube section (linear taper)
ctx.lineTo(points.tubeEnd.x, points.tubeEnd.y);
 
// Mouthpiece (right end)
ctx.lineTo(points.mouthBottom.x, points.mouthBottom.y);
 
// Bottom tube section (linear taper)
ctx.lineTo(points.bellBottomEnd.x, points.bellBottomEnd.y);
 
// Bottom bell curve (mirror of top)
ctx.bezierCurveTo(
points.bellBottomEnd.x - w * 0.1, points.bellBottomEnd.y + 10,
points.bellBottomStart.x + w * 0.1, points.bellBottomStart.y - 25,
points.bellBottomStart.x, points.bellBottomStart.y
);
 
ctx.closePath();
ctx.fill();
}
 
function drawOuterFunnel() {
cloudOffset += 0.3 * cloudDirection;
if (cloudOffset > 6 || cloudOffset < -6) cloudDirection *= -1;
 
ctx.save();
ctx.shadowColor = 'rgba(135, 206, 250, 0.5)';
ctx.shadowBlur = 20 + cloudOffset*2;
drawTrumpetFunnel(outerFunnelPoints, outerColor);
ctx.restore();
}
 
function drawInnerFunnel() {
drawTrumpetFunnel(innerFunnelPoints, '#154360');
}
 
function drawSectionLines() {
ctx.strokeStyle = "white";
ctx.lineWidth = 2;
ctx.setLineDash([6, 6]);
 
ctx.beginPath();
// Bell to tube divider
ctx.moveTo(innerFunnelPoints.bellEnd.x, innerFunnelPoints.bellEnd.y);
ctx.lineTo(innerFunnelPoints.bellBottomEnd.x, innerFunnelPoints.bellBottomEnd.y);
 
ctx.stroke();
ctx.setLineDash([]);
}
 
function drawLabels() {
ctx.fillStyle = "white";
ctx.font = "bold 22px Arial";
ctx.textAlign = "center";
textPositions.forEach(pos => {
ctx.fillText(pos.text, pos.x, pos.y);
});
}
 
function drawSectionDots() {
sectionDots.forEach(dot => {
dot.draw(ctx);
});
}
 
function moveSectionDots() {
sectionDots.forEach(dot => {
dot.move();
});
}
 
function drawOuterSmallDots() {
outerSmallDots.forEach(dot => {
dot.draw(ctx);
});
}
 
function moveOuterSmallDots() {
outerSmallDots.forEach(dot => {
dot.move();
});
}
 
function animate() {
ctx.clearRect(0, 0, w, h);
drawOuterFunnel();
drawOuterSmallDots();
drawInnerFunnel();
drawSectionLines();
drawLabels();
drawSectionDots();
moveSectionDots();
moveOuterSmallDots();
requestAnimationFrame(animate);
}
 
initDots();
animate();
 
window.addEventListener('resize', function() {
canvas.width = canvas.offsetWidth;
// Update dynamic positions if needed
});
</script>
"""
 
st.title("AI in Innovation Management")
components.html(html_code, height=500)
