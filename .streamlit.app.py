import streamlit as st
import pandas as pd

def render_powerpoint_table():
    html = """
    <div style="display: table; border-collapse: collapse;">
        <div style="display: table-row; font-weight: bold;">
            <div style="display: table-cell; border: 1px solid black; padding: 8px; width: 100px;">What ?</div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px; width: 200px;">How ?</div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px; width: 150px;">When ?</div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;">Contribution</div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;">Technology</div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;">Data</div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;">Process</div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;">Innovation Process</div>
        </div>
        <div style="display: table-row;">
            <div style="display: table-cell; border: 1px solid black; padding: 8px;">Contribution</div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;">Decision-maker</div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;">Innovation Process</div>
            <div style="display: table-cell; border: 1px solid black;">Efficiency and productivity</div>
            <div style="display: table-cell; border: 1px solid black;">Machine</div>
            <div style="display: table-cell; border: 1px solid black;">Financial Data</div>
            <div style="display: table-cell; border: 1px solid black;">Front End</div>
        </div>
        <div style="display: table-row;">
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black;">Cost saving</div>
            <div style="display: table-cell; border: 1px solid black;">Human-Machine</div>
            <div style="display: table-cell; border: 1px solid black;">Market Data</div>
            <div style="display: table-cell; border: 1px solid black;">Development</div>

        </div>
        <div style="display: table-row;">
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black;">Product performance enhancement</div>
            <div style="display: table-cell; border: 1px solid black;">AI Component</div>
            <div style="display: table-cell; border: 1px solid black;">Product Data</div>
            <div style="display: table-cell; border: 1px solid black;"></div>
        </div>
         <div style="display: table-row;">
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black;">Produkt performance enhancement</div>
            <div style="display: table-cell; border: 1px solid black;">Machine Learning</div>
            <div style="display: table-cell; border: 1px solid black;">Customer Data</div>
             <div style="display: table-cell; border: 1px solid black;"></div>
        </div>
         <div style="display: table-row;">
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black;">Enhanced creativity</div>
            <div style="display: table-cell; border: 1px solid black;">Natural Language Processing</div>
            <div style="display: table-cell; border: 1px solid black;">Operational Data</div>
             <div style="display: table-cell; border: 1px solid black;"></div>
        </div>
         <div style="display: table-row;">
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black;">Security</div>
            <div style="display: table-cell; border: 1px solid black;">Computer Vision</div>
            <div style="display: table-cell; border: 1px solid black;">Organizational Data</div>
             <div style="display: table-cell; border: 1px solid black;"></div>
        </div>
         <div style="display: table-row;">
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black;">Work Quality</div>
            <div style="display: table-cell; border: 1px solid black;">Robotics</div>
            <div style="display: table-cell; border: 1px solid black;"></div>
             <div style="display: table-cell; border: 1px solid black;"></div>
        </div>
         <div style="display: table-row;">
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black;"></div>
            <div style="display: table-cell; border: 1px solid black;">Automation</div>
            <div style="display: table-cell; border: 1px solid black;"></div>
             <div style="display: table-cell; border: 1px solid black;"></div>
        </div>
         <div style="display: table-row;">
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black;"></div>
            <div style="display: table-cell; border: 1px solid black;">Speech Recognition</div>
            <div style="display: table-cell; border: 1px solid black;"></div>
             <div style="display: table-cell; border: 1px solid black;"></div>
        </div>
          <div style="display: table-row;">
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black; padding: 8px;"></div>
            <div style="display: table-cell; border: 1px solid black;"></div>
            <div style="display: table-cell; border: 1px solid black;">Reinforcement Learning</div>
            <div style="display: table-cell; border: 1px solid black;"></div>
             <div style="display: table-cell; border: 1px solid black;"></div>
        </div>


    </div>
    """
    st.components.v1.html(html, height=600)  # Adjust height as needed

render_powerpoint_table()
