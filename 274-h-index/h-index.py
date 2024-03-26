class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Calculates the h-index of a researcher based on their citation counts.

        Intuition:
        * The h-index is defined as the maximum number 'h' such that the researcher
          has at least 'h' papers with at least 'h' citations each.
        * Sorting the citations helps in finding this value efficiently.

        Approach:
        1. Sort the citations in ascending order.
        2. Iterate through citations:
           * If a citation is greater than or equal to the number of remaining papers
             (n - i), the current 'i' is the h-index

        Time Complexity:
        * O(n log n) due to the sorting step.
        * The subsequent loop has O(n) time complexity.

        Space Complexity:
        * O(1) if we perform in-place sorting. Some sorting algorithms may 
          require O(n) additional space.

        Args:
            citations: A list of integers representing citation counts.

        Returns:
            The h-index of the researcher.
        """

        citations.sort()
        n = len(citations)
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0
