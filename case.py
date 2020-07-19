#! /usr/bin/env python3

import yaml


class case:
    def __init__(self, path):
        self.path = path

    def get_cases(self):
        with open(self.path, 'r+') as f:
            cases = yaml.safe_load(f)
        return cases
