import os
from dotenv import load_dotenv
from abc import abstractmethod
from dataclasses import dataclass , field
from pathlib import Path , PosixPath
from termcolor import cprint
import requests


@dataclass(slots=True)
class Solution():

    """Just a helper class to help you load the data.
    --------------------------------------------------------------------------
    In order to work and succesfully download the challenge data
    you must provide your login cookie from AoC in the .env file as cookie=...
    You must also provide the day of the challenge on which you are working on.

    It will make the challenge data directories automatically for each day.
    Then you can write your solutions as subclasses of Solution class
    and access the data via the instance attribute 'self.challenge_data'
    which is simply a f.read().

    Import on the top of your daily solutions:
                    'from pyaoc.data_source import Solution'

    For any bugs feel free to reach out and open an issue.

    Happy Coding!

    ~ Made by Channi
    """

    day : int = field(default = None)
    cookie : str = field(init = False , repr = False , default = None)
    file_path : PosixPath = field(init = False , repr = False)
    challenge_data : str = field(init = False , default = None)

    def __post_init__(self) -> None:
        load_dotenv()
        if "cookie" not in os.environ.keys():
            raise CookieNotFound()

        self.cookie = os.environ["cookie"]

        ##hacky day resolution
        if self.day is None:
            hacky_resolution = Path.cwd().parts[-1]
            if not hacky_resolution.startswith("day") or not hacky_resolution[-1].isdigit():
                raise ValueError("Unable Resolve Day of Competition.")
            self.day = hacky_resolution[-1]

        data_path = Path(__file__).resolve().parent.joinpath("challenge_data",f"day_{self.day}")
        data_path.mkdir(parents=True,exist_ok=True)

        self.file_path = data_path / f"day_{self.day}.txt"
        if not self.file_path.is_file():
            response = requests.request("GET",
                f"https://adventofcode.com/2022/day/{self.day}/input",
                headers={'Cookie': self.cookie})
            cprint("Request: OK")
            if response.status_code == 200:
                ##store data
                with self.file_path.open(mode="w+", encoding="utf-8") as f:
                    f.write(response.text)
                cprint("Data succesfully stored!" , "blue" , attrs = ["bold","reverse"])

        ##read data
        self.challenge_data = None
        with self.file_path.open(mode="r+" , encoding = "utf-8") as f:
            self.challenge_data = f.read()
        cprint(f"Data for day {self.day} succesfully read!" , "blue" , attrs = ["bold","reverse"])

    @abstractmethod
    def solve(self) -> ...:
        ...


class CookieNotFound(Exception):
    """Exception raised for missing cookies in your environment."""

    def __init__(self, message="We couldn't find your Cookie in the path!"):
        self.message = message
        super().__init__(self.message)
