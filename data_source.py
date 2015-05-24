#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path
import sys
import psycopg2
import cgitb
from dbtest import *
cgitb.enable()

'''A class that acts as an interface between the server and the database,
and returns requests into a CSV format.'''
class DataSource:

    def __init__(self):
        """Constructor for the DataSource database interface class.
        """
        pass

    def createCursorAndLookups(self):
        """Creates the cursor and lookup dictionaries that DataSource uses.
        The cursor is used to make queries to the database, and the lookup
        dictionaries convert from between IDs in the database and the names
        of actual regions or statistics."""

        USERNAME = 'reddingt'
        DB_NAME = 'reddingt'
        PASSWORD = ''

        # Step 1: Read your password from the secure file.
        try:
            f = open(os.path.join('/cs257', USERNAME))
            PASSWORD = f.read().strip()
            f.close()
        except:
            print "(Error - password not found)"
            sys.exit()

        # Step 2: Connect to the database.
        try:
            db_connection = psycopg2.connect(user=USERNAME,
                                     database=DB_NAME,
                                     password=PASSWORD)
        except:
            print "(Error - failed to connect to database)"
            sys.exit()

        #create cursor and lookup dictionaries
        try:
            self.cursor = db_connection.cursor()
            self.region_dictionary = {}
            self.region_dictionary_flip = {}
            self.cursor.execute("""SELECT * FROM regionlookup;""")
            for row in self.cursor:
                self.region_dictionary[row[0]] = row[1]
                self.region_dictionary_flip[row[1]] = row[0]
            self.stat_dictionary = {}
            self.cursor.execute("""SELECT * FROM statlookup;""")
            for row in self.cursor:
                self.stat_dictionary[row[1]] = row[0]

        except:
            sys.exit()


    def verifyQueryParameters(self,statistic, year_1, year_2, state):
        if (year_1=="NA" or year_2=="NA" or statistic=="NA" or state=="NA"):
            return "ERROR: Incomplete or invalid form"
        try:
            int(year_1)
            int(year_2)
        except:
            return "ERROR: Year inputs must be numbers"
        try:
            stat_id = self.stat_dictionary[statistic]
        except:
            return "ERROR: Invalid statistic name"
        try:
            if state!="State-by-state":
                state_id = self.region_dictionary[state]
        except:
            return "ERROR: Invalid state/region name"

        return "All parameters valid"

    def getDataForYearRange(self, statistic, start_year, end_year, state):
        ''' Gets data from database, given a statistic name
            (string), start year (string), and end
            year (string) for some state/region.'''

        #Returns error message if given invalid parameters
        verify_params = self.verifyQueryParameters(statistic,
                               start_year, end_year, state)
        if (verify_params!="All parameters valid"):
           return verify_params
        if (start_year != end_year) and state=="State-by-state":
            return "ERROR: Cannot get data for all states for multiple years"

        state_id = self.region_dictionary[state]
        stat_id = self.stat_dictionary[statistic]
        start_year = int(float(start_year))
        end_year = int(float(end_year))

        years = self.getMaxYearRangeInteger(statistic)

        #Gives single year data if years repeat or are otherwise atypical
        if start_year > years[1]:
            start_year = years[1]
        if end_year < years[0]:
            end_year = years[0]
        if (start_year == end_year) or (start_year > end_year):
            return self.getDataForSpecificYear(statistic, start_year, state)

        #Data for year range
        else:
            output_string = "State,Year," + statistic
            self.cursor.execute("""SELECT year,value
                FROM statistics WHERE statistic_id = %s AND year >= %s
                AND year <= %s
                AND region_id = %s """, (stat_id,start_year,end_year,state_id))
            for row in self.cursor:
                output_string += "\r\n"
                output_string += state + "," + str(row[0]) + "," + str(row[1])
            return output_string


    def getDataForSpecificYear(self, statistic, single_year, state):
        ''' Gets data for some statistic parameter (string) given a
            start and end year (strings) for some state/region
            or gives all regions if state = "State-by-state". '''

        #Returns error message if given invalid parameters
        verify_params = self.verifyQueryParameters(statistic,
                           single_year, single_year, state)
        if (verify_params!="All parameters valid"):
           return verify_params

        output_string =""
        stat_id = self.stat_dictionary[statistic]

        # Provides data if year range parameters are atypical
        year_range = self.getMaxYearRangeInteger(statistic)
        single_year = int(float(single_year))
        if single_year < year_range[0]:
           single_year = year_range[0]
        elif single_year > year_range[1]:
           single_year = year_range[1]

        #Single state/region
        if state!="State-by-state":
            output_string += "State,Year," + statistic
            state_id = self.region_dictionary[state]
            self.cursor.execute("""SELECT year,value
                FROM statistics WHERE statistic_id = %s AND year = %s
                AND region_id = %s """, (stat_id,single_year,state_id))
            for row in self.cursor:
                output_string += "\r\n"
                output_string += state + "," + str(row[0]) + "," + str(row[1])

        #Gives data for all regions (except "United States")
        else:
            output_string += "State,Year," + statistic
            self.cursor.execute("""SELECT region_id,year,value
                FROM statistics WHERE statistic_id = %s
                AND year = %s ORDER BY region_id""", (stat_id,single_year))
            for row in self.cursor:
                if row[0]!=0:
                    output_string += "\r\n"
                    state_id = self.region_dictionary_flip[row[0]]
                    output_string += state_id + ","
                    output_string += str(row[1]) + "," + str(row[2])

        return output_string

    def getMaxYearRange(self, statistic):
        ''' Gives start and end years that the database
            has data for a given statistic (in CSV form). '''

        self.cursor.execute("""SELECT start_year,end_year
            FROM statlookup WHERE statistic_name = %s""", (statistic,))
        years = self.cursor.fetchone()
        output_string = "Start Year, End Year"
        output_string += "\r\n"
        output_string += str(years[0]) + "," + str(years[1])
        return output_string

    def getMaxYearRangeInteger(self, statistic):
        ''' Gives start and end years that the database
            has for a given statistic (just the integers). '''

        self.cursor.execute("""SELECT start_year,end_year
            FROM statlookup WHERE statistic_name = %s""", (statistic,))
        years = self.cursor.fetchone()
        return [years[0] , years[1]]

    def getListOfStatisticNames(self):
        ''' Queries the database for a list of all valid statistic
            names to populate the dropdown menu on the website. '''

        stat_list = []
        output_string = "Statistic Name"
        #gets item from dictionary and sorts for drop-down menu
        for key in self.stat_dictionary:
            stat_list.append(key)
        stat_list.sort()
        for item in stat_list:
            output_string += "\r\n"
            output_string += item
        return output_string

    def getListOfStates(self):
        ''' Queries the database for a list of all valid states/regions. '''

        output_string = "Name"
        self.cursor.execute("""SELECT region_name
            FROM regionlookup ORDER BY region_id""")
        for row in self.cursor:
            output_string += "\r\n"
            output_string += row[0]
        return output_string


    def sendQuery(self, sqlQuery):

        try:
            outputString = ""
            thisData = self.getDataForSpecificYear("GDP",1970,"State-by-state")
            outputString += thisData
            outputString

        except:
            outputString +=  'Problem with select query. =(<br>'

        #myDict = self.getDataForSpecificYear('GDP')
        #for item in myDict:
        #    outputString += str(item) + "\n"
        return outputString
