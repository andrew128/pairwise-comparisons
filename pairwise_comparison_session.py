from typing import List, Dict, Tuple, Optional

class PairwiseComparisonSession:
    def __init__(self):
        # Map of index of option to option
        self.option_map: Dict[int, str] = {}
        # Map of index of option to score
        self.option_score: Dict[int, int] = {}

    def store_options(self, options: List[str]) -> None:
       """Store mapping of indices to their names"""
       self.option_map = {i: option for i, option in enumerate(options)}

    def get_option(self, index: int) -> str:
        return self.option_map[index]

    def store_result_from_user(self, option_index) -> None:
        self.option_score[option_index] += 1

    def generate_results(self) -> Tuple[int, str, int]:
        """
        Show the results
        """
        results = []
        for index, option in self.option_map.items():
            score = self.option_score.get(index, 0)  # Default to 0 if no score
            results.append((index, option, score))
        
        # Sort by score in descending order
        return sorted(results, key=lambda x: x[2], reverse=True)
