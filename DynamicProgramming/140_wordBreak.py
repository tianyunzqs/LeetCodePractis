# -*- coding: utf-8 -*-
# @Time        : 2020/5/11 15:18
# @Author      : tianyunzqs
# @Description : 

"""
140. Word Break II
Hard

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""


class Solution:
    def __init__(self):
        self.res = []

    def word_break1(self, s, word_dict):
        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True
        for i in range(N):
            for j in range(i, N + 1):
                if dp[i] and s[i:j] in word_dict:
                    dp[j] = True
        return dp

    def dfs(self, s, path, word_dict):
        # 递归终止条件
        if not s:
            self.res.append(path.strip())

        for i in range(1, len(s) + 1):
            # 如果前面的字符串在dict中，则遍历后面剩余的子串
            if s[:i] in word_dict:
                self.dfs(s[i:], path + " " + s[:i], word_dict)

    def wordBreak(self, s: str, wordDict: list) -> list:
        if not s:
            return [""]
        wordDict = set(wordDict)
        dp = self.word_break1(s, wordDict)
        # 如果不满足wordBreak条件，则直接返回即可
        if not dp[-1]:
            return []
        # 深度优先搜索
        self.dfs(s, "", wordDict)
        return self.res


if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(Solution().wordBreak(s, wordDict))

    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(Solution().wordBreak(s, wordDict))

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(Solution().wordBreak(s, wordDict))
