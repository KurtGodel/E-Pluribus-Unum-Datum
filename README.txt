
Project Name: E Pluribus Unum Datum
Group Members: Ben Wedin & Thomas Redding
Full URL: http://thacker.mathcs.carleton.edu/cs257/reddingt/cs257_webapp/index.html
Note: The website is no longer online and also consisted of a SQL database




Features:
1. User can get state-by-state data for a variety of statistics
2. User can get a single state's data across a range of years
    for a variety of statistics
3. User can get a line graph of a statistic for a specified state over time
4. User can get a bar chart showing how a statistic differs
    among the 50 states for a given year
5. User can get a color-coded map showing how a statistic differs
    among the 50 states for a given year
6. User can download the graphic





This website is made to allow the user to generate visual representations of
state data. In order to understand how it functions, the reader should
understand HTML5, JavaScript (including ajax), CSS, and Python.

You should use the two flow charts provided in the "Development Docs" directory
as a reference point. Because of the event-based nature of the website, it can
be less intuitive to follow this code, but using the flow charts provided will
make it much easier.

"index.html" is webpage that loads when the user enteres the url. It imports
"javascript.js" (which is in charge of communications with the server),
"drawer.js" (which is in charge of drawing the charts), and style.css (which
adds some stylistic changes to the webpage).

"javascript.js" calls "webapp.py" whenever it requires data from the server.
"webapp.py" examines the request and calls "data_source.py" to request the
required data and send it back to the user.

"data_source.py" acts as an interface with the sql database.
