# Introduction
This is a Flask based web application for MyFitnessPal users that allows them to analyze and visualize their nutrition and meal data through <a href="https://github.com/coddingtonbear/python-myfitnesspal">coddingtonbear's python-myfitnesspal API</a>. As of now the analysis is straightforward but over time it will scale to include more detailed data insights to help users reach their fitness goals.

# Overview
Nutrition.py is a wrapper library for the unofficial MFP API. This file includes commonly used functions such as `calculate_average_daily` and `calculate_average_macro_ratio` and more. This is where the majority of the MyFitnessPal data analysis will occur and as the application scales I'll add more functionality as needed. The server backend runs Flask based and can be found in Server.py. Frontend is an implementation of the clean Bootstrap 3 theme <a href="https://github.com/puikinsh/gentelella">Gentelella</a>.

# Current state
Planning is complete and the backend in Nutrition.py is about 90% fleshed out. Currently working on building the HTML pages and CSS. Also grappling with the most secure way to deal with user authentication considering I would not want to store MyFitnessPal passwords on the server so I'm looking into <a href="https://github.com/maxcountryman/flask-login">Flask-Login</a> for user session management.

# TODO
<ul>
  <li>Implement 2 more functions in Nutrition.py</li>
  <li>Complete HTML and CSS changes to Gentelella</li>
  <li>Research the best way to implement a Single Page Application</li>
  <li>Implement a Single Page Application</li>
</ul>
