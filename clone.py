import sys
import argparse
from github import Github
from lib.cloner import Cloner
from lib.code_strategy import CodeStrategy
from lib.issues_strategy import IssuesStrategy

if sys.version_info[0] < 3 and sys.version_info[1] < 6:
    raise Exception("Python 3.6 or a more recent version is required.")

parser = argparse.ArgumentParser(description="Clone repository")
parser.add_argument('--access_token', required=True, type=str, help="Access token to your GitHub organization")
parser.add_argument('--organization_name', required=True, type=str, help="Organization name where the repo to copy is")
parser.add_argument('--base_repository_name', required=True, type=str, help="Repository to copy from")
parser.add_argument('--new_repository_name', required=True, type=str, help="Repository to create and copy to")

args = parser.parse_args()
print(args.access_token, args.base_repository_name, args.new_repository_name)

github = Github(args.access_token)

cloner = Cloner(github, args.organization_name)

print("Starting cloning %s repository to %s..." % (args.base_repository_name, args.new_repository_name))
cloner.add_strategy(IssuesStrategy())
cloner.add_strategy(CodeStrategy())
cloner.clone(args.base_repository_name, args.new_repository_name)
print("Finished.")
