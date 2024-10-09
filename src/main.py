import json
import argparse
from scheluder import schelude


class EventPulseBotCLI:
    def __init__(self):
        self._parser = argparse.ArgumentParser(description='Process arguments')
        self._parser.add_argument('-dl', '--distributionlist', type=str)
        self._args = self._parser.parse_args()

    @property
    def emails(self):
        return self._args.distributionlist


if __name__ == '__main__':
    args = EventPulseBotCLI()
    with open(args.emails, 'r') as file:
        emails = json.load(file)
    schelude(emails)
