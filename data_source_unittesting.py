#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from data_source import *
import cgitb
cgitb.enable()


# Unit tests for the DataSource class within data_source.py
# (within this directory)
#Created by Thomas Redding and Ben Wedin, 2015


class TestStringMethods(unittest.TestCase):
    # preparing to test
    def setUp(self):
        self.dataSource = DataSource()
        self.dataSource.createCursorAndLookups()

    # ending the test
    def tearDown(self):
        pass

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_getYearRangeTest1(self):
        self.assertEqual(self.dataSource.getMaxYearRange("State Prison Population"),
            """Start Year, End Year\r\n1925,2013""")

    def test_getYearRangeTest2(self):
        self.assertEqual(self.dataSource.getMaxYearRange("Aggravated Assault Rate"),
        """Start Year, End Year\r\n1960,2012""")


    def test_listOfStatistics(self):
        self.assertEqual(self.dataSource.getListOfStatisticNames(),
        """Statistic Name\r
Aggravated Assault Rate\r
Forcible Rape Rate\r
GDP\r
GDP per capita\r
Murder Rate\r
Personal Income\r
Population\r
Robbery Rate\r
State Prison Population""")

    def test_listOfRegions(self):
        self.assertEqual(self.dataSource.getListOfStates(),"""Name\r
United States\r
Alabama\r
Alaska\r
Arizona\r
Arkansas\r
California\r
Colorado\r
Connecticut\r
Delaware\r
District of Columbia\r
Florida\r
Georgia\r
Hawaii\r
Idaho\r
Illinois\r
Indiana\r
Iowa\r
Kansas\r
Kentucky\r
Louisiana\r
Maine\r
Maryland\r
Massachusetts\r
Michigan\r
Minnesota\r
Mississippi\r
Missouri\r
Montana\r
Nebraska\r
Nevada\r
New Hampshire\r
New Jersey\r
New Mexico\r
New York\r
North Carolina\r
North Dakota\r
Ohio\r
Oklahoma\r
Oregon\r
Pennsylvania\r
Rhode Island\r
South Carolina\r
South Dakota\r
Tennessee\r
Texas\r
Utah\r
Vermont\r
Virginia\r
Washington\r
West Virginia\r
Wisconsin\r
Wyoming""")

    def test_getDataForYearRangeOutOfBoundsBothYears(self):
        self.assertEqual(self.dataSource.getDataForYearRange("Population","42","4242","United States"),
"""State,Year,Population\r
United States,1929,121769000.0\r
United States,1930,123075000.0\r
United States,1931,124038000.0\r
United States,1932,124839000.0\r
United States,1933,125580000.0\r
United States,1934,126372000.0\r
United States,1935,127251000.0\r
United States,1936,128054000.0\r
United States,1937,128822000.0\r
United States,1938,129825000.0\r
United States,1939,130884000.0\r
United States,1940,131955000.0\r
United States,1941,133417000.0\r
United States,1942,134670000.0\r
United States,1943,134697000.0\r
United States,1944,134075000.0\r
United States,1945,133387000.0\r
United States,1946,140638000.0\r
United States,1947,143665000.0\r
United States,1948,146091000.0\r
United States,1949,148666000.0\r
United States,1950,151871000.0\r
United States,1951,153970000.0\r
United States,1952,156369000.0\r
United States,1953,158946000.0\r
United States,1954,161881000.0\r
United States,1955,165058000.0\r
United States,1956,168078000.0\r
United States,1957,171178000.0\r
United States,1958,174153000.0\r
United States,1959,177136000.0\r
United States,1960,179972000.0\r
United States,1961,182976000.0\r
United States,1962,185739000.0\r
United States,1963,188434000.0\r
United States,1964,191085000.0\r
United States,1965,193460000.0\r
United States,1966,195499000.0\r
United States,1967,197375000.0\r
United States,1968,199312000.0\r
United States,1969,201298000.0\r
United States,1970,203798722.0\r
United States,1971,206817509.0\r
United States,1972,209274882.0\r
United States,1973,211349205.0\r
United States,1974,213333635.0\r
United States,1975,215456585.0\r
United States,1976,217553859.0\r
United States,1977,219760875.0\r
United States,1978,222098244.0\r
United States,1979,224568579.0\r
United States,1980,227224719.0\r
United States,1981,229465744.0\r
United States,1982,231664432.0\r
United States,1983,233792014.0\r
United States,1984,235824907.0\r
United States,1985,237923734.0\r
United States,1986,240132831.0\r
United States,1987,242288936.0\r
United States,1988,244499004.0\r
United States,1989,246819222.0\r
United States,1990,249622814.0\r
United States,1991,252980941.0\r
United States,1992,256514224.0\r
United States,1993,259918588.0\r
United States,1994,263125821.0\r
United States,1995,266278393.0\r
United States,1996,269394284.0\r
United States,1997,272646925.0\r
United States,1998,275854104.0\r
United States,1999,279040168.0\r
United States,2000,282162411.0\r
United States,2001,284968955.0\r
United States,2002,287625193.0\r
United States,2003,290107933.0\r
United States,2004,292805298.0\r
United States,2005,295516599.0\r
United States,2006,298379912.0\r
United States,2007,301231207.0\r
United States,2008,304093966.0\r
United States,2009,306771529.0\r
United States,2010,309326295.0\r
United States,2011,311582564.0\r
United States,2012,313873685.0\r
United States,2013,316128839.0\r
United States,2014,318857056.0""")

    def test_getDataForYearRangeOutOfBoundsEndYear(self):
        self.assertEqual(self.dataSource.getDataForYearRange("State Prison Population","1993","2030","Wyoming"),
"""State,Year,State Prison Population\r
Wyoming,1993,1129.0\r
Wyoming,1994,1217.0\r
Wyoming,1995,1395.0\r
Wyoming,1996,1477.0\r
Wyoming,1997,1549.0\r
Wyoming,1998,1571.0\r
Wyoming,1999,1710.0\r
Wyoming,2000,1680.0\r
Wyoming,2001,1684.0\r
Wyoming,2002,1737.0\r
Wyoming,2003,1872.0\r
Wyoming,2004,1980.0\r
Wyoming,2005,2047.0\r
Wyoming,2006,2114.0\r
Wyoming,2007,2084.0\r
Wyoming,2008,2084.0\r
Wyoming,2009,2075.0\r
Wyoming,2010,2112.0\r
Wyoming,2011,2183.0\r
Wyoming,2012,2204.0\r
Wyoming,2013,2310.0""")

    def test_getDataForYearRangeOutOfBoundsStartYear(self):
        self.assertEqual(self.dataSource.getDataForYearRange("GDP","1889","2000","Oklahoma"),
"""State,Year,GDP\r
Oklahoma,1963,6151.0\r
Oklahoma,1964,6544.0\r
Oklahoma,1965,6966.0\r
Oklahoma,1966,7468.0\r
Oklahoma,1967,8087.0\r
Oklahoma,1968,8836.0\r
Oklahoma,1969,9622.0\r
Oklahoma,1970,10369.0\r
Oklahoma,1971,11278.0\r
Oklahoma,1972,12738.0\r
Oklahoma,1973,14483.0\r
Oklahoma,1974,16204.0\r
Oklahoma,1975,18163.0\r
Oklahoma,1976,20822.0\r
Oklahoma,1977,24022.0\r
Oklahoma,1978,27105.0\r
Oklahoma,1979,31546.0\r
Oklahoma,1980,37608.0\r
Oklahoma,1981,45430.0\r
Oklahoma,1982,49317.0\r
Oklahoma,1983,47701.0\r
Oklahoma,1984,51291.0\r
Oklahoma,1985,52765.0\r
Oklahoma,1986,48997.0\r
Oklahoma,1987,49055.0\r
Oklahoma,1988,52667.0\r
Oklahoma,1989,55007.0\r
Oklahoma,1990,57805.0\r
Oklahoma,1991,59632.0\r
Oklahoma,1992,62209.0\r
Oklahoma,1993,65552.0\r
Oklahoma,1994,68251.0\r
Oklahoma,1995,70859.0\r
Oklahoma,1996,76316.0\r
Oklahoma,1997,80331.0\r
Oklahoma,1998,80902.0\r
Oklahoma,1999,85202.0\r
Oklahoma,2000,91973.0""")

    def test_getDataForYearRangeFlippedYearArgs(self):
        self.assertEqual(self.dataSource.getDataForYearRange("Aggravated Assault Rate","1966","1963","Texas"),
"""State,Year,Aggravated Assault Rate\r
Texas,1966,150.4""")

    def test_getDataForYearRangeRepeatedYear(self):
        self.assertEqual(self.dataSource.getDataForYearRange("Aggravated Assault Rate","2010","2010","Minnesota"),
"""State,Year,Aggravated Assault Rate\r
Minnesota,2010,136.2""")

    def test_getDataForYearRangeRepeatedYearOutOfBounds(self):
        self.assertEqual(self.dataSource.getDataForYearRange("GDP per capita","2020","2020","Montana"),
"""State,Year,GDP per capita\r
Montana,2013,43382.0""")

    def test_getDataForSpecificYearStateByState(self):
        self.assertEqual(self.dataSource.getDataForSpecificYear("Robbery Rate","1970","State-by-state"),
"""State,Year,Robbery Rate\r
Alabama,1970,50.3\r
Alaska,1970,71.8\r
Arizona,1970,120.2\r
Arkansas,1970,45.6\r
California,1970,206.9\r
Colorado,1970,129.1\r
Connecticut,1970,70.4\r
Delaware,1970,105.5\r
District of Columbia,1970,1561.9\r
Florida,1970,186.1\r
Georgia,1970,95.8\r
Hawaii,1970,63.3\r
Idaho,1970,20.5\r
Illinois,1970,251.1\r
Indiana,1970,110.3\r
Iowa,1970,28.5\r
Kansas,1970,75.1\r
Kentucky,1970,72.8\r
Louisiana,1970,140.8\r
Maine,1970,12.6\r
Maryland,1970,338.6\r
Massachusetts,1970,99.5\r
Michigan,1970,346.6\r
Minnesota,1970,89.1\r
Mississippi,1970,19.0\r
Missouri,1970,200.8\r
Montana,1970,22.3\r
Nebraska,1970,57.3\r
Nevada,1970,188.4\r
New Hampshire,1970,12.1\r
New Jersey,1970,169.4\r
New Mexico,1970,67.6\r
New York,1970,446.1\r
North Carolina,1970,52.3\r
North Dakota,1970,6.5\r
Ohio,1970,145.9\r
Oklahoma,1970,54.7\r
Oregon,1970,102.5\r
Pennsylvania,1970,108.6\r
Rhode Island,1970,78.3\r
South Carolina,1970,60.1\r
South Dakota,1970,17.1\r
Tennessee,1970,82.0\r
Texas,1970,136.5\r
Utah,1970,53.1\r
Vermont,1970,7.6\r
Virginia,1970,95.5\r
Washington,1970,93.5\r
West Virginia,1970,27.3\r
Wisconsin,1970,33.1\r
Wyoming,1970,22.0""")

fooSuite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)

fooRunner = unittest.TextTestRunner()
fooResult = fooRunner.run(fooSuite)


print "Content-type: text/html\r\n\r\n",
output_string = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<title>Tiny web app results</title>
</head>
<body>
'''
output_string += "---- START OF TEST RESULTS<br><br>"
output_string += "fooResult::errors <br><br>"
for item in fooResult.errors:
    output_string += "<br><br>"
    output_string += str(item)

output_string += "fooResult::failures<br><br>"
for item in fooResult.failures:
    output_string += "<br><br>"
    output_string += str(item)
#output_string += str(fooResult.failures)

output_string += '''</body>
</html>'''
print output_string
