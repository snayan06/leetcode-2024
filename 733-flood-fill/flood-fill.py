class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # up  # left  # down  # right
        prev_color = image[sr][sc]

        def dfs(sr, sc):
            if image[sr][sc] == color:
                return image
            else:
                image[sr][sc] = color
            for dx, dy in directions:
                new_sr, new_sc = sr + dx, sc + dy

                if (
                    0 <= new_sr < m
                    and 0 <= new_sc < n
                    and image[new_sr][new_sc] == prev_color
                ):
                    dfs(new_sr, new_sc)

        dfs(sr,sc)

        return image