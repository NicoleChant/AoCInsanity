import requests
import os
from dotenv import load_dotenv
from abc import abstractmethod , ABC
import argparse
load_dotenv()

class Solution(ABC):

    def __init__(self) -> None:
        """Just a helper constructor loading the data"""

        if not os.path.isfile("challenge.txt"):
            response = requests.request(
                "GET",
                os.getenv('url'),
                headers={'Cookie': os.getenv('cookie')})
            if response.status_code == 200:
                with open("challenge.txt", mode="w+") as f:
                    f.write(response.text)
                print("Data succesfully stored!")

        ##read data
        self.data = None
        with open("challenge.txt", mode="r+") as f:
            self.data = f.read()
        print("Data succesfully read!")

    @abstractmethod
    def solve(self) -> int:
        ...
