import os
from github import Repository

from lib.abstract_strategy import AbstractStrategy


class CodeStrategy(AbstractStrategy):
    def clone(self, base_repository: Repository, new_repository: Repository):
        # copy code
        os.system("git clone --bare %s" % base_repository.ssh_url)
        os.system("cd %s.git && git push --mirror %s" % (base_repository.name, new_repository.ssh_url))
        os.system("rm -Rf %s.git" % base_repository.name)

