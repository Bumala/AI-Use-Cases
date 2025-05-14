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











# Display the first drop down list with current selections
with multiselect_container:
    # Add a styled sentence above the dropdown
    st.markdown(
        """
        <p style="font-size:18px; font-weight:bold; color:black;margin-bottom: 0px;">
            Select attributes in the drop down list below to identify the relevant use case and cluster:
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











 
# ---------- Calculate and show top use case ----------
if selected_attributes:
  summed = analysis_table[selected_attributes].sum(axis=1)
  top_use_case = summed.idxmax()
  st.success(f" **Relevant Use Case:** {top_use_case}")
else:
  st.info("The relevant use case is displayed here")






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
html(html_code, height=1200)







import streamlit as st
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# ---------- Generate Dummy Use Cases ----------
def generate_use_cases(stage, x_range, y_range):
    return pd.DataFrame({
        "x": np.random.uniform(x_range[0], x_range[1], 10),
        "y": np.random.uniform(y_range[0], y_range[1], 10),
        "stage": stage,
        "description": [f"{stage} Use Case #{i+1}" for i in range(10)]
    })

# Funnel stages
front_end = generate_use_cases("Front End", (0.1, 0.3), (0.6, 1.0))
development = generate_use_cases("Development", (0.4, 0.6), (0.4, 0.8))
market_intro = generate_use_cases("Market Introduction", (0.7, 0.9), (0.3, 0.7))
df = pd.concat([front_end, development, market_intro]).reset_index(drop=True)

# ---------- Simulated selection + calculation ----------
selected_attributes = st.multiselect("Select Attributes", options=["Attr 1", "Attr 2", "Attr 3"])
analysis_table = pd.DataFrame(np.random.randint(0, 10, size=(len(df), len(selected_attributes))),
                              columns=selected_attributes)
analysis_table["description"] = df["description"]

# ---------- Calculate top use case ----------
top_use_case = None
if selected_attributes:
    summed = analysis_table[selected_attributes].sum(axis=1)
    top_idx = summed.idxmax()
    top_use_case = analysis_table.loc[top_idx, "description"]
    st.success(f"**Relevant Use Case:** {top_use_case}")
else:
    st.info("Select attributes to identify the most relevant use case.")

# ---------- Build Plotly Figure ----------
fig = go.Figure()

# CASE 1: BEFORE SELECTION – show all use case dots
if not selected_attributes:
    # Funnel chart setup
    fig.add_trace(go.Funnel(
        y=["Front End", "Development", "Market Introduction"],
        x=[120, 90, 50],  # Example funnel values
        textinfo="value+percent initial",
        marker=dict(color=["blue", "green", "red"]),
    ))

    # Show all use case dots with clickable functionality
    fig.add_trace(go.Scatter(
        x=df["x"],
        y=df["y"],
        mode="markers",
        marker=dict(size=10, color="steelblue", opacity=0.7),
        text=df["description"],
        hoverinfo="text",
        showlegend=False,
        customdata=df["description"],  # Attach custom data to each point (use case description)
        name="Use Case Dots"
    ))

# CASE 2: AFTER SELECTION – show only top use case
elif top_use_case:
    top_row = df[df["description"] == top_use_case].iloc[0]

    # Funnel chart setup
    fig.add_trace(go.Funnel(
        y=["Front End", "Development", "Market Introduction"],
        x=[120, 90, 50],  # Example funnel values
        textinfo="value+percent initial",
        marker=dict(color=["blue", "green", "red"]),
    ))

    # Dot for the top use case
    fig.add_trace(go.Scatter(
        x=[top_row["x"]],
        y=[top_row["y"]],
        mode="markers",
        marker=dict(size=14, color='crimson'),
        text=[top_row["description"]],
        hoverinfo='text',
        showlegend=False
    ))

    # Line from the top use case to the funnel
    fig.add_trace(go.Scatter(
        x=[top_row["x"], top_row["x"]],
        y=[top_row["y"], top_row["y"] - 0.1],
        mode='lines',
        line=dict(color='gray', dash='dot'),
        hoverinfo='skip',
        showlegend=False
    ))

    # Text box for the top use case
    fig.add_trace(go.Scatter(
        x=[top_row["x"]],
        y=[top_row["y"] - 0.12],
        text=[f"🔍 {top_row['description']}"],
        mode='text',
        textposition="top center",
        hoverinfo='skip',
        showlegend=False
    ))

# ---------- Add Custom Background (Shapes) ----------
fig.update_layout(
    title="Interactive Funnel with Use Cases",
    height=600,
    width=1000,
    xaxis=dict(showgrid=False, zeroline=False, visible=False, range=[0, 1]),
    yaxis=dict(showgrid=False, zeroline=False, visible=False, range=[0, 1.2]),
    plot_bgcolor='white',  # Set plot background color
    paper_bgcolor='lightgray',  # Set paper background color
    shapes=[
        dict(
            type="rect",
            x0=0, x1=1, y0=0, y1=1,
            xref="paper", yref="paper",
            fillcolor="rgba(0, 0, 255, 0.1)",  # Light blue background
            line=dict(width=0),
            layer="below"
        ),
    ],
    margin=dict(l=40, r=40, t=40, b=40),
)

# ---------- Show Plotly Figure in Streamlit ----------
plotly_chart = st.plotly_chart(fig, use_container_width=True)

# ---------- Handle Dot Clicks ----------
# If the user clicks on any of the dots, show the information in the sidebar or main area
click_data = st.session_state.get("click_data", None)

if click_data:
    clicked_description = click_data['points'][0]['customdata']
    st.sidebar.write(f"**Clicked Use Case:** {clicked_description}")
    
# Update the session state with the latest click data
def handle_click(trace, points, selector):
    if points.point_inds:
        st.session_state["click_data"] = points
        st.experimental_rerun()  # Rerun the app to reflect new data

# Set the click callback to handle the event
fig.data[0].on_click(handle_click)














