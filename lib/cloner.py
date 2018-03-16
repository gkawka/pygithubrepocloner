from github import Github
from lib.abstract_strategy import AbstractStrategy


class Cloner:
    clone_strategies = []

    def __init__(self, github: Github, organization_name: str):
        self.organization_name = organization_name
        self.github = github

    def clone(self, base_repository_name: str, new_repository_name: str):
        if not self.clone_strategies:
            raise RuntimeError("Empty clone strategy list. add_strategy first")

        organization = self.github.get_organization(self.organization_name)
        base_repository = organization.get_repo(base_repository_name)

        # create new repository
        new_repository = organization.create_repo(new_repository_name)

        for strategy in self.clone_strategies:
            strategy.clone(base_repository, new_repository)

    def add_strategy(self, strategy: AbstractStrategy):
        self.clone_strategies.append(strategy)
