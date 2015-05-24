#!/usr/bin/python
# -*- coding: utf-8 -*-
"""A web application that both displays a form and the result of submitting to
the form.  This program demonstrates a couple simple-minded techniques for
presenting the form and sanitizing user input.

The program does one of two things, depending on its CGI parameters.

1. If no statistic is selected, empty text is given.

2. If a statistic is selected, some fact about the statistic and a summary
    of the user's request.

It's structured to separate out the front-end presentation (stored in
template.html) from the logical components of the application.

By Thomas Redding and Ben Wedin, 2015;
    adapted from Jadrian Miles, 2015; adapted from Jeff Ondich's sample, 2012.
"""

import cgi
import cgitb
import re
from data_source import *

cgitb.enable()

dataSource = DataSource()

def main():
    print 'Content-type: text/html\r\n\r\n'

    parameters = getCgiParameters()

    #Create cursor and lookup dictionaries used by dataSource to make queries
    dataSource.createCursorAndLookups()

    # print the GET request
    print parametersToString(parameters)

    print "\r\n"

    # print the csv-formated response
    print respondToRequest(parameters['requestType'],
                         parameters['statistic'],
                         parameters['summary'],
                         parameters['state'],
                         parameters['year'],
                         parameters['singleyear'],
                         parameters['startyear'],
                         parameters['endyear'])


# converts the dictionary of parameter values into a string with format
# key1=value1&key2=value2&key3=value3...
def parametersToString(parameters):
    """Converts list of CGI parameters to a string of
    name=value separated with &"""
    outputStr = ""
    for key in parameters:
        outputStr += key
        outputStr += "="
        outputStr += parameters[key]
        outputStr += "&"
    return outputStr[:-1]


def respondToRequest(requestType, statistic, summary, state, year, singleyear,
        startyear, endyear):
    """Calls the appropriate method with CGI parameters to
    dataSource according to the request type."""
    outputStr = ""
    if(requestType == "getListOfRegions"):
        outputStr += dataSource.getListOfStates()
    elif(requestType == "getListOfStatistics"):
        outputStr += dataSource.getListOfStatisticNames()
    elif(requestType == "getData"):
        if(summary == "state map" or summary=="bar chart"):
            outputStr += dataSource.getDataForSpecificYear(statistic,
                singleyear, "State-by-state")
        elif(summary == "line graph"):
            outputStr += dataSource.getDataForYearRange(statistic,
                startyear, endyear, state)
        else:
            outputStr += "error - invalid 'summary' value"
    else:
        outputStr += "NA"
    return outputStr

def getCgiParameters():
    """Returns a dictionary of sanitized, default-populated values for the CGI
    parameters that we care about.
    """
    form = cgi.FieldStorage()
    parameters = {'statistic':'', 'summary':'', 'state':'',
        'year':'', 'singleyear':'', 'startyear':'', 'endyear':''}

    if 'requestType' in form:
        parameters['requestType'] = sanitizeUserInput(
        form['requestType'].value)


    if 'statistic' in form:
        parameters['statistic'] = sanitizeUserInput(
        form['statistic'].value)

    if 'summary' in form:
        parameters['summary'] = sanitizeUserInput(
        form['summary'].value)

    if 'state' in form:
        parameters['state'] = sanitizeUserInput(form['state'].value)

    if 'year' in form:
        parameters['year'] = sanitizeUserInput(form['year'].value)

    if 'singleyear' in form:
        parameters['singleyear'] = sanitizeUserInput(form['singleyear'].value)

    if 'startyear' in form:
        parameters['startyear'] = sanitizeUserInput(form['startyear'].value)

    if 'endyear' in form:
        parameters['endyear'] = sanitizeUserInput(form['endyear'].value)

    return parameters


def sanitizeUserInput(s):
    """Strips out scary characters from s and returns the sanitized version.
    """
    # We talked briefly in class about SQL injection.  One common "attack
    # vector" is through CGI parameters, either GET or POST.  If we use the
    # strings we get from the user to construct a database query, then we need
    # to be very careful that the user can't trick us into executing arbitrary
    # commands on our database.  There's actually a great XKCD comic about
    # this, along with a good explanation of the principle:
    #   http://www.explainxkcd.com/wiki/index.php/327:_Exploits_of_a_Mom
    #
    # There are better ways to sanitize input than the following, but this is a
    # very simple example of the kind of thing you can do to protect your
    # system from malicious user input. Unfortunately, this example turns
    # "O'Neill" into "ONeill", among other things.
    #
    # One thing to keep in mind about input sanitization is that it must happen
    # on the SERVER SIDE.  Clients who want to mess with your app can always
    # find ways to send it bogus data; you need to be prepared to receive ANY
    # junk they might come up with, and handle it safely.

    # Only keep alphanumeric characters; remove all others
    chars_to_remove = ";,\\/:'\"<>@"
    s = re.sub(r'[^a-zA-Z0-9]',' ', s)
    return s


def indent(s, k):
    """Returns an indented copy of the string, with 4*k spaces prepended to
    each line.
    """
    return "\n".join([" "*(4*k) + line for line in s.splitlines()])


if __name__ == '__main__':
    main()
