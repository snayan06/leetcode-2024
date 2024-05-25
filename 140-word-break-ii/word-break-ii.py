class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = [""]

        for i in range(1, len(s) + 1):
            print("i:{}",i)
            for j in range(i):
                word = s[j:i]
                print("j:,word:",j, word)
                if word in word_set:
                    print(dp[j])
                    for sentence in dp[j]:
                        print(sentence, True)
                        dp[i].append((sentence + " " + word).strip())

        return dp[len(s)]
