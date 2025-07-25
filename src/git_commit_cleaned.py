import git
import os

REPO_PATH= os.getcwd()
CLEANED_FILE = "data/cleaned_data.csv"

def commit_cleaned_file():
    repo= git.Repo(REPO_PATH)
    repo.git.add(CLEANED_FILE)
    repo.index.commit("Add cleaned data")
    print("Committed cleaned data")
    
if __name__=="__main__":
    commit_cleaned_file()
    print("Script finished")
