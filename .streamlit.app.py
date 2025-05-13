 
 
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
 
# Wrap the table in a div container to manage zoom and scrolling
html_code = selected_bar_html + f"""
<div style="overflow-x: auto; width: 100%; padding: 10px; box-sizing: border-box;">
   <div class="zoomed-table">
       {generate_html_table(data, st.session_state.selected)}
   </div>
</div>
""" + interaction_js
 
# Inject update script
html_code += """
<script>
let selectedItems = new Set();
 
function updateSelectedBar() {
   const bar = document.getElementById("selectedItems");
   bar.innerText = selectedItems.size === 0 ? "None" : Array.from(selectedItems).join(", ");
}
 
function handleCellClick(element) {
   const attr = element.getAttribute('data-attr');
   const isSelected = element.style.backgroundColor === 'rgb(146, 208, 80)';
 
   // Toggle visual selection
   element.style.backgroundColor = isSelected ? element.dataset.originalColor : '#92D050';
 
   if (!isSelected) {
       selectedItems.add(attr);
   } else {
       selectedItems.delete(attr);
   }
 
   updateSelectedBar();
 
   // Notify Streamlit backend
   window.parent.postMessage({
       isStreamlitMessage: true,
       type: 'cellClick',
       data: { attribute: attr, selected: !isSelected }
   }, '*');
}
 
document.addEventListener("DOMContentLoaded", function() {
   // Store original background color of each cell
   const cells = document.querySelectorAll('td');
   cells.forEach(cell => {
       const original = getComputedStyle(cell).backgroundColor;
       cell.dataset.originalColor = original;
   });
 
   document.getElementById('resetButton').addEventListener('click', function() {
       // Clear selections
       selectedItems.clear();
 
       // Restore each cell's original background color
       cells.forEach(cell => {
           cell.style.backgroundColor = cell.dataset.originalColor;
       });
 
       updateSelectedBar();
 
       // Optionally notify Streamlit backend
       window.parent.postMessage({
           isStreamlitMessage: true,
           type: 'resetSelection',
           data: { reset: true }
       }, '*');
   });
 
   updateSelectedBar();
});
</script>
"""
 
# Apply the zoom effect to the table
html_code += """
<style>
.zoomed-table {
   transform: scale(0.75); /* Zoom out to 75% */
   transform-origin: top center;
   width: 100%;
}
</style>
"""
 
html(html_code, height=1200)
 
