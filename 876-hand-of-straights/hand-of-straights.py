import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Determine if it's possible to arrange the hand into groups of size 'groupSize', each containing consecutive integers.

        Args:
        - hand: A list of integers representing the cards in the hand.
        - groupSize: An integer indicating the size of each group.

        Returns:
        - A boolean value indicating whether it's possible to rearrange the cards into groups of 'groupSize'.

        Intuition:
        - We first create a frequency dictionary to count the occurrences of each card value in the hand.
        - Then, we build a min-heap from the unique card values.
        - We iterate through the min-heap and for each card value, we attempt to form a group of 'groupSize' consecutive cards.
        - If we encounter a card value that cannot be used to form a group, or if there's a gap in the sequence, we return False.
        - Otherwise, if we successfully form all required groups, we return True.

        Time Complexity Analysis:
        - Constructing the frequency dictionary takes O(n) time, where n is the number of cards in the hand.
        - Building the min-heap from the unique card values also takes O(n) time.
        - The main loop iterates through the min-heap, and for each card value, it performs constant-time operations to decrement the count in the frequency dictionary and potentially remove the card value from the heap. This loop has a time complexity of O(n * k), where k is the average size of the groups.
        - Thus, the overall time complexity is O(n * k).

        Space Complexity Analysis:
        - The frequency dictionary and the min-heap both require additional space proportional to the number of unique card values, which is O(n).
        - Therefore, the overall space complexity is O(n).
        """

        # Count the frequency of each card
        hash_map = {}
        for h in hand:
            hash_map[h] = hash_map.get(h, 0) + 1

        # Build a min-heap from the unique card values
        min_heap = list(hash_map.keys())
        heapq.heapify(min_heap)

        # Attempt to form groups
        while min_heap:
            first = min_heap[0]

            for i in range(first, first + groupSize):
                if i not in hash_map:
                    return False

                hash_map[i] -= 1
                if hash_map[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True
