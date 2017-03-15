# Introduction
This is a data analysis library and Flask based web application for MyFitnessPal users that allows them to analyze and visualize their nutrition and meal data through <a href="https://github.com/coddingtonbear/python-myfitnesspal">coddingtonbear's python-myfitnesspal API</a>. Current features include plots to visalize your calorie and macronutrient consumption over a set period of time, highest, average, and lowest value identification, and intelligent analysis that only selects completed days by observing values and how they relate to the user's overall consumption. Over time it will scale to include more detailed data insights to help users reach their fitness goals.

# Overview
- Nutrition.py is a playground library for the unofficial MFP API. This file includes commonly used functions such as `calculate_average_daily` and `calculate_average_macro_ratio` and more. This is where the majority of the MyFitnessPal data analysis will occur and as the application scales I'll add more functionality as needed. New functions are tested and developed here and will be
transfered to `server.py` upon completion.
- The server backend runs Flask based and can be found in Server.py.
- Frontend is an implementation of the clean Bootstrap 3 theme <a href="https://github.com/puikinsh/gentelella">Gentelella</a> and uses JQuery for
sending AJAX responses to the Flask REST API.

# Current state
I'm researching more detailed data analysis techniques and looking into implementing
more readable insights. For instance, instead of simply listing ``Average calories
for past month: 3300``, I want to be able to generate custom insights like this:

 ``Wow! You've reached your calorie goals everyday this past week because you've been eating
a much larger breakfast compared to last week. Keep it up!``

# TODO
- Cleanup MongoDB querying.
- Look into Redis for data caching.
- Fix JQuery bug where pressing submit on a modal doesn't automatically close it.
