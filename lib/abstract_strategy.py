from abc import ABC, abstractmethod

from github import Repository


class AbstractStrategy(ABC):

    @abstractmethod
    def clone(self, base_repository: Repository, new_repository: Repository):
        pass
