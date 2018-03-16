from github import Repository
from lib.abstract_strategy import AbstractStrategy


class IssuesStrategy(AbstractStrategy):

    def clone(self, base_repository: Repository, new_repository: Repository):
        # copy issues
        for issue in base_repository.get_issues(direction="asc"):
            new_repository.create_issue(issue.title, issue.body)
