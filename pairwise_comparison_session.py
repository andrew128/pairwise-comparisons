from typing import List, Dict

class PairwiseComparisonSession:
    def __init__(self):
        self.option_map: Dict[int, str] = {}

    def read_options(self, options: List[int], names: List[str]) -> None:
        """Store mapping of IDs to their names"""
        self.option_map = dict(zip(options, names))

    def prompt_user(self):
        '''
        Prompt the user for two options
        '''
        pass

    def generate_options_to_compare(self):
        '''
        '''
        pass

    def generate_results(self):
        pass

    def run(self):
        pass