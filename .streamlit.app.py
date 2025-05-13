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
 
# ======= SESSION STATE =======
if "selected" not in st.session_state:
   st.session_state.selected = set()
 
if "attr_multiselect" not in st.session_state:
   st.session_state.attr_multiselect = []
 
# Initialize selected_attributes from session state
selected_attributes = list(st.session_state.selected)
 
# ---------- Selectable attribute list ----------
attribute_columns = list(analysis_table.columns)
 
# Create container for the multiselect
multiselect_container = st.container()
 
# Display the initial multiselect with current selections
with multiselect_container:
   selected_attributes = st.multiselect(
       "Selected attributes (automatically synchronized with your table selections):",
       attribute_columns,
       default=st.session_state.attr_multiselect,
       key="attr_multiselect_widget"
   )
 
# Update session state when dropdown changes
if set(selected_attributes) != st.session_state.selected:
   st.session_state.selected = set(selected_attributes)
   st.session_state.attr_multiselect = selected_attributes
 
# ---------- Calculate and show top use case ----------
if selected_attributes:
   summed = analysis_table[selected_attributes].sum(axis=1)
   top_use_case = summed.idxmax()
   st.success(f"🚀 **Top Use Case:** {top_use_case}")
else:
   st.info("👆 Select attributes by clicking cells in the table below to see the top use case.")
 
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
 
# ======= JAVASCRIPT FOR INTERACTIVITY =======
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
 
# ======= HANDLE MESSAGES FROM JAVASCRIPT =======
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
 
# ======= SELECTED BAR AND TABLE =======







 
# JavaScript to handle Streamlit communication
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
html_code = selected_bar_html + f"""
<div style="overflow-x: auto; width: 100%; padding: 10px; box-sizing: border-box;">
   <div class="zoomed-table">
       {generate_html_table(data, st.session_state.selected)}
   </div>
</div>
""" + interaction_js + streamlit_js
 
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
