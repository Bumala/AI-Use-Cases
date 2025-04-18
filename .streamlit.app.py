import streamlit as st
import pandas as pd

# Set the page layout to "wide"
st.set_page_config(layout="wide")

# Data definition
data = [
    ["Impact (What)", "Benefits", "Quality/Scope/Knowledge", "Time Efficiency", "Cost"],
    [None, "Focus within Business Model Navigator", "Customer Segments", "Value Proposition", "Value Chain", "Revenue Model"],
    [None, "Aim", "Product Innovation", "Process Innovation", "Business Model Innovation"],
    [None, "Ambidexterity", "Exploration", "Exploitation"],
    ["Technology (How)", "AI Role", "Automaton", "Assistant", "Partner"],
    [None, "AI Concepts", "Machine Learning", "Deep Learning", "Artificial Neural Networks", "Natural Language Processing", "Computer Vision", "Robotics"],
    [None, "Analytics Focus", "Descriptive", "Diagnostic", "Predictive", "Prescriptive"],
    [None, "Analytics Problem", "Description/ Summary", "Clustering", "Classification", "Dependency Analysis", "Regression"],
    [None, "Data Type", "Customer Data", "Machine Data", "Business Data (Internal Data)", "Market Data", "Public & Regulatory Data", "Synthetic Data"],
    ["Context (Where/When)", "Innovation Phase", "Front End", "Development", "Market Introduction"],
    [None, "Department", "R&D", "Manufacturing", "Marketing & Sales", "Customer Service"],
]

df = pd.DataFrame(data)

# Function to generate the HTML table
def generate_html_table(df):
    # Define consistent widths
    first_col_width = 160
    second_col_width = 200
    base_cell_width = 150
    cell_height = 50

    def style(width, bold=False):
        bold_style = "font-weight: bold;" if bold else ""
        return f"text-align: center; vertical-align: middle; padding: 10px; border: 1px solid #000000; width: {width}px; height: {cell_height}px; {bold_style}"

    # Define colspans
    colspan_2 = {
        (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 5),
        (2, 2), (2, 3), (2, 4), 
        (4, 2), (4, 3), (4, 4),
        (6, 2), (6, 5),
        (7, 4),
        (9, 2), (9, 3), (9, 4),
        (10, 2), (10, 5), 
    }

    colspan_3 = {
        (3, 2), (3, 3)
    }

    html = "<table style='border-spacing: 0; width: 100%; border-collapse: collapse; table-layout: fixed; border: 3px solid #000000;'>"

    for i, row in df.iterrows():
        html += "<tr>"
        for j, val in enumerate(row):
            if pd.isna(val):
                continue


            #first column format, column 0
            if j == 0:
                if i == 0:
                    html += f"<td rowspan='4' style='{style(first_col_width, bold=True)} background-color: #61cbf3; border-bottom: 3px solid #000000;'>{val}</td>"
                elif i == 4:
                    html += f"<td rowspan='5' style='{style(first_col_width, bold=True)} background-color: #61cbf3; border-bottom: 3px solid #000000;'>{val}</td>"
                elif i == 9:
                    html += f"<td rowspan='2' style='{style(first_col_width, bold=True)} background-color: #61cbf3;'>{val}</td>"
                else:
                    continue


            #making inner thick border boundaries
            elif i == 3 and j == 1:  
                html += f"<td style='{style(base_cell_width, bold=True)} background-color: #94dcf8; border-bottom: 3px solid #000000;'>{val}</td>"
            
            elif i == 8 and j == 1:  
                html += f"<td style='{style(base_cell_width, bold=True)} background-color: #94dcf8; border-bottom: 3px solid #000000;'>{val}</td>"

            elif i == 8 and j == 2:  
                html += f"<td style='{style(base_cell_width)} background-color: #f1fbfe; border: 1px solid #000000; border-bottom: 3px solid #000000;'>{val}</td>"

            elif i == 8 and j == 4:  
                html += f"<td style='{style(base_cell_width)} background-color: #f1fbfe; border: 1px solid #000000; border-bottom: 3px solid #000000;'>{val}</td>"

            elif i == 8 and j == 6:  
                html += f"<td style='{style(base_cell_width)} background-color: #f1fbfe; border: 1px solid #000000; border-bottom: 3px solid #000000;'>{val}</td>"


            
            elif j == 1:
                html += f"<td style='{style(second_col_width, bold=True)} background-color: #94dcf8;'>{val}</td>"
            elif (i, j) in colspan_3:
                html += f"<td colspan='3' style='{style(base_cell_width * 3)} background-color: #f1fbfe; border: 1px solid #000000; border-bottom: 3px solid #000000;'>{val}</td>"
            elif (i, j) in colspan_2:
                html += f"<td colspan='2' style='{style(base_cell_width * 2)} background-color: #f1fbfe; border: 1px solid #000000;'>{val}</td>"

            
            else:
                html += f"<td style='{style(base_cell_width)} background-color: #f1fbfe;'>{val}</td>"
        html += "</tr>"

    html += "</table>"
    return html

# Apply CSS to center the table with zoom and ensure proper alignment
st.markdown("""
    <style>
        .center-table {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 100%;
            margin: 0 auto;
            transform: scale(0.9); /* Zoom out slightly to fit the table on the screen */
            transform-origin: top center;
        }
        table {
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Render the table in Streamlit within the centered container
st.markdown('<div class="center-table">' + generate_html_table(df) + '</div>', unsafe_allow_html=True)


# Create the new analysis table below your existing code
analysis_table_data = {
    "Use Case": ["AI-infused experiments in R&D", "AI-powered manufacturing planning in smart factories", "AI-driven Human-Machine Collaboration in ideation",
                 "AI-enabled idea generation in the Metaverse", "AI-optimized patent analysis", "AI-powered forecasting of the technology life cycle of EVs (S-Curve)",
                "AI-enabled bionic digital twin production planning", "AI-infused Human-Robot Collaboration planning", "AI-powered material flow planning",
                "AI-assisted ideation", "AI-driven interactive collaborative innovation", "AI-based digital twin for lithium-ion battery development", 
                 "AI- and Genetic Algorithms-based vehicle design", "AI-augmented visual inspections", "AI-optimized scenario engineering", "AI-driven design process", 
                 "AI- and Bio-inspired Design", "AI-assisted quality control of the bumper warpage", "AI-enabled predictive maintenance", "AI-optimized braking system test", 
                 "AI-based identification of consumer adoption stage", "AI-powered marketing campaign", "AI-driven relationship marketing", "AI-assisted customer service in after-sales", 
                 "AI-enabled battery monitoring", "AI-assisted staff training", "AI-driven predictive quality models for customer defects", "AI-powered customer satisfaction analysis", 
                 "AI-driven competition analysis", "AI-driven vehicles sales prediction"
],
"Quality/Scope/Knowledge": [],
"Time Efficiency": [],
"Cost": [],

"Customer Segments": [],
"Value Proposition": [],
"Value Chain": [],
"Revenue Model": [],

"Product Innovation": [],
"Process Innovation": [],
"Business Model Innovation": [],

"Exploration": [],
"Exploitation": [],

"Automaton": [],
"Assistant": [],
"Partner": [],

"Machine Learning": [],
"Deep Learning": [],
"Artificial Neural Networks": [],
"Natural Language Processing": [],
"Computer Vision": [],
"Robotics": [],

"Descriptive": [],
"Diagnostic": [],
"Predictive": [],
"Prescriptive": [],

"Description/ Summary": [],
"Clustering": [],
"Classification": [],
"Dependency Analysis": [],
"Regression": [],

"Customer Data": [],
"Machine Data": [],
"Business Data (Internal Data)": [],
"Market Data": [],
"Public & Regulatory Data": [],
"Synthetic Data": [],

"Front End": [],
"Development": [],
"Market Introduction": [],

"R&D": [],
"Manufacturing": [],
"Marketing & Sales": [],
"Customer Service": [],

}

analysis_table = pd.DataFrame(analysis_table_data)

# Perform analysis or other operations with the table



