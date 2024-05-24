from collections import Counter
import copy

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        lettersCounter = Counter(letters)
        
        def explore(index, remainingLetters):
            if index == len(words):
                return 0
            
            # Option 1: Skip the current word
            score_without_word = explore(index + 1, remainingLetters)
            
            # Option 2: Include the current word if possible
            word = words[index]
            wordScore = 0
            tmpCounter = copy.deepcopy(remainingLetters)
            isValid = True
            
            for ch in word:
                if ch in tmpCounter and tmpCounter[ch] > 0:
                    tmpCounter[ch] -= 1
                    wordScore += score[ord(ch) - ord("a")]
                else:
                    isValid = False
                    break
            
            score_with_word = 0
            if isValid:
                score_with_word = wordScore + explore(index + 1, tmpCounter)
            
            # Return the maximum score between including and excluding the current word
            return max(score_with_word, score_without_word)
        
        return explore(0, lettersCounter)
