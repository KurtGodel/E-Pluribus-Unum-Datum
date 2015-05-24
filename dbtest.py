
#!/usr/bin/python

# cgitb is for DEBUG PURPOSES ONLY!  Comment out these lines once your app is
# "in production".
# We print out the ContentType HTTP header first because cgitb produces its
# error output in HTML.
import cgitb
cgitb.enable()
import os.path
import sys
import psycopg2


def runCode():
    outputStr = 'Content-type: text/html\r\n\r\n'
    outputStr += '<html><head></head><body>'

    # Note that cgitb works by catching uncaught exceptions.  In the code below I
    # use a bunch of try/except blocks, which is correct practice that you should
    # follow in the code that you write for this project.
    #   HOWEVER!  If I work really hard at catching my own exceptions during
    # development, I lose out on the chance for cgitb to tell me details about
    # them.  So consider leaving out the exception handling when you're first
    # developing your stuff.  (You could leave "# TODO" comments for yourself to
    # make sure you go back and fill them in.)


    # CHANGE THESE LINES!                                      <~~~~~~~~~~~~~~~ Hey!
    USERNAME = 'jadrian'
    DB_NAME = 'jadrian'

    outputStr += 'Hello!<br>'

    # Step 1: Read your password from the secure file.
    outputStr += 'Reading your password...'
    try:
        f = open(os.path.join('/cs257', USERNAME))
        PASSWORD = f.read().strip()
        f.close()
        outputStr += 'Success!<br>'
        # UNCOMMENT THIS LINE TO SEE YOUR PASSWORD!            <~~~~~~~~~~~~~~~ Hey!
        #print 'Your database password is %s.<br>' % PASSWORD
    except:
        outputStr += 'Failed. =(<br>'
        sys.exit()

    # Step 2: Connect to the database.
    outputStr += 'Connecting to database %s...' % DB_NAME
    try:
        db_connection = psycopg2.connect(user=USERNAME,
                                         database=DB_NAME,
                                         password=PASSWORD)
        outputStr += 'Success!<br>'
    except:
        outputStr += 'Failed. =(<br>'
        sys.exit()

    # Step 3: Create a "cursor".  When you execute a
    # query with a cursor, you can get the rows of the
    # output in a for-loop (like scrolling a cursor
    # through a text document).
    outputStr += 'Creating a database cursor...'
    try:
        cursor = db_connection.cursor()
        outputStr += 'Success!<br>'
    except:
        outputStr += 'Failed. =(<br>'
        sys.exit()

    # Step 4: Read the rows of the output and act
    # on them.
    try:
        queryStr = "SELECT table_name FROM information_schema.tables WHERE table_schema='public'"
        outputStr += "["
        outputStr += queryStr
        outputStr += "]"
        cursor.execute(queryStr)
        outputStr += '<pre>'
        for row in cursor:
            outputStr += row
        outputStr += '</pre>'
    except:
        outputStr += 'Problem with select query. =(<br>'

    outputStr += '</body></html>'

    return outputStr
