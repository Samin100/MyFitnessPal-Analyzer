# MyFitnessPal-Analyzer
Tools for analyzing MyFitnessPal data through coddingtonbear's unofficial MFP API. Once the backend has been fleshed out I may develop it into a web application for others to use.

# Introduction
This is the start of a simple web application that imports a user's MyFitnessPal data and provides insights such as:
<ol>
  <li>calorie averages (weekly/monthy/custom period)</li>
  <li>most common meals</li>
  <li>highest/lowest calorie days</li>
  <li>macronutrient ratios</li>
  <li>nutritional analysis (actual vs. ideal nutrition) -> open to interpretation</li>
</ol>

# Frameworks, APIs, and tools
<ol>
  <li>The backend will be written in Python and use coddingtonbear's API found at https://github.com/coddingtonbear/python-myfitnesspal.</li>
  <li>In addition, charting libraries will be required to plot the nutrition data. For the web app portion, maybe Flask or Django. I'm learning towards Django since we'll require user authentication for their MFP account.</li>
</ol>
