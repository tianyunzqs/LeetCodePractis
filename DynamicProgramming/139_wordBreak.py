# -*- coding: utf-8 -*-
# @Time        : 2020/5/5 10:31
# @Author      : tianyunzqs
# @Description : 

"""
139. Word Break
Medium

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.
Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

"""
dp[i] = s[0:i+1]在dictionary
"""


def build_dictionary_tree(word_dict):
    trie = dict()
    for word in word_dict:
        p = trie
        for ch in word:
            if ch not in p:
                p[ch] = {}
            p = p[ch]
        p[''] = ''
    return trie


def wordBreak2(s: str, wordDict: list) -> bool:
    """
    字典树未考虑以下情形
    s = "aaaaaaa",
    wordDict = ["aaaa", "aa"]或["aaaa", "aaa"]
    :param s:
    :param wordDict:
    :return:
    """
    trie = build_dictionary_tree(wordDict)
    p = trie
    for i, ch in enumerate(s):
        if ch in p:
            p = p[ch]
            if '' in p:
                p = trie
        else:
            return False

    return p == trie


def wordBreak(s: str, wordDict: list) -> bool:
    """
    dp[i]表示子串s[0:i]能否被分割成wordDict中的词语
    dp[0]表示子串s[0:0]=''，空串默认可以分割，因此dp[0] = True
    这里dp = [False for _ in range(len(s) + 1)]
    多加一个位置是因为在遍历的时候，需要遍历子串s[0: i+1]，包含位置i
    if判断条件里添加dp[j]的限定是因为如果子串s[0:j]不能分割为wordDict中词语组合，s[j:i]子串就可以不用判断了
    :param s:
    :param wordDict:
    :return:
    """
    wordDict = set(wordDict)
    dp = [False for _ in range(len(s) + 1)]
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j: i] in wordDict:
                dp[i] = True
                break

    return dp[-1]


if __name__ == '__main__':
    s = [
        "leetcode",
        "applepenapple",
        "catsandog",
        "abcd",
        "aaaaaaa",
        "aaaaaaa",

    ]
    wordDict = [
        ["leet", "code"],
        ["apple", "pen"],
        ["cats", "dog", "sand", "and", "cat"],
        ["a", "abc", "b", "cd"],
        ["aaaa", "aa"],
        ["aaaa", "aaa"]
    ]
    for a, b in zip(s, wordDict):
        print(a, b)
        print(wordBreak(a, b))
