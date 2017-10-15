import urllib

def read_text():
    quotes = open("/Users/anuroopthomas/Development/GitHub/TestPython/testpython/movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("There is some profanity")
    elif "false" in output:
        print("No curse words")
    else:
        print("Cannot Scan")

read_text()
