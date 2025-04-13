import streamlit as st
import pandas as pd

data = [
    ["Teaching Method", "Knowledge", "Factual", "Conceptual", "Procedural", "Metacognitive"],
    [None, "Cognitive processes", "Remembering", "Understanding", "Applying", "Analyzing", "Evaluating", "Creating"],
    [None, "Content presentation", "Expository", "", "", "Explorative"],
    [None, "Knowledge acquisition", "Cumulative", "", "", "Cyclic"],
    [None, "Level", "Undergraduate", "Master", "MBA", "", ""],
    ["Course setting", "Course format", "Lecture", "Tutorial", "Workshop", "Project", "Hackathon", "Innovation lab", "Innovation contest"],
    [None, "Participation as", "Individual", "", "", "Team"],
    [None, "Team composition", "Monodisciplinary", "", "", "Interdisciplinary"],
    [None, "Third party involvement", "Involved", "", "", "No involved"],
    ["Course Content", "Data value chain", "Data generation", "Data acquisition", "Data processing", "Data aggregation", "Data Analytics", "Visualization"],
    [None, "Analytics perspective", "Descriptive", "Predictive", "Prescriptive", "", ""],
    [None, "Analytics technologies", "(Big) Data analytics", "Text analytics", "Network analytics", "Streaming analytics", "Web analytics"],
    ["Innovation Approach", "Innovation method", "Grounded in innovation mgt.", "", "", "Grounded in analytics"],
    [None, "Creativity technique", "Intuitive", "Discursive", "Mixed", "", ""],
    [None, "Ideation approach", "Data first", "Business first", "", "", ""],
    [None, "Innovation level", "Conceptual", "Metadata", "Data", "", ""],
    [None, "Data origin", "Open data", "Company", "Teacher", "Self-generation", ""],
    [None, "Tools", "Given", "Self-selected", "", "", ""],
    [None, "Degree of elaboration", "Concept", "Prototype", "Full-fledged service", "", ""],
]

df = pd.DataFrame(data)

def generate_morphological_box_html(df):
    html = "<table style='border-collapse: collapse; width: 100%;'>"
    for i in range(len(df)):
        html += "<tr>"
        for j in range(len(df.columns)):
            value = df.iloc[i, j]
            style = "border: 1px solid black; padding: 8px; text-align: center;"
            rowspan = 1
            colspan = 1

            # Manual Spanning Logic based on visual interpretation
            if i == 0 and j == 0:
                rowspan = 5
                style += "vertical-align: middle;"
            elif i in [1, 2, 3, 4] and j == 0:
                continue
            elif i == 5 and j == 0:
                rowspan = 4
                style += "vertical-align: middle;"
            elif i in [6, 7, 8] and j == 0:
                continue
            elif i == 9 and j == 0:
                rowspan = 3
                style += "vertical-align: middle;"
            elif i in [10, 11] and j == 0:
                continue
            elif i == 12 and j == 0:
                rowspan = 7
                style += "vertical-align: middle;"
            elif i in [13, 14, 15, 16, 17, 18] and j == 0:
                continue

            if i == 0 and j == 1: colspan = 5
            elif i == 1 and j == 1: colspan = 7
            elif i == 2 and j == 1: colspan = 3
            elif i == 3 and j == 1: colspan = 3
            elif i == 5 and j == 1: colspan = 7
            elif i == 6 and j == 1: colspan = 5
            elif i == 7 and j == 1: colspan = 5
            elif i == 8 and j == 1: colspan = 5
            elif i == 9 and j == 1: colspan = 6
            elif i == 10 and j == 1: colspan = 3
            elif i == 11 and j == 1: colspan = 5
            elif i == 12 and j == 1: colspan = 5
            elif i == 13 and j == 1: colspan = 3
            elif i == 14 and j == 1: colspan = 2
            elif i == 15 and j == 1: colspan = 3
            elif i == 16 and j == 1: colspan = 4
            elif i == 17 and j == 1: colspan = 2
            elif i == 18 and j == 1: colspan = 3

            if pd.notna(value) and value != "":
                html += f"<td style='{style}' rowspan='{rowspan}' colspan='{colspan}'>{value}</td>"
        html += "</tr>"
    html += "</table>"
    return html

st.write(generate_morphological_box_html(df), unsafe_allow_html=True)
