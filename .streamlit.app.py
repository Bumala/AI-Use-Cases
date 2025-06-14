import streamlit as st
import pandas as pd
from streamlit.components.v1 import html
import json
import plotly.graph_objects as go
import streamlit.components.v1 as components
 
 
#------------------------------------------------------------------------------------------------------ Streamlit page layout -------------------------------------------------------------------------------------------------------------------
# Set Streamlit page layout
st.set_page_config(layout="wide")
 



#------------------------------------------------------------------------------------------------------------- Funnel image -------------------------------------------------------------------------------------------------------------------
 
html_code = """
<canvas id="funnelCanvas" width="1000" height="450" style="width: 100%; height: auto; background: white;"></canvas>

<script>
const canvas = document.getElementById('funnelCanvas');
const ctx = canvas.getContext('2d');
canvas.width = canvas.offsetWidth;
canvas.height = 450;

const w = canvas.width;
const h = canvas.height;

// Trumpet parameters
const bellLength = w * 0.3;
const tubeLength = w * 0.7;
const startDiameter = 300;
const endDiameter = 60;
const tubeStartRatio = 0.5;

// Inner funnel points
const innerFunnelPoints = {
  bellStart: {x: 0, y: h/2 - startDiameter/2},
  bellEnd: {x: bellLength, y: h/2 - (startDiameter * tubeStartRatio)/2},
  tubeEnd: {x: w, y: h/2 - endDiameter/3},
  mouthBottom: {x: w, y: h/2 + endDiameter/3},
  bellBottomEnd: {x: bellLength, y: h/2 + (startDiameter * tubeStartRatio)/2},
  bellBottomStart: {x: 0, y: h/2 + startDiameter/2}
};

// Outer funnel points
const outerFunnelPoints = {
  bellStart: {x: -20, y: 0},
  bellEnd: {x: bellLength - 20, y: h/2 - (startDiameter * 0.7 + 40)/2},
  tubeEnd: {x: 900, y: h/2 - (endDiameter + 20)/2},
  mouthBottom: {x: 900, y: h/2 + (endDiameter + 20)/2},
  bellBottomEnd: {x: bellLength - 20, y: h/2 + (startDiameter * 0.7 + 40)/2},
  bellBottomStart: {x: -20, y: 450}
};


const textPositions = [
  {text: 'Front End', x: w * 0.1, y: h/2 + 5 },
  {text: 'Development', x: w * 0.5, y: h/2 + 5 },
  {text: 'Market Introduction', x: w * 0.85, y: h/2 + 5 }
];

function generateColor() {
  const colors = ['#e74c3c', '#2ecc71', '#f1c40f', '#3498db', '#9b59b6', '#1abc9c', '#e67e22', '#d35400', '#34495e', '#7f8c8d'];
  return colors[Math.floor(Math.random() * colors.length)];
}

class Dot {
  constructor(x, y, dx, dy, radius, color, bounds) {
    this.x = x;
    this.y = y;
    this.dx = dx;
    this.dy = dy;
    this.radius = radius;
    this.color = color;
    this.bounds = bounds;
  }

  move() {
    this.x += this.dx;
    this.y += this.dy;
    if (this.x < this.bounds.xMin) this.x = this.bounds.xMax;
    if (this.x > this.bounds.xMax) this.x = this.bounds.xMin;
    if (this.y < this.bounds.yMin) this.y = this.bounds.yMax;
    if (this.y > this.bounds.yMax) this.y = this.bounds.yMin;
  }

  draw(ctx) {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fillStyle = this.color;
    ctx.fill();
  }
}

class SmallDot {
  constructor(x, y, dx, dy, radius, color, bounds) {
    this.x = x;
    this.y = y;
    this.dx = dx;
    this.dy = dy;
    this.radius = radius;
    this.color = color;
    this.bounds = bounds;
  }

  move() {
    this.x += this.dx;
    this.y += this.dy;
    if (this.x < this.bounds.xMin) this.x = this.bounds.xMax;
    if (this.x > this.bounds.xMax) this.x = this.bounds.xMin;
    if (this.y < this.bounds.yMin) this.y = this.bounds.yMax;
    if (this.y > this.bounds.yMax) this.y = this.bounds.yMin;
  }

  draw(ctx) {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fillStyle = this.color;
    ctx.fill();
  }
}

const sectionBounds = [
  {
    xMin: innerFunnelPoints.bellStart.x,
    xMax: innerFunnelPoints.bellEnd.x,
    yMin: h / 2 - 100,
    yMax: h / 2 + 100
  },
  {
    xMin: innerFunnelPoints.bellEnd.x,
    xMax: innerFunnelPoints.tubeEnd.x,
    yMin: h / 2 - 40,
    yMax: h / 2 + 40
  }
];


const marketIntroOuterBounds = {
  xMin: 900,
  xMax: 2000,
  yMin: h/2 - 50,
  yMax: h/2 + 50
};

let sectionDots = [];
let outerSmallDots = [];
let cloudOffset = 0;
let cloudDirection = 1;

function randomBetween(min, max) {
  return Math.random() * (max - min) + min;
}

// Initialize dots
function initDots() {
  sectionDots = [];
  for (let i = 0; i < 2; i++) {
    for (let j = 0; j < 15; j++) {
      sectionDots.push(new Dot(
        randomBetween(sectionBounds[i].xMin + 10, sectionBounds[i].xMax - 10),
        randomBetween(sectionBounds[i].yMin + 10, sectionBounds[i].yMax - 10),
        Math.random() * 0.5 + 0.3, // always moving right
        (Math.random() - 0.5) * 0.5,
        5,
        generateColor(),
        sectionBounds[i]
      ));
    }
  }

  outerSmallDots = [];
  for (let i = 0; i < 4000; i++) {
    outerSmallDots.push(new SmallDot(
      randomBetween(marketIntroOuterBounds.xMin, marketIntroOuterBounds.xMax),
      randomBetween(marketIntroOuterBounds.yMin, marketIntroOuterBounds.yMax),
      (Math.random() - 0.5) * 0.15,
      (Math.random() - 0.5) * 0.15,
      1.5,
      'rgba(10, 40, 80, 0.3)',
      marketIntroOuterBounds
    ));
  }
}

// Draw funnels
function drawTrumpetFunnel(points, color) {
  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.moveTo(points.bellStart.x, points.bellStart.y);
  ctx.bezierCurveTo(
  points.bellStart.x + w * 0.15, points.bellStart.y + 40,
  points.bellEnd.x - w * 0.05, points.bellEnd.y - 30,
  points.bellEnd.x, points.bellEnd.y
);



  ctx.lineTo(points.tubeEnd.x, points.tubeEnd.y);
  ctx.lineTo(points.mouthBottom.x, points.mouthBottom.y);
  ctx.lineTo(points.bellBottomEnd.x, points.bellBottomEnd.y);
  ctx.bezierCurveTo(
  points.bellBottomEnd.x - w * 0.05, points.bellBottomEnd.y + 30,
  points.bellBottomStart.x + w * 0.15, points.bellBottomStart.y - 40,
  points.bellBottomStart.x, points.bellBottomStart.y
);



  ctx.closePath();
  ctx.fill();
}

let expansionProgress = 0;  
let expansionSpeed = 0.005;
const maxScale = 1.0;

let isPaused = false;
let pauseCounter = 0;
const pauseFrames = 120;

function drawOuterFunnel() {
  let scale;

  if (isPaused) {
    scale = maxScale;
    pauseCounter++;
    if (pauseCounter >= pauseFrames) {
      isPaused = false;
      pauseCounter = 0;
      expansionProgress = 0;
    }
  } else {
    scale = Math.sin(expansionProgress * Math.PI / 2);
    expansionProgress += expansionSpeed;
    if (scale >= maxScale) {
      scale = maxScale;
      isPaused = true;
    }
  }

  ctx.save();
  ctx.translate(0, h / 2);
  ctx.scale(scale, scale);
  ctx.translate(0, -h / 2);

  ctx.shadowColor = 'rgba(135, 206, 250, 0.4)';
  ctx.shadowBlur = 15 * scale;
  drawTrumpetFunnel(outerFunnelPoints, 'rgba(135, 206, 250, 0.3)');
  ctx.restore();
}

function drawInnerFunnel() {
  drawTrumpetFunnel(innerFunnelPoints, '#154360');
}

function drawSectionLines() {
  ctx.strokeStyle = "white";
  ctx.lineWidth = 2;
  ctx.setLineDash([6, 6]);

  ctx.beginPath();
  ctx.moveTo(innerFunnelPoints.bellEnd.x, innerFunnelPoints.bellEnd.y-60);
  ctx.lineTo(innerFunnelPoints.bellBottomEnd.x, innerFunnelPoints.bellBottomEnd.y+60);
  ctx.stroke();

  ctx.beginPath();
  ctx.moveTo(900, outerFunnelPoints.bellStart.y);
  ctx.lineTo(900, outerFunnelPoints.bellBottomStart.y);
  ctx.stroke();

  ctx.setLineDash([]);
}

function drawLabels() {
  ctx.fillStyle = "white";
  ctx.font = "bold 22px Arial";
  ctx.textAlign = "center";
  textPositions.forEach(pos => {
    ctx.fillText(pos.text, pos.x, pos.y);
  });
}

function drawSectionDots() {
  sectionDots.forEach(dot => dot.draw(ctx));
}

function moveSectionDots() {
  sectionDots = sectionDots.flatMap(dot => {
    dot.move();

    // At x ≈ 300: simulate a filter gate
    if (dot.bounds === sectionBounds[0] && dot.x > sectionBounds[0].xMax - 5) {
      if (Math.random() < 0.5) {
        // Let dot proceed to next section
        dot.bounds = sectionBounds[1];
        return [dot];
      } else {
        // Reset to beginning of section 0
        dot.x = sectionBounds[0].xMin + 10;
        dot.y = randomBetween(sectionBounds[0].yMin + 10, sectionBounds[0].yMax - 10);
        dot.dx = randomBetween(0.5, 1.0);
        dot.dy = (Math.random() - 0.5) * 0.3;
        return [dot];
      }
    }

    // At x ≈ 900: another filter gate
    if (dot.bounds === sectionBounds[1] && dot.x > sectionBounds[1].xMax - 5) {
      if (Math.random() < 0.5) {
        // Let it continue beyond 900 (into fading or external region)
        dot.bounds = { xMin: 900, xMax: 1500, yMin: dot.y - 10, yMax: dot.y + 10 }; // loose bounds
        return [dot];
      } else {
        // Send back to ~x=300
        dot.x = sectionBounds[1].xMin + 10;
        dot.y = randomBetween(sectionBounds[1].yMin + 10, sectionBounds[1].yMax - 10);
        dot.dx = randomBetween(0.5, 1.0);
        dot.dy = (Math.random() - 0.5) * 0.3;
        return [dot];
      }
    }

    // At x > 1000: loop back to start of section 0
    if (dot.x > 1000) {
      dot.bounds = sectionBounds[0];
      dot.x = sectionBounds[0].xMin + 10;
      dot.y = randomBetween(sectionBounds[0].yMin + 10, sectionBounds[0].yMax - 10);
      dot.dx = randomBetween(0.5, 1.0);
      dot.dy = (Math.random() - 0.5) * 0.3;
      return [dot];
    }

    return [dot];
  });
}



function drawOuterSmallDots() {
  outerSmallDots.forEach(dot => dot.draw(ctx));
}

function moveOuterSmallDots() {
  outerSmallDots.forEach(dot => dot.move());
}

function animate() {
  ctx.clearRect(0, 0, w, h);
  drawOuterFunnel();
  drawOuterSmallDots();
  drawInnerFunnel();
  drawSectionLines();
  drawLabels();
  drawSectionDots();
  moveSectionDots();
  moveOuterSmallDots();
  requestAnimationFrame(animate);
}

initDots();
animate();

window.addEventListener('resize', function() {
  canvas.width = canvas.offsetWidth;
});
</script>


"""
 
st.markdown("<p style='font-size:24px; font-weight: 700; margin-bottom:0; text-align:center;'>AI in the automotive innovation process</p>", unsafe_allow_html=True)
components.html(html_code, height=500)


#---------------------------------------------------------------------------------------------- Introduction -------------------------------------------------------------------------------------------------------------------


st.markdown("<p style='font-weight: 700; font-size:20px; margin-bottom:10; text-align:center;'>AI's impact on the automotive innovation process: </p>", unsafe_allow_html=True)

# Settings
font_size = 30
stretch_y = 4  # Stretch factor

# HTML and CSS
html_code = f"""
<div style="display: flex; justify-content: center; width: 100%;">
    <div style="display: flex; gap: 400px; align-items: center;">
        <div style="font-size: {font_size}px; font-family: monospace; line-height: 1; display: inline-block; 
                    transform: rotate(90deg) scaleY({stretch_y}); transform-origin: center;">}}</div>
        <div style="font-size: {font_size}px; font-family: monospace; line-height: 1; display: inline-block; 
                    transform: rotate(90deg) scaleY({stretch_y}); transform-origin: center;">}}</div>
        <div style="font-size: {font_size}px; font-family: monospace; line-height: 1; display: inline-block; 
                    transform: rotate(90deg) scaleY({stretch_y}); transform-origin: center;">}}</div>
    </div>
</div>
"""

# Render HTML in Streamlit
st.markdown(html_code, unsafe_allow_html=True)


html_code = """
<div style="display: flex; justify-content: center; gap: 100px; margin-top: 50px;">
    <p style="font-size: 20px; text-align: right; font-weight: 700; 
              margin-left: 50px; margin-top: -40px; white-space: nowrap">
        Amplification of idea space
    </p>
    <p style="font-size: 20px; text-align: center; margin-top: -40px; white-space: nowrap; font-weight: 700">
        Efficiency improvements in product development
    </p>
    <p style="font-size: 20px; text-align: center; margin-top: -40px; text-align: center; white-space: nowrap; font-weight: 700; right-margin: 200">
        Optimized market introduction
    </p>
</div>
"""

st.markdown(html_code, unsafe_allow_html=True)


#------------------------------------------------------------------------------------------ All 30 use cases -------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------- All use case descriptions

# Your data
use_case_descriptions = {
    "AI-infused experiments in R&D": "This use case focuses on integrating AI into experimental R&D processes to accelerate discovery and optimize results.",
 
    "AI-infused experiments in R&D": "Madanchian and Taherdoost (2024) analyze how AI-infused experiments unlock new possibilities for enhancing strategic decision-making, cost reduction, and the acceleration of R&D processes. Furthermore, the authors underscore how AI provides researchers with creative ways to enhance operational efficiency and facilitate real-time data analysis and decision-making under uncertainty, enabling companies to adapt to market changes. Companies can improve their organizational performance and innovation capacity by harnessing Machine Learning in R&D, for instance, to convert spoken words into text and integrate implicit and explicit knowledge. Machine Learning models assess R&D product readiness and predict costs, thereby improving commercialization efficiency. An AI-powered decision support system can categorize projects and rank responsible scientists or reviewers using natural language processing and machine learning models. These models enhance reviewer assignment and project evaluation, thus improving the accuracy and efficiency of the review process and R&D project evaluation (Madanchian & Taherdoost, 2024).",
    "AI-powered manufacturing planning in smart factories":"In this use case, the advantages of a virtual smart factory are examined. The virtual smart factory enables companies to identify opportunities for cost reduction in the physical smart factory based on key insights that minimize waste of raw materials, save time, and improve products. Sjödin et al. (2018) highlight the importance for factories to create simulation systems that accurately represent reality, allowing them to test and enhance the actual factory in a digital environment. Virtual factories significantly impact cost reduction by providing insights into resource usage and operational efficiency, thus empowering the generation of ideas for improvement. Companies can develop methods for leveraging data analytics and visualization to facilitate real-time decision-making. Visual representations of the work in the manufacturing plant can assist decision-makers in making improvements to the manufacturing planning. Proactive processes to predict and plan future production can enhance the efficiency of the manufacturing plant.",
    "AI-driven Human-Machine Collaboration in ideation":"Madanchian and Taherdoost (2024) emphasize the advantages of AI in research for generating new knowledge more rapidly. The assistance of AI systems enables automotive companies to concentrate more on creative tasks. AI significantly boosts creativity and efficiency, thereby aiding in the resolution of complex problems. Moreover, AI can personalize the user experience during the idea generation process and enhance decision-making. The authors highlight the crucial impact of AI on R&D by leveraging automation and refining experimental processes. For instance, labs can be outfitted with robots and AI-enhanced automation systems that manage the experimentation environment. This enables scientists to complete experiments more quickly and generate new ideas at an early stage, giving them adequate time to focus on strategic and other creative tasks (Madanchian & Taherdoost, 2024).",
    "AI-enabled idea generation in the Metaverse":"Lin et al. (2024) explore the possibilities that the AI-powered metaverse offers by enhancing how information is extracted and shared between customers and automotive companies to inspire new ideas. The metaverse is a digital world that facilitates communication and collaboration among different users. It can break down barriers to accessing and transforming customer data from various online platforms by broadening the methods through which information can be gathered. Furthermore, the metaverse can elevate these experiences by transforming the current Internet’s 2D visual experience into a 3D experience filled with limitless opportunities for collaboration and interpretation. Users can engage in physical interactions that resemble those in the real world, creating new avenues to exchange valuable information. AI empowers the metaverse to incorporate real-time images, thoughts, and actions, enabling innovative methods of information sharing. This environment also fosters more efficient collaboration among departments to generate new ideas (Lin et al., 2024).",
    "AI-optimized patent analysis":"In this use case, AI is used to identify patent infringement risks and mitigate them. Previous research in risk analysis relies on experts manually examining patent documents to assess and forecast risk levels. However, machine learning algorithms enable objective, quantitative approaches that enhance the validity of patent evaluations (Yang & Yu, 2020)",
    "AI-powered forecasting of the technology life cycle of EVs (S-Curve)":"Chen and Cho (2024) utilize AI-augmented patent analysis to assess the global trend in Electric Vehicle (EV) technology development. They employ this analysis to track EV growth over time according to the technology life cycle known as the S-Curve. The technology life cycle forecasts the progress of technologies and industries, defining its initial stage as the emergence phase and concluding with the decline phase. The technology life cycle is represented as an S-curve, predicting the trajectory and pace of technological advancement (Chen & Cho, 2024). ",
    "AI-enabled bionic digital twin production planning":"The authors employ bionics to enhance AI-driven digital twins in this use case, featuring characteristics of intelligent living beings, such as the intelligence and self-evolution of individual elements and groups of entities. A Digital Twin (DT) is defined as a virtual representation of a physical system. It seamlessly integrates product design and manufacturing with simulations and interactions. The authors utilize this model to identify potential concepts and ideas for upgrading the old welding line of an automotive company, allowing for the simultaneous production of two different vehicle models and brands on a single production line (Li et al., 2021).",
    "AI-infused Human-Robot Collaboration planning":" The authors of this study leverage AI-infused digital twins to generate promising concepts for virtual process flows that integrate human-robot collaboration and ensure efficient automobile manufacturing. These concepts are then used for planning the real manufacturing process (Kousi et al., 2021). ",
    "AI-powered material flow planning":"In this use case, machine learning is harnessed to identify new, efficient ways of material transportation within the manufacturing plant. Building on this foundation, these insights are implemented to develop effective material flows. The planning of the production process in this case is based on selecting the most promising concepts to enable efficient manufacturing processes (Flores-García et al., 2024).",
    "AI-assisted ideation":"Generative Artificial Intelligence (GenAI) is utilized in this use case to enhance creativity and innovation. GAI enables companies to identify key ideas within large volumes of data to kickstart the design of more environmentally friendly cars (Akhtar et al., 2024).",
    "AI-driven interactive collaborative innovation":"This use case focuses on AI-powered collaborative interaction within the omniverse, a virtual platform created by NVIDIA, between various departments of an automotive company and even with customers to co-create a vehicle that meets the demands of all stakeholders involved. NVIDIA Omniverse is an open cloud platform that enables virtual collaboration and real-time simulations, allowing creators and engineers to work together from anywhere in the world, in real time (Lin et al., 2024).",
    "AI-based digital twin for lithium-ion battery development":"In this use case, the authors harness an AI-infused digital twin in the development of lithium-ion batteries to simulate production scenarios, digitally test the batteries, and analyze their quality before ultimately producing them as a physical product (Naseri et al., 2023). ",
    "AI- and Genetic Algorithms-based vehicle design":"This use case examines the application of AI-augmented Genetic Algorithms that allow automotive manufacturers to design and produce vehicles efficiently. Genetic algorithms (GAs) are grounded in the principles of natural selection and evolution, mimicking the processes of genetic variation, selection, and reproduction to incrementally generate and refine potential solutions (Han & Sun, 2024).",
    "AI-augmented visual inspections":"In this use case, an automotive company disassembles used car clutches, breaks them apart, and reuses suitable parts to create products for vehicles. AI-augmented visual inspections of the used clutches assess the quality of reusable components, contributing to the remanufacturing of 95% of used materials (Süße et al., 2023).",
    "AI-optimized scenario engineering":"In this study, the authors analyze the development and training of vehicle software to adapt to various scenarios in a virtual environment using AI models. Li et al. (2023) introduce the framework of scenario engineering for developing accessible and reliable foundation models in the metaverse, defined as scenario engineering enabled foundation models in metaverse (SEEFMM). For instance, ChatGPT-3 and DALL-E are foundation models transforming the applications of artificial intelligence. Foundation models in AI are algorithms trained on vast amounts of data, allowing them to be utilized in numerous applications (Li et al., 2023).",
    "AI-driven design process":"The authors extend their examination of Generative Artificial Intelligence(GenAI) application in the front to the development stage, where GenAI enhances the creation of functional car prototypes while reducing costs in the prototype development phase (Akhtar et al., 2024).",
    "AI- and Bio-inspired Design":"The authors harness AI-infused Bionic design to create a vehicle that leverages biological forms to achieve design that fulfills the desirable engineering requirements of the automotive industry (Deng et al., 2023).",
    "AI-assisted quality control of the bumper warpage":"Chang et al. (2022) examine the use of AI in the injection molding of bumper warpage, making the molding production more intelligent and automated. AI-driven injection molding addresses the challenges of monitoring molding parameters such as temperature, pressure, and speed during the manufacturing process to produce high-quality vehicles that meet stringent safety standards (Chang et al., 2022).",
    "AI-enabled predictive maintenance":"Oh and Kim (2024) achieve their aim in this study of reducing the costs associated with aging machines and conventional maintenance techniques by harnessing an AI-based machine failure management system that performs predictive maintenance. Predictive Maintenance (PdM) systems forecast replacement cycles, thereby improving productivity (Oh & Kim, 2024).",
    "AI-optimized braking system test":"In this study, the authors harness AI to assess the braking system in a virtual environment, predicting the interdependencies among the various subsystems and deriving the performance parameters of the entire system (Aleksendric & Duboka, 2008).",
    "AI-based identification of consumer adoption stage":"This study analyzes the fundamental drivers of Electric Vehicle (EV) interest and aims to identify the potential next wave of EV customers using machine learning models. It investigates the upcoming mainstream EV market by harnessing a machine learning method to uncover demographic and socio-economic attributes, as well as car and mobility preferences, in five Nordic countries: Denmark, Finland, Iceland, Norway, and Sweden, based on a dataset of 5067 survey participants. The research reveals six consumer clusters based on demographic and socio-economic attributes, mobility, vehicle preferences, and interests in EVs and vehicle-to-grid technologies (Zarazua De Rubens, 2019).",
    "AI-powered marketing campaign":"This use case employs AI to analyze customer data and online platforms for creating marketing campaigns tailored to customers’ preferences. Toyota serves as an inspiration since the company harnessed AI to develop a marketing campaign for the launch of a new vehicle model. Initially, potential customers were asked to submit data regarding their preferences. This data provided by the target group was analyzed. The AI system was then trained with texts and videos from the video platform YouTube to identify the preferred styles of target customers that matched the data they provided. As a result, the company created thousands of creative advertisements customized for the different profiles of ad recipients.",
    "AI-driven relationship marketing":"This study analyzes how organizations can harness AI to adapt to a dynamic market characterized by constantly changing customer needs and to build strong customer relationships. The authors examine how AI improves customer relationships throughout the entire customer journey (Roy et al., 2025).",
    "AI-assisted customer service in after-sales":"Sliż (2024) uncovers the potential of the large language model ChatGPT to streamline automotive after-sales. The study reveals that ChatGPT can enhance the efficiency of service reception, check-out, repair and maintenance, making them more customer-centric and efficient. GPT’s tools may transform traditional customer service in the automobile industry by enabling quick and precise responses to customer requests and leveraging intelligent chatbots (Sliż, 2024) .",
    "AI-enabled battery monitoring":"In this use case, the AI-powered Digital Twin is utilized to create a link between a virtual lithium-ion battery of an electric vehicle (EV) and the real, physical battery, enabling the monitoring of its condition and performance throughout its entire lifetime. This capability allows automotive companies to analyze the battery’s performance in customer use and identify areas for improvement (Naseri et al., 2023).",
    "AI-assisted staff training":"Li et al. (2023) focus on the implementation of AI-assisted staff training for customer services in the metaverse. The metaverse provides a multisensory learning experience in an immersive environment. The automotive industry can leverage the AI-powered metaverse to create virtual-real environments for staff training, allowing employees to practice essential skills for their profession (Li et al., 2023).",
    "AI-driven predictive quality models for customer defects":"The goal of this study is to explore automotive customer complaint data and the standardized procedures for handling customer data, generating real-time insights, and leveraging AI to predict quality errors, customer defects, and maintenance needs. The study examines the integration of AI to enhance operational performance and address the high costs and complexity associated with quality complaint analysis (Silva et al., 2024).",
    "AI-powered customer satisfaction analysis":"Liang et al. (2024) harness AI in this study to understand how customers receive a newly released vehicle, gaining deeper insights into customer satisfaction during the post-purchase phase.  ",
    "AI-driven competition analysis":"AI-driven competition analysis enables companies to strategically position themselves in a given market and identify where they could or wish to be in the future. Liu et al. (2020) employ machine learning models on favorite data to analyze the asymmetric competitive market.",
    "AI-driven vehicles sales prediction":"Zhang et al. (2022) leverage deep learning to develop a sales prediction model for the automotive industry based on online opinions and the online search index. The authors discover that deep learning-driven vehicle sales predictions are significantly more accurate than traditional vehicle sales forecasting methods."
}

# Heading
st.markdown("<p style='font-weight: 700; font-size:22px; margin-top:3em; text-align:center;'>AI use cases in automotive</p>", unsafe_allow_html=True)

# Styling
st.markdown("""
<style>
.container {
    display: flex;
    justify-content: center;
    gap: 40px;
    flex-wrap: wrap;
}
.column {
    flex: 1;
    min-width: 300px;
    max-width: 350px;
}
.details-box-1 {
    background-color: #e37852;
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 10px 15px;
    margin-bottom: 15px;
    font-family: sans-serif;
}
.details-box-2 {
    background-color: #FFA07A;
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 10px 15px;
    margin-bottom: 15px;
    font-family: sans-serif;
}
.details-box-3 {
    background-color: #FFC4A6;
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 10px 15px;
    margin-bottom: 15px;
    font-family: sans-serif;
}
details summary {
    font-weight: bold;
    cursor: pointer;
    outline: none;
}
.column-title {
    font-weight: bold;
    font-size: 20px;
    margin-bottom: 15px;
    text-align: center;
    color: black;
}
</style>
""", unsafe_allow_html=True)

titles = list(use_case_descriptions.keys())
assert len(titles) >= 30, "You must have at least 30 use cases"

column_html = """
<div class='container'>

  <div class='column'>
    <div class='column-title'>Front end use cases</div>
""" + "".join([
    f"<div class='details-box-1'><details><summary>{titles[i]}</summary><p>{use_case_descriptions[titles[i]]}</p></details></div>"
    for i in range(0, 10)
]) + """
  </div>

  <div class='column'>
    <div class='column-title'>Development use cases</div>
""" + "".join([
    f"<div class='details-box-2'><details><summary>{titles[i]}</summary><p>{use_case_descriptions[titles[i]]}</p></details></div>"
    for i in range(10, 20)
]) + """
  </div>

  <div class='column'>
    <div class='column-title'>Market introduction use cases</div>
""" + "".join([
    f"<div class='details-box-3'><details><summary>{titles[i]}</summary><p>{use_case_descriptions[titles[i]]}</p></details></div>"
    for i in range(20, 30)
]) + """
  </div>

</div>
"""

st.markdown(column_html, unsafe_allow_html=True)


#-------------------------------------------------------------------------------------------- Table for category, dimension and attributes -----------------------------------------------------------------------------------------------------
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
 
 
#---------------------------------------------------------------------------------------------------------- Analysis table ----------------------------------------------------------------------------------------------------------------------
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
    "Cost": [2, 2, 0, 0, 0, 0, 2, 1, 2, 2, 0, 2, 2, 0, 2, 2, 0, 0, 2, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0],
 
    "Customer Segments": [0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2],
    "Value Proposition": [2, 0, 0, 2, 0, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 0, 2, 2, 2, 0, 0, 2, 2, 2],
    "Value Chain": [2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0],
    "Revenue Model": [0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2],
 
    "Product Innovation": [2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 1, 0, 0, 0, 2, 0, 2],
    "Process Innovation": [1, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 2, 0, 2, 2, 2, 2, 0, 2, 2],
    "Business Model Innovation": [0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2],

    "Exploitation": [0, 2, 0, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0],
    "Exploration": [2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 0, 0, 2, 0, 2, 2, 2, 2],
   
    "Automaton": [2, 0, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    "Helper": [1, 0, 1, 2, 2, 2, 0, 0, 0, 0, 2, 1, 2, 0, 2, 2, 1, 2, 0, 2, 1, 0, 2, 2, 0, 0, 0, 2, 2, 2],
    "Partner": [2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 1, 0, 2, 2, 2, 0, 0, 0],
 
    "Machine Learning": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    "Deep Learning": [2, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2],
    "Artificial Neural Networks": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Natural Language Processing": [2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 0, 2],
    "Computer Vision": [0, 0, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    "Robotics": [0, 0, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 
    "Descriptive": [1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0],
    "Diagnostic": [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
    "Predictive": [2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 0, 0, 2, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 0, 2],
    "Prescriptive": [0, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 2, 0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
 
    "Description/ Summary": [1, 0, 0, 2, 2, 0, 0, 0, 1, 1, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0],
    "Clustering": [0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2],
    "Classification": [2, 0, 0, 0, 2, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    "Dependency Analysis": [1, 1, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    "Regression": [2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 0, 0, 2, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 0, 2],
 
    "Customer Data": [0, 1, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2],
    "Machine Data": [2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 2, 2, 2, 2, 2, 2, 2],
    "Business Data (Internal Data)": [2, 2, 1, 0, 2, 2, 2, 2, 2, 2, 2, 0, 1, 0, 0, 1, 0, 0, 2, 1, 0, 1, 1, 2, 2, 2, 0, 0, 0, 2],
    "Market Data": [2, 1, 1, 1, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2],
    "Public & Regulatory Data": [2, 0, 0, 0, 2, 2, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 1, 0, 0, 2, 2, 2, 2, 2, 0, 2],
    "Synthetic Data": [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 
    "Front End": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
    "Development": [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    "Market Introduction": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
 
    "R&D": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 1, 0, 2, 2, 2, 2],
    "Manufacturing": [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0, 0, 1, 0, 1, 1, 2, 0, 0, 1],
    "Marketing & Sales": [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1, 0, 0, 0, 2, 2, 2],
    "Customer Service": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1]
}
 
 
analysis_table = pd.DataFrame(analysis_table_data)
analysis_table.set_index("Use Case", inplace=True)
 

 
# ------------------------------------------------------------------------------------------------------- Session state ------------------------------------------------------------------------------------------------------------------------
if "selected" not in st.session_state:
 st.session_state.selected = set()
 
if "attr_multiselect" not in st.session_state:
 st.session_state.attr_multiselect = []
 
# Initialize selected_attributes from session state
selected_attributes = list(st.session_state.selected)
 
 
 
#---------------------------------------------------------------------------------------------------------- First drop down list for selectable attributes -------------------------------------------------------------------------------------

if "attr_multiselect" not in st.session_state:
    st.session_state.attr_multiselect = []
if "selected" not in st.session_state:
    st.session_state.selected = set()



attribute_columns = list(analysis_table.columns)

# Initialize session state
if "attr_multiselect" not in st.session_state:
    st.session_state.attr_multiselect = []
if "selected" not in st.session_state:
    st.session_state.selected = set()

# Create container for the multiselect
multiselect_container = st.container()

with multiselect_container:
    st.markdown(
        """
        <p style="font-size:18px; font-weight:bold; color:black;margin-bottom: 0px; margin-top: 3em;">
            Select as many attributes as you like from the dropdown list below to identify relevant AI use cases and clusters in automotive. The more attributes you choose, the more accurately the most relevant AI use case will be displayed. If you select fewer than three attributes, please refer to the section with additional relevant use cases further down this page.
        </p>
        """,
        unsafe_allow_html=True,
    )

    selected_attributes = st.multiselect(
        "",
        attribute_columns,
        default=st.session_state.attr_multiselect,
        key="attr_multiselect"
    )

# Only update st.session_state.selected if it changed
if set(selected_attributes) != st.session_state.selected:
    st.session_state.selected = set(selected_attributes)
 
 
#--------------------------------------------------------------------------------------------------------- Table layout ------------------------------------------------------------------------------------------------------------------------
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
 
 
#----------------------------------------------------------------------------------------------- Python, Javascript, Streamlit Communication ---------------------------------------------------------------------------------------------------
 
#------------------ Javascript for interactivity ----------------------------------
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
 
#-------------------------- Handle messages from Javascript --------------------
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
 
 
#--------------------------- JavaScript to handle Streamlit communication--------
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
 
 
 
#------------------------------------------------------------------------------------------ Top use case selection and display ------------------------------------------------------------------------------------------------------------------
 
 
# ---------------------------- Calculate and show top use case -----------------------
if selected_attributes:
   summed = analysis_table[selected_attributes].sum(axis=1)
   top_use_case = summed.idxmax()
 
   # Combine the title and the paragraph with spacing
   use_case_info = f"<b>{top_use_case}</b><br>{use_case_descriptions.get(top_use_case, '')}"
 
   # Display top use case inside a styled box
   st.markdown(
       f"""
       <div style="margin-top: 1em;">
       <label style="font-weight: 700; color: #000;"> Most relevant AI Use Case </label><br>
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
   st.info("Please select the attributes above to display relevant information.")
 

#------------------------------------------------------------------------------------------------- Top use case graph display ------------------------------------------------------------------------------------------------------------------
 
st.markdown(
   "<h3 style='font-size:18px; font-weight:700; margin-bottom:0; margin-top:2em; text-align:center;'>Significance levels of attributes for the most relevant AI use case in automotive, based on the user's selection</h3>",
   unsafe_allow_html=True
)
 
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
       range=[0, 2],
       title_font=dict(family='Arial Bold', color='black'),
       tickfont=dict(color='black'),
       
   )
   fig.update_xaxes(
   title_text="Attributes",
   automargin=True,
   title_standoff=30,  # Lower value brings title closer to axis
   tickangle=50,
   title_font=dict(family='Arial Bold', color='black'),
   tickfont=dict(color='black'),
)
   fig.update_layout(
   margin=dict(t=0, b=40),
   height=500
)
   st.plotly_chart(fig, use_container_width=True)
  
#-------------------------------------------------------------------------------------------------------- Cluster Analysis --------------------------------------------------------------------------------------------------------------------
 
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
   
   "AI- and Genetic Algorithms-based vehicle design": "Cluster 2: AI-optimized Design and Quality in Automotive",
   "AI-augmented visual inspections": "Cluster 2: AI-optimized Design and Quality in Automotive",
   "AI-optimized scenario engineering": "Cluster 2: AI-optimized Design and Quality in Automotive",
   "AI-driven design process": "Cluster 2: AI-optimized Design and Quality in Automotive",
   "AI- and Bio-inspired Design": "Cluster 2: AI-optimized Design and Quality in Automotive",
   "AI-assisted quality control of the bumper warpage": "Cluster 2: AI-optimized Design and Quality in Automotive",
   "AI-optimized braking system test": "Cluster 2: AI-optimized Design and Quality in Automotive",
   
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
 
 
#---------------- Dictionary mapping clusters to detailed information -------------------------------------
cluster_details = {
   "Cluster 1: Ideation and Intelligent Planning in Automotive": (
       """Use Cases in Cluster 1:

       - AI-powered manufacturing planning in smart factories  
       - AI-driven Human-Machine Collaboration in ideation 
       - AI-enabled bionic digital twin production planning
       - AI-infused Human-Robot Collaboration planning 
       - AI-powered material flow planning 
       - AI-based digital twin for lithium-ion battery development 
       - AI-enabled predictive maintenance
       - AI-driven predictive quality models for customer defects 
       
       This cluster encapsulates the application of AI in ideation and planning, simulation, and optimization of automotive manufacturing and maintenance systems. These use cases reflect a forward-looking shift towards digitized, intelligent, and resilient production environments, where AI serves as a partner in ideation and continuous innovation. 
       """
     
   ),
   "Cluster 2: AI-optimized Design and Quality in Automotive": (
       """Use Cases in Cluster 2:

       - AI- and Genetic Algorithms-based vehicle design"
       - AI-augmented visual inspections
       - AI-optimized scenario engineering 
       - AI-driven design process
       - AI- and Bio-inspired Design 
       - AI-assisted quality control of the bumper warpage 
       - AI-optimized braking system test

       "This cluster depicts the unification of AI-driven creativity with engineering rigor. The use cases illustrate how AI can enhance design intelligence, minimize waste through quality control, and simulate complex systems, all of which are essential for innovation in a competitive and sustainability-driven automotive market. 
       """
   ),
   "Cluster 3: AI-driven Customer-Centric Innovation in Automotive": (
       """Use cases in Cluster 3:

        - AI-enabled idea generation in the Metaverse
        - AI-driven interactive collaborative innovation 
        - AI-based identification of consumer adoption stage 
        - AI-powered marketing campaign 
        - AI-driven relationship marketing
        - AI-powered customer satisfaction analysis 
        - AI-driven competition analysis
        
        This cluster comprises AI applications that aim to enhance customer-centricity, thereby establishing a strong and long-term relationship with customers that is strategically beneficial. The cluster illustrates how AI fosters deeper engagement with consumers, transforms marketing and ideation processes, and supports strategic innovation tailored to customer expectations. 
        """       
   ),
   "Cluster 4: AI in Automotive Customer Service": (
       """Use cases in Cluster 4:

        - AI-assisted customer service in after-sales"
        - AI-enabled battery monitoring 
        - AI-assisted staff training
        
        This cluster demonstrates how AI can enhance internal operations by supporting service quality, improving battery longevity, and transforming training methodologies. These cases highlight the strategically crucial roles AI plays in the post-purchase stage, supporting the workforce and sustaining product value and service excellence over time.
        """
   ),
   "Cluster 5: AI in Strategic Forecasting": (
       """Use cases in Cluster 5:

        - AI-infused experiments in R&D
        - AI-optimized patent analysis
        - AI-powered forecasting of the technology life cycle of EVs (S-Curve)
        - AI-assisted ideation
        - AI-driven vehicles sales prediction 
        
        This cluster represents the strategic brain of the AI use case ecosystem in the automotive industry. It showcases how AI enhances long-term innovation capabilities, facilitates the generation of novel ideas, and enables companies to confidently anticipate future technological developments.
        """       
   )
}
 
#-------------------------------- Selection of Clusters ------------------------------------------------
 
if top_use_case:
   cluster_name = use_case_to_cluster.get(top_use_case, "Unknown Cluster")
   cluster_info = cluster_details.get(cluster_name, "Detailed information about this cluster is not available.")
 
   st.markdown(
       f"""
       <div style="margin-top: 1em;">
           <label style="font-weight: 700; color: #000;">Cluster details for the most relevant AI use case</label><br>
           <div style="
               width: 100%;
               background-color: #F5F5F5;
               color: #000;
               padding: 10px;
               border: 1px solid #000;
               border-radius: 8px;
               font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
               font-size: 14px;
           ">
               <span style="font-weight:bold;">{cluster_name}</span><br>
               <span>{cluster_info}</span>
           </div>
       </div>
       """,
       unsafe_allow_html=True
   )
else:
   st.info("Please select the attributes above to display relevant information.")
 
 #----------------------------------------------------------------------------------------------- Graph of top use case cluster ---------------------------------------------------------------------------------------------------------------

if top_use_case:
    # Step 1: Find the cluster for the selected top use case
    cluster_name = use_case_to_cluster.get(top_use_case)

    if cluster_name:
        # Step 2: Get all use cases in that cluster
        cluster_use_cases = [
            use_case for use_case, cluster in use_case_to_cluster.items()
            if cluster == cluster_name
        ]

        # Step 3: Filter the analysis table to include only those use cases
        cluster_df = analysis_table.loc[
            analysis_table.index.intersection(cluster_use_cases)
        ]

        if not cluster_df.empty:
            # Step 4: Calculate average values for each attribute
            avg_values = cluster_df.mean()

            # Step 5: Create the bar chart
            fig = go.Figure(data=[
                go.Bar(
                    x=avg_values.index,
                    y=avg_values.values,
                    marker_color=[
                        '#92D050' if v >= 1.5 else '#FFD966' if v >= 0.5 else '#D9D9D9'
                        for v in avg_values.values
                    ],
                )
            ])

            # Step 6: Format the chart
            fig.update_yaxes(
                tickvals=[0, 1, 2],
                ticktext=["Low", "Moderate", "High"],
                title_text="Average Significance Level",
                range=[0, 2],
                title_font=dict(family='Arial Bold', color='black'),
                tickfont=dict(color='black'),
            )
            fig.update_xaxes(
                title_text="Attributes",
                tickangle=50,
                title_font=dict(family='Arial Bold', color='black'),
                tickfont=dict(color='black'),
                automargin=True,
                title_standoff=30
            )
            fig.update_layout(
                title=f"Average Attribute Significance for {cluster_name}",
                title_font=dict(family='Arial Bold', size=18, color='black'),
                margin=dict(t=150, b=80),
                title_x=0.2,
                height=500
            )

            # Step 7: Show chart
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No data found for the cluster's use cases.")
    else:
        st.warning("Selected use case does not belong to a known cluster.")

# -------------------------------------------------------------------------------------------------- Calculate and show other relevant use case --------------------------------------------------------------------------------------------------
if selected_attributes:
   summed = analysis_table[selected_attributes].sum(axis=1)
   top_6_use_cases = summed.nlargest(6).index[1:]  # Get indices of top 6 use cases
 
   # single string for all use cases, separated by <br><br>
   use_cases_info = ""
   for use_case in top_6_use_cases:
       description = use_case_descriptions.get(use_case, "")
       use_cases_info += f"<b>{use_case}</b><br>{description}<br><br>"
 
   # Strip the trailing <br><br> for a clean finish
   use_cases_info = use_cases_info.rstrip("<br><br>")
 
   st.markdown("---")
   st.markdown(
       f"""
       <div style="margin-top: 1em;">
           <label style="font-weight: 700; color: #000;"> Other relevant AI Use Cases</label><br>
           <div style="
               background-color: #ff8b3d;
               padding: 10px;
               border-radius: 8px;
               border: 1px solid #000;
               font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
               font-size: 14px;
               color: #000;
               white-space: pre-wrap;
           ">{use_cases_info}</div>
       </div>
       """,
       unsafe_allow_html=True
   )
   
else:
   top_6_use_cases = None  # Default value if no attributes are selected
   st.info("Please select the attributes above to display relevant information.")
