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
