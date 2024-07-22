from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Create a dictionary to map names to heights
        d = {}
        for name, height in zip(names, heights):
            if height in d:
                d[height].append(name)
            else:
                d[height] = [name]

        # Sort the dictionary items by height in descending order
        sorted_items = sorted(d.items(), key=lambda x: x[0], reverse=True)

        # Extract and return the sorted names
        sorted_names = []
        for height, names in sorted_items:
            sorted_names.extend(names)
        return sorted_names
