import streamlit as st

def render_powerpoint_table_v2():
    html = """
    <div style="width: 100%; overflow: auto;">  
        <div style="display: flex; font-weight: bold;">
            <div style="width: 100px; border: 1px solid black; padding: 8px;">What ?</div>
            <div style="width: 200px; border: 1px solid black; padding: 8px;">How ?</div>
            <div style="width: 150px; border: 1px solid black; padding: 8px;">When ?</div>
            <div style="flex: 1; border: 1px solid black; padding: 8px;">Contribution</div>
            <div style="flex: 1; border: 1px solid black; padding: 8px;">Technology</div>
            <div style="flex: 1; border: 1px solid black; padding: 8px;">Data</div>
            <div style="flex: 1; border: 1px solid black; padding: 8px;">Process</div>
            <div style="flex: 1; border: 1px solid black; padding: 8px;">Innovation Process</div>
        </div>
        <div style="display: flex;">
            <div style="width: 100px; border: 1px solid black; padding: 8px;">Contribution</div>
            <div style="width: 200px; border: 1px solid black; padding: 8px;">Decision-maker</div>
            <div style="width: 150px; border: 1px solid black; padding: 8px;">Innovation Process</div>
            <div style="flex: 1; border: 1px solid black; padding: 8px;">Efficiency and productivity</div>
            <div style="flex: 1; border: 1px solid black;">Machine</div>
            <div style="flex: 1; border: 1px solid black;">Financial Data</div>
            <div style="flex: 1; border: 1px solid black;">Front End</div>
            <div style="flex: 1; border: 1px solid black; display: none;"></div>
        </div>
        <div style="display: flex;">
            <div style="width: 100px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 200px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 150px; border: 1px solid black; padding: 8px;"></div>
            <div style="flex: 1; border: 1px solid black;">Cost saving</div>
            <div style="flex: 1; border: 1px solid black;">Human-Machine</div>
            <div style="flex: 1; border: 1px solid black;">Market Data</div>
            <div style="flex: 1; border: 1px solid black;">Development</div>
             <div style="flex: 1; border: 1px solid black; display: none;"></div>
        </div>
        <div style="display: flex;">
            <div style="width: 100px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 200px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 150px; border: 1px solid black; padding: 8px;"></div>
            <div style="flex: 1; border: 1px solid black;">Product performance enhancement</div>
            <div style="flex: 1; border: 1px solid black;">AI Component</div>
            <div style="flex: 1; border: 1px solid black;">Product Data</div>
            <div style="flex: 1; border: 1px solid black; display: none;"></div>
             <div style="flex: 1; border: 1px solid black; display: none;"></div>
        </div>
         <div style="display: flex;">
            <div style="width: 100px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 200px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 150px; border: 1px solid black; padding: 8px;"></div>
            <div style="flex: 1; border: 1px solid black;">Produkt performance enhancement</div>
            <div style="flex: 1; border: 1px solid black;">Machine Learning</div>
            <div style="flex: 1; border: 1px solid black;">Customer Data</div>
            <div style="flex: 1; border: 1px solid black; display: none;"></div>
             <div style="flex: 1; border: 1px solid black; display: none;"></div>
        </div>
         <div style="display: flex;">
            <div style="width: 100px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 200px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 150px; border: 1px solid black; padding: 8px;"></div>
            <div style="flex: 1; border: 1px solid black;">Enhanced creativity</div>
            <div style="flex: 1; border: 1px solid black;">Natural Language Processing</div>
            <div style="flex: 1; border: 1px solid black;">Operational Data</div>
             <div style="flex: 1; border: 1px solid black; display: none;"></div>
             <div style="flex: 1; border: 1px solid black; display: none;"></div>
        </div>
         <div style="display: flex;">
            <div style="width: 100px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 200px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 150px; border: 1px solid black; padding: 8px;"></div>
            <div style="flex: 1; border: 1px solid black;">Security</div>
            <div style="flex: 1; border: 1px solid black;">Computer Vision</div>
            <div style="flex: 1; border: 1px solid black;">Organizational Data</div>
             <div style="flex: 1; border: 1px solid black; display: none;"></div>
             <div style="flex: 1; border: 1px solid black; display: none;"></div>
        </div>
         <div style="display: flex;">
            <div style="width: 100px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 200px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 150px; border: 1px solid black; padding: 8px;"></div>
            <div style="flex: 1; border: 1px solid black;">Work Quality</div>
            <div style="flex: 1; border: 1px solid black;">Robotics</div>
            <div style="flex: 1; border: 1px solid black;"></div>
             <div style="flex: 1; border: 1px solid black; display: none;"></div>
             <div style="flex: 1; border: 1px solid black; display: none;"></div>
        </div>
         <div style="display: flex;">
            <div style="width: 100px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 200px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 150px; border: 1px solid black; padding: 8px;"></div>
            <div style="flex: 1; border: 1px solid black; display: none;"></div>
            <div style="flex: 1; border: 1px solid black;">Automation</div>
            <div style="flex: 1; border: 1px solid black; display: none;"></div>
             <div style="flex: 1; border: 1px solid black; display: none;"></div>
             <div style="flex: 1; border: 1px solid black; display: none;"></div>
        </div>
         <div style="display: flex;">
            <div style="width: 100px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 200px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 150px; border: 1px solid black; padding: 8px;"></div>
            <div style="flex: 1; border: 1px solid black; display: none;"></div>
            <div style="flex: 1; border: 1px solid black;">Speech Recognition</div>
            <div style="flex: 1; border: 1px solid black; display: none;"></div>
             <div style="flex: 1; border: 1px solid black; display: none;"></div>
             <div style="flex: 1; border: 1px solid black; display: none;"></div>
        </div>
          <div style="display: flex;">
            <div style="width: 100px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 200px; border: 1px solid black; padding: 8px;"></div>
            <div style="width: 150px; border: 1px solid black; padding: 8px;"></div>
            <div style="flex: 1; border: 1px solid black; display: none;"></div>
            <div style="flex: 1; border: 1px solid black;">Reinforcement Learning</div>
            <div style="flex: 1; border: 1px solid black; display: none;"></div>
             <div style="flex: 1; border: 1px solid black; display: none;"></div>
             <div style="flex: 1; border: 1px solid black; display: none;"></div>
        </div>

    </div>
    """
    st.components.v1.html(html, height=600)

render_powerpoint_table_v2()
