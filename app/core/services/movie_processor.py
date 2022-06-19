from abc import ABC, abstractmethod

from bs4 import BeautifulSoup
import requests


class MovieProcessor(ABC):
    movie: BeautifulSoup | None

    def get_content(self, url: str) -> None:
        requested_page = requests.get(url=url, headers={"Accept-Language": "en-GB,en;q=0.9"})
        if requested_page.status_code != 200:
            self.movie = None
            raise ConnectionError(f"{requested_page.status_code} : {url}")

        self.movie = BeautifulSoup(requested_page.content, features="html.parser")

    @abstractmethod
    def get_movie_name(self) -> str:
        ...

    @abstractmethod
    def get_movie_year(self) -> int:
        ...


class IMDBProcessor(MovieProcessor):
    def get_movie_name(self) -> str:
        return self.movie.find("h1", attrs={"data-testid": "hero-title-block__title"}).text

    def get_movie_year(self) -> int:
        return int(
            self.movie.find("ul", attrs={"data-testid": "hero-title-block__metadata"}).findChildren("a")[0].text
        )
