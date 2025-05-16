import streamlit as st
import pandas as pd
from streamlit.components.v1 import html
import json
import plotly.graph_objects as go




 
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
html(html_code, height=700)





use_case_descriptions = {
    "AI-infused experiments in R&D": "This use case focuses on integrating AI into experimental R&D processes to accelerate discovery and optimize results.",
    "AI-powered manufacturing planning in smart factories": "This use case enables intelligent scheduling, resource allocation, and process optimization using AI in smart factories.",
    "AI-infused experiments in R&D": "This use case balaalalalalalallala.",
}































# ---------- Calculate and show top use case ----------
if selected_attributes:
    summed = analysis_table[selected_attributes].sum(axis=1)
    top_use_case = summed.idxmax()





    # Combine the title and the paragraph with spacing
    use_case_info = f"{top_use_case}<br><br>{use_case_descriptions.get(top_use_case, '')}"

    # Display top use case inside a styled box
    st.markdown(
        f"""
        <div style="margin-top: 1em;">
        <label style="font-weight: 600;"> Relevant AI Use Case </label><br>
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
    st.info("The relevant use case is displayed here")









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


# Dictionary mapping clusters to detailed information
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
        "Aims at driving customer-centric innovations in the automotive sector using AI. "
        "Applications include marketing campaigns, customer satisfaction analysis, and competition analysis."
    ),
    "Cluster 4: AI in Automotive Customer Service": (
        "Focuses on enhancing customer service in automotive with AI tools. "
        "This includes battery monitoring, staff training, and after-sales service improvements."
    ),
    "<b>Cluster 5: AI in Strategic Forecasting</b>": (
        "Involves AI applications in strategic forecasting and planning. "
        "Examples include patent analysis, technology lifecycle forecasting, and sales prediction."
    )
}











if top_use_case:
    # Fetch the cluster name for the selected use case
    cluster_name = use_case_to_cluster.get(top_use_case, "Unknown Cluster")
    cluster_info = cluster_details.get(cluster_name, "Detailed information about this cluster is not available.")
    
    copyable_text = f"{cluster_name}\n\n{cluster_info}"
    st.markdown("---")
    st.markdown(
    f"""
    <div style="margin-top: 1em;">
        <label style="font-weight: 600;"> Cluster Information </label><br>
        <textarea rows="10" style="
            width: 100%;
            background-color: #F5F5F5;
            color: #000;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif, !important;
            font-size: 14px;
        " readonly>{copyable_text}</textarea>
    </div>
    """,
    unsafe_allow_html=True
)


    
else:
    st.info("Please select a use case to display relevant information.")












# Ensure 'top_use_case' holds the index of your selected use case
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
        range=[0, 2]
    )
    fig.update_xaxes(
    title_text="Attributes",
    automargin=True,
    title_standoff=5,  # Lower value brings title closer to axis
    tickangle=20
)
    fig.update_layout(
    margin=dict(b=60)  # Adjust bottom margin (try 20-60)
)
    st.plotly_chart(fig, use_container_width=True)









