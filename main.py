#importing the website package
from Website import create_app
#we can do this because Website is a python package because __init__.py
app = create_app()
if __name__ =='__main__': #only if we run this file execute the succeeding line
    app.run(debug = True) #we only want to run the web server if this file is run
    #this is going to start a web server and debug = true means anytime we make changes it refreshes the web server

