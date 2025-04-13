import streamlit as st
import pandas as pd

# Data for the Morphological Box (as closely mapped from the image)
data = [
    ["Teaching Method", "Knowledge", "Factual", "Conceptual", "Procedural", "Metacognitive"],
    [None, "Cognitive processes", "Remembering", "Understanding", "Applying", "Analyzing", "Evaluating", "Creating"],
    [None, "Content presentation", "Expository", None, None, "Explorative"],
    [None, "Knowledge acquisition", "Cumulative", None, None, "Cyclic"],
    [None, "Level", "Undergraduate", "Master", "MBA"],
    ["Course setting", "Course format", "Lecture", "Tutorial", "Workshop", "Project", "Hackathon", "Innovation lab", "Innovation contest"],
    [None, "Participation as", "Individual", None, None, "Team"],
    [None, "Team composition", "Monodisciplinary", None, None, "Interdisciplinary"],
    [None, "Third party involvement", "Involved", None, None, "No involved"],
    ["Course Content", "Data value chain", "Data generation", "Data acquisition", "Data processing", "Data aggregation", "Data Analytics", "Visualization"],
    [None, "Analytics perspective", "Descriptive", "Predictive", "Prescriptive"],
    [None, "Analytics technologies", "(Big) Data analytics", "Text analytics", "Network analytics", "Streaming analytics", "Web analytics"],
    ["Innovation Approach", "Innovation method", "Grounded in innovation mgt.", None, None, "Grounded in analytics"],
    [None, "Creativity technique", "Intuitive", "Discursive", "Mixed"],
    [None, "Ideation approach", "Data first", "Business first"],
    [None, "Innovation level", "Conceptual", "Metadata", "Data"],
    [None, "Data origin", "Open data", "Company", "Teacher", "Self-generation"],
    [None, "Tools", "Given", "Self-selected"],
    [None, "Degree of elaboration", "Concept", "Prototype", "Full-fledged service"],
]

df = pd.DataFrame(data)

def generate_complex_html_table(df):
    html = "<table style='border-collapse: collapse; width: 100%;'>"
    for i in range(len(df)):
        html += "<tr>"
        for j in range(len(df.columns)):
            value = df.iloc[i, j]
            style = "border: 1px solid black; padding: 8px; text-align: center;"

            # Specific row/column spans based on the image structure
            rowspan = 1
            colspan = 1

            if i == 0 and j == 0:
                rowspan = 5
            elif i in [1, 2, 3, 4] and j == 0:
                continue
            elif i == 5 and j == 0:
                rowspan = 4
            elif i in [6, 7, 8] and j == 0:
                continue
            elif i == 9 and j == 0:
                rowspan = 3
            elif i in [10, 11] and j == 0:
                continue
            elif i == 12 and j == 0:
                rowspan = 7
            elif i in [13, 14, 15, 16, 17, 18] and j == 0:
                continue

            if i == 0 and j == 1:
                colspan = 5
                style += "text-align: center;"
            elif i == 1 and j == 1:
                colspan = 7
                style += "text-align: center;"
            elif i == 2 and j == 1:
                colspan = 3
                style += "text-align: center;"
            elif i == 3 and j == 1:
                colspan = 3
                style += "text-align: center;"
            elif i == 5 and j == 1:
                colspan = 7
                style += "text-align: center;"
            elif i == 6 and j == 1:
                colspan = 5
                style += "text-align: center;"
            elif i == 7 and j == 1:
                colspan = 5
                style += "text-align: center;"
            elif i == 8 and j == 1:
                colspan = 5
                style += "text-align: center;"
            elif i == 9 and j == 1:
                colspan = 6
                style += "text-align: center;"
            elif i == 10 and j == 1:
                colspan = 3
                style += "text-align: center;"
            elif i == 11 and j == 1:
                colspan = 5
                style += "text-align: center;"
            elif i == 12 and j == 1:
                colspan = 5
                style += "text-align: center;"
            elif i == 13 and j == 1:
                colspan = 3
                style += "text-align: center;"
            elif i == 14 and j == 1:
                colspan = 2
                style += "text-align: center;"
            elif i == 15 and j == 1:
                colspan = 3
                style += "text-align: center;"
            elif i == 16 and j == 1:
                colspan = 4
                style += "text-align: center;"
            elif i == 17 and j == 1:
                colspan = 2
                style += "text-align: center;"
            elif i == 18 and j == 1:
                colspan = 3
                style += "text-align: center;"

            if pd.notna(value):
                html += f"<td style='{style}' rowspan='{rowspan}' colspan='{colspan}'>{value}</td>"
        html += "</tr>"
    html += "</table>"
    return html

st.write(generate_complex_html_table(df), unsafe_allow_html=True)
