from urllib.parse import urljoin

import requests

from src.config.config import config


class GitHubApi:

    DEFAULT_HEADER = "application/vnd.github+json"

    def __init__(self) -> None:
        pass

    def _form_url(self, path):
        return urljoin(config.BASE_URL_API, path)

    def login(self, user_name):
        print("LOGIN REQUEST")
        return True

    def logout(self):
        print("LOGOUT REQUEST")
        return True

    def research_repo(self, repo_name):
        r = requests.get(
            url=self._form_url("/search/repositories"),
            headers={"accept": self.DEFAULT_HEADER},
            params={"q": repo_name},
        )
        r.raise_for_status()

        return r


a = GitHubApi()
print(a.research_repo("talent-eng"))
