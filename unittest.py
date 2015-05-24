import unittest
from data_source import *

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      dataSource = DataSource()
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_getYearRangeTest1(self):
      self.assertEqual(dataSource.getMaxYearRange("State Prison Population",
      """requestType:getMaxYearRange,statistic:State Prison Population\r\n
      Start Year, End Year\r\n
      1925,2013\r\n""")

    def test_getYearRangeTest2(self):
        self.assertEqual(dataSource.getMaxYearRange("Aggravated Assault Rate",
        """requestType:getMaxYearRange,statistic:Aggravated Assault Rate\r\n
        Start Year, End Year\r\n
        1960,2012\r\n""")


  def test_listOfStatistics(self):
      self.assertEqual(dataSource.getListOfStatisticNames(),
      """requestType:getListOfStatisticNames\r\n
      Statistic Name\r\n
      Aggravated Assault Rate\r\n
      Forcible Rape Rate\r\n
      GDP\r\n
      GDP per capita\r\n
      Murder Rate\r\n
      Personal Income\r\n
      Population\r\n
      Robbery Rate\r\n
      State Prison Population\r\n""")




  def test_listOfRegions(self):
      self.assertEqual(dataSource.getListOfStates(),"""requestType:getListOfRegions\r\n
      Region Name\r\n
      United States\r\n
      Alabama\r\n
      Alaska\r\n
      Arizona\r\n
      Arkansas\r\n
      California\r\n
      Colorado\r\n
      Connecticut\r\n
      Delaware\r\n
      District of Columbia\r\n
      Florida\r\n
      Georgia\r\n
      Hawaii\r\n
      Idaho\r\n
      Illinois\r\n
      Indiana\r\n
      Iowa\r\n
      Kansas\r\n
      Kentucky\r\n
      Louisiana\r\n
      Maine\r\n
      Maryland\r\n
      Massachusetts\r\n
      Michigan\r\n
      Minnesota\r\n
      Mississippi\r\n
      Missouri\r\n
      Montana\r\n
      Nebraska\r\n
      Nevada\r\n
      New Hampshire\r\n
      New Jersey\r\n
      New Mexico\r\n
      New York\r\n
      North Carolina\r\n
      North Dakota\r\n
      Ohio\r\n
      Oklahoma\r\n
      Oregon\r\n
      Pennsylvania\r\n
      Rhode Island\r\n
      South Carolina\r\n
      South Dakota\r\n
      Tennessee\r\n
      Texas\r\n
      Utah\r\n
      Vermont\r\n
      Virginia\r\n
      Washington\r\n
      West Virginia\r\n
      Wisconsin\r\n
      Wyoming\r\n""")

def test_getDataForYearRangeOutOfBoundsBothYears(self):
    self.assertEqual(dataSource.getDataForYearRange("Population",42,4242,"United States"),
    """requestType:getDataForYearRange,statistic:Population,state:United States,startYear:42,endYear:4242\r\n
    Year,Value\r\n
    1929,121769000\r\n
    1930,123075000\r\n
    1931,124038000\r\n
    1932,124839000\r\n
    1933,125580000\r\n
    1934,126372000\r\n
    1935,127251000\r\n
    1936,128054000\r\n
    1937,128822000\r\n
    1938,129825000\r\n
    1939,130884000\r\n
    1940,131955000\r\n
    1941,133417000\r\n
    1942,134670000\r\n
    1943,134697000\r\n
    1944,134075000\r\n
    1945,133387000\r\n
    1946,140638000\r\n
    1947,143665000\r\n
    1948,146091000\r\n
    1949,148666000\r\n
    1950,151871000\r\n
    1951,153970000\r\n
    1952,156369000\r\n
    1953,158946000\r\n
    1954,161881000\r\n
    1955,165058000\r\n
    1956,168078000\r\n
    1957,171178000\r\n
    1958,174153000\r\n
    1959,177136000\r\n
    1960,179972000\r\n
    1961,182976000\r\n
    1962,185739000\r\n
    1963,188434000\r\n
    1964,191085000\r\n
    1965,193460000\r\n
    1966,195499000\r\n
    1967,197375000\r\n
    1968,199312000\r\n
    1969,201298000\r\n
    1970,203798722\r\n
    1971,206817509\r\n
    1972,209274882\r\n
    1973,211349205\r\n
    1974,213333635\r\n
    1975,215456585\r\n
    1976,217553859\r\n
    1977,219760875\r\n
    1978,222098244\r\n
    1979,224568579\r\n
    1980,227224719\r\n
    1981,229465744\r\n
    1982,231664432\r\n
    1983,233792014\r\n
    1984,235824907\r\n
    1985,237923734\r\n
    1986,240132831\r\n
    1987,242288936\r\n
    1988,244499004\r\n
    1989,246819222\r\n
    1990,249622814\r\n
    1991,252980941\r\n
    1992,256514224\r\n
    1993,259918588\r\n
    1994,263125821\r\n
    1995,266278393\r\n
    1996,269394284\r\n
    1997,272646925\r\n
    1998,275854104\r\n
    1999,279040168\r\n
    2000,282162411\r\n
    2001,284968955\r\n
    2002,287625193\r\n
    2003,290107933\r\n
    2004,292805298\r\n
    2005,295516599\r\n
    2006,298379912\r\n
    2007,301231207\r\n
    2008,304093966\r\n
    2009,306771529\r\n
    2010,309326295\r\n
    2011,311582564\r\n
    2012,313873685\r\n
    2013,316128839\r\n
    2014,318857056\r\n"""


  def test_getDataForYearRangeOutOfBoundsEndYear(self):
      self.assertEqual(dataSource.getDataForYearRange("State Prison Population",1993,2030,"Wyoming"),
      """requestType:getDataForYearRange,statistic:State Prison Population,state:Wyoming,startYear:1993,endYear:2030\r\n
      Year,Value\r\n
      1993,1129\r\n
      1994,1217\r\n
      1995,1395\r\n
      1996,1477\r\n
      1997,1549\r\n
      1998,1571\r\n
      1999,1710\r\n
      2000,1680\r\n
      2001,1684\r\n
      2002,1737\r\n
      2003,1872\r\n
      2004,1980\r\n
      2005,2047\r\n
      2006,2114\r\n
      2007,2084\r\n
      2008,2084\r\n
      2009,2075\r\n
      2010,2112\r\n
      2011,2183\r\n
      2012,2204\r\n
      2013,2310\r\n"""


  def test_getDataForYearRangeOutOfBoundsStartYear(self):
      self.assertEqual(dataSource.getDataForYearRange("GDP",1889,2000,"Oklahoma"),
      """requestType:getDataForYearRange,statistic:GDP,state:Oklahoma,startYear:1889,endYear:2000\r\n
      Year,Value\r\n
      1963,6151\r\n
      1964,6544\r\n
      1965,6966\r\n
      1966,7468\r\n
      1967,8087\r\n
      1968,8836\r\n
      1969,9622\r\n
      1970,10369\r\n
      1971,11278\r\n
      1972,12738\r\n
      1973,14483\r\n
      1974,16204\r\n
      1975,18163\r\n
      1976,20822\r\n
      1977,24022\r\n
      1978,27105\r\n
      1979,31546\r\n
      1980,37608\r\n
      1981,45430\r\n
      1982,49317\r\n
      1983,47701\r\n
      1984,51291\r\n
      1985,52765\r\n
      1986,48997\r\n
      1987,49055\r\n
      1988,52667\r\n
      1989,55007\r\n
      1990,57805\r\n
      1991,59632\r\n
      1992,62209\r\n
      1993,65552\r\n
      1994,68251\r\n
      1995,70859\r\n
      1996,76316\r\n
      1997,80331\r\n
      1998,80902\r\n
      1999,85202\r\n
      2000,91973\r\n""")

def test_getDataForYearRangeFlippedYearArgs(self):
    self.assertEqual(dataSource.getDataForYearRange("Aggravated Assault Rate",1966,1963,"Texas"),
    """requestType:getDataForYearRange,statistic:Aggravated Assault Rate,state:Texas,startYear:1966,endYear:1963\r\n
    Year,Value\r\n
    1966,150.4\r\n""")

def test_getDataForYearRangeRepeatedYear(self):
    self.assertEqual(dataSource.getDataForYearRange("Aggravated Assault Rate",2010,2010,"Minnesota"),
    """requestType:getDataForYearRange,statistic:Forcible Rape Rate,state:Minnesota,startYear:2010,endYear:2010\r\n
    Year,Value\r\n
    2010,33.9\r\n""")

def test_getDataForYearRangeRepeatedYearOutOfBounds(self):
    self.assertEqual(dataSource.getDataForYearRange("Aggravated Assault Rate",2020,2020,"Montana"),
    """requestType:getDataForYearRange,statistic:GDP per capita,state:Montana,startYear:2020,endYear:2020\r\n
    Year,Value\r\n
    2013,43026\r\n""")

def test_getDataForSpecificYearStateByState(self):
    self.assertEqual(dataSource.getDataForSpecificYear("Robbery Rate",1970,"State-by-state"),
    """requestType:getDataForSpecificYear,statistic:Robbery Rate,state:State-by-state,year:1970\r\n
    Year,Value\r\n
    United States,374.4\r\n
    Alabama,11.7\r\n
    Alaska,12.2\r\n
    Arizona,9.5\r\n
    Arkansas,10.1\r\n
    California,6.9\r\n
    Colorado,6.2\r\n
    Connecticut,3.5\r\n
    Delaware,7.7\r\n
    District of Columbia,29.2\r\n
    Florida,12.7\r\n
    Georgia,15.3\r\n
    Hawaii,3.6\r\n
    Idaho,4.6\r\n
    Illinois,9.6\r\n
    Indiana,4.9\r\n
    Iowa,1.9\r\n
    Kansas,4.8\r\n
    Kentucky,11.1\r\n
    Louisiana,11.7\r\n
    Maine,1.5\r\n
    Maryland,9.2\r\n
    Massachusetts,3.5\r\n
    Michigan,9.4\r\n
    Minnesota,2\r\n
    Mississippi,11.5\r\n
    Missouri,10.7\r\n
    Montana,3.2\r\n
    Nebraska,3\r\n
    Nevada,8.8\r\n
    New Hampshire,2\r\n
    New Jersey,5.7\r\n
    New Mexico,9.6\r\n
    New York,7.9\r\n
    North Carolina,11.7\r\n
    North Dakota,0.5\r\n
    Ohio,6.6\r\n
    Oklahoma,5.9\r\n
    Oregon,4.6\r\n
    Pennsylvania,5.4\r\n
    Rhode Island,3.2\r\n
    South Carolina,14.6\r\n
    South Dakota,3.8\r\n
    Tennessee,8.8\r\n
    Texas,11.6\r\n
    Utah,3.4\r\n
    Vermont,1.3\r\n
    Virginia,10.4\r\n
    Washington,3.5\r\n
    West Virginia,6.2\r\n
    Wisconsin,2\r\n
    Wyoming,5.7\r\n"""


if __name__ == '__main__':
    unittest.main()
