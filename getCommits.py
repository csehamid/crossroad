from github import Github

# First create a Github instance:
g = Github("csehamid", "34a931ebce4443696c45379afb5cee7438041f4d")

# Then play with your Github objects:
print "list of all repositories"
for repo in g.get_user().get_repos():
    print repo.name
    
print
print "list of all commits for crossroad repo"
for commit in ( g.get_user().get_repo("crossroad").get_commits()):
    if commit.commit is not None:
        print commit.commit.author.date ,"   ", commit.commit.message , "\n"
        
        