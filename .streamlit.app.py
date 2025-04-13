import streamlit as st

def render_powerpoint_table_v3():
    html = """
    <div style="width: 100%; overflow-x: auto;">
        <div style="display: flex; font-weight: bold;">
            <div class="cell header" style="width: 100px;">What ?</div>
            <div class="cell header" style="width: 200px;">How ?</div>
            <div class="cell header" style="width: 150px;">When ?</div>
            <div class="cell header" style="flex: 1;">Contribution</div>
            <div class="cell header" style="flex: 1;">Technology</div>
            <div class="cell header" style="flex: 1;">Data</div>
            <div class="cell header" style="flex: 1;">Process</div>
            <div class="cell header" style="flex: 1;">Innovation Process</div>
        </div>
        <div style="display: flex;">
            <div class="cell" style="width: 100px;">Contribution</div>
            <div class="cell" style="width: 200px;">Decision-maker</div>
            <div class="cell" style="width: 150px;">Innovation Process</div>
            <div class="cell" style="flex: 1;">Efficiency and productivity</div>
            <div class="cell" style="flex: 1;">Machine</div>
            <div class="cell" style="flex: 1;">Financial Data</div>
            <div class="cell" style="flex: 1;">Front End</div>
            <div class="empty-cell" style="flex: 1; display: none;"></div>
        </div>
        <div style="display: flex;">
            <div class="empty-cell" style="width: 100px; display: none;"></div>
            <div class="empty-cell" style="width: 200px; display: none;"></div>
            <div class="empty-cell" style="width: 150px; display: none;"></div>
            <div class="cell" style="flex: 1;">Cost saving</div>
            <div class="cell" style="flex: 1;">Human-Machine</div>
            <div class="cell" style="flex: 1;">Market Data</div>
            <div class="cell" style="flex: 1;">Development</div>
             <div class="empty-cell" style="flex: 1; display: none;"></div>
        </div>
        <div style="display: flex;">
            <div class="empty-cell" style="width: 100px; display: none;"></div>
            <div class="empty-cell" style="width: 200px; display: none;"></div>
            <div class="empty-cell" style="width: 150px; display: none;"></div>
            <div class="cell" style="flex: 1;">Product performance enhancement</div>
            <div class="cell" style="flex: 1;">AI Component</div>
            <div class="cell" style="flex: 1;">Product Data</div>
            <div class="empty-cell" style="flex: 1; display: none;"></div>
             <div class="empty-cell" style="flex: 1; display: none;"></div>
        </div>
         <div style="display: flex;">
            <div class="empty-cell" style="width: 100px; display: none;"></div>
            <div class="empty-cell" style="width: 200px; display: none;"></div>
            <div class="empty-cell" style="width: 150px; display: none;"></div>
            <div class="cell" style="flex: 1;">Produkt performance enhancement</div>
            <div class="cell" style="flex: 1;">Machine Learning</div>
            <div class="cell" style="flex: 1;">Customer Data</div>
            <div class="empty-cell" style="flex: 1; display: none;"></div>
             <div class="empty-cell" style="flex: 1; display: none;"></div>
        </div>
         <div style="display: flex;">
            <div class="empty-cell" style="width: 100px; display: none;"></div>
            <div class="empty-cell" style="width: 200px; display: none;"></div>
            <div class="empty-cell" style="width: 150px; display: none;"></div>
            <div class="cell" style="flex: 1;">Enhanced creativity</div>
            <div class="cell" style="flex: 1;">Natural Language Processing</div>
            <div class="cell" style="flex: 1;">Operational Data</div>
             <div class="empty-cell" style="flex: 1; display: none;"></div>
             <div class="empty-cell" style="flex: 1; display: none;"></div>
        </div>
         <div style="display: flex;">
            <div class="empty-cell" style="width: 100px; display: none;"></div>
            <div class="empty-cell" style="width: 200px; display: none;"></div>
            <div class="empty-cell" style="width: 150px; display: none;"></div>
            <div class="cell" style="flex: 1;">Security</div>
            <div class="cell" style="flex: 1;">Computer Vision</div>
            <div class="cell" style="flex: 1;">Organizational Data</div>
             <div class="empty-cell" style="flex: 1; display: none;"></div>
             <div class="empty-cell" style="flex: 1; display: none;"></div>
        </div>
         <div style="display: flex;">
            <div class="empty-cell" style="width: 100px; display: none;"></div>
            <div class="empty-cell" style="width: 200px; display: none;"></div>
            <div class="empty-cell" style="width: 150px; display: none;"></div>
            <div class="cell" style="flex: 1;">Work Quality</div>
            <div class="cell" style="flex: 1;">Robotics</div>
            <div class="cell" style="flex: 1;"></div>
             <div class="empty-cell" style="flex: 1; display: none;"></div>
             <div class="empty-cell" style="flex: 1; display: none;"></div>
        </div>
         <div style="display: flex;">
            <div class="empty-cell" style="width: 100px; display: none;"></div>
            <div class="empty-cell" style="width: 200px; display: none;"></div>
            <div class="empty-cell" style="width: 150px; display: none;"></div>
            <div class="empty-cell" style="flex: 1; display: none;"></div>
            <div class="cell" style="flex: 1;">Automation</div>
            <div class="empty-cell" style="flex: 1; display: none;"></div>
             <div class="empty-cell" style="flex: 1; display: none;"></div>
             <div class="empty-cell" style="flex: 1; display: none;"></div>
        </div>
         <div style="display: flex;">
            <div class="empty-cell" style="width: 100px; display: none;"></div>
            <div class="empty-cell" style="width: 200px; display: none;"></div>
            <div class="empty-cell" style="width: 150px; display: none;"></div>
            <div class="empty-cell" style="flex: 1; display: none;"></div>
            <div class="cell" style="flex: 1;">Speech Recognition</div>
            <div class="empty-cell" style="flex: 1; display: none;"></div>
             <div class="empty-cell" style="flex: 1; display: none;"></div>
             <div class="empty-cell" style="flex: 1; display: none;"></div>
        </div>
          <div style="display: flex;">
            <div class="empty-cell" style="width: 100px; display: none;"></div>
            <div class="empty-cell" style="width: 200px; display: none;"></div>
            <div class="empty-cell" style="width: 150px; display: none;"></div>
            <div class="empty-cell" style="flex: 1; display: none;"></div>
            <div class="cell" style="flex: 1;">Reinforcement Learning</div>
            <div class="empty-cell" style="flex: 1; display: none;"></div>
             <div class="empty-cell" style="flex: 1; display: none;"></div>
             <div class="empty-cell" style="flex: 1; display: none;"></div>
        </div>

    </div>
    """
    st.components.v1.html(html, height=600)

render_powerpoint_table_v3()
