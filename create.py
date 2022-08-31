import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv("ACCESSTOKEN")

def create():
    #save folder name 
    script_arg = str(sys.argv[1])
    
    #create project folder
    path = '/Users/james/Documents/Projects/MyProjects/{}'.format(script_arg)
    os.mkdir(path)
    
    #create repo on github
    g = Github(access_token)
    user = g.get_user()
    repo = user.create_repo(script_arg)
    
    #success!
    msg = "Successfully Created Repository: "
    print(msg, script_arg)

create()