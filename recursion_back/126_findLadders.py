# -*- coding: utf-8 -*-
# @Time        : 2021/5/10 10:50
# @Author      : tianyunzqs
# @Description :

"""
126. 单词接龙 II
按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的
转换序列
是形式上像 beginWord -> s1 -> s2 -> ... -> sk 这样的单词序列，并满足：
    每对相邻的单词之间仅有单个字母不同。
    转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList 中的单词。
    sk == endWord
给你两个单词 beginWord 和 endWord ，以及一个字典 wordList 。
请你找出并返回所有从 beginWord 到 endWord 的 最短转换序列 ，
如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk] 的形式返回。

示例 1：
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
解释：存在 2 种最短的转换序列：
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

示例 2：
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：[]
解释：endWord "cog" 不在字典 wordList 中，所以不存在符合要求的转换序列。

提示：
1 <= beginWord.length <= 7
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord、endWord 和 wordList[i] 由小写英文字母组成
beginWord != endWord
wordList 中的所有单词 互不相同
"""

import itertools
import collections
from typing import List


class Solution:
    @staticmethod
    def edit_distance(word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = i

        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[-1][-1]

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 使用通配符构造邻接表（每个单词的任意子串作为两个节点之间的边）
        hash = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                hash[word[:i] + "*" + word[i + 1:]].append(word)

        # 生成需要访问的路径队列
        queue = [[beginWord, [beginWord]]]
        # 生成已访问节点
        visited = set()
        visited.add(beginWord)
        # 保存结果
        res = []

        while queue:
            new_visited = set()
            # 依次输出队列中所有路径
            for _ in range(len(queue)):
                word, path = queue.pop()
                # 如果当前节点是endWord，保存路径
                if word == endWord:
                    res.append(path)

                # 访问该节点所有边
                for i in range(len(word)):
                    masked_word = word[:i] + "*" + word[i + 1:]
                    # 访问该节点通过这条边能够访问的所有节点
                    for j in hash[masked_word]:
                        # 因为是求最短路径，所以如果节点已经访问过则不再访问
                        if j in visited:
                            continue
                        else:
                            queue.insert(0, [j, path + [j]])
                            new_visited.add(j)
            # 更新已经访问过的节点
            visited |= new_visited

        return res

    def findLadders2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        def helper(beginWord: str, endWord: str, wordList: List[str], max_len, tmp=[]):
            if endWord not in wordList:
                return []
            # new_begin_words = [word for word in wordList if self.edit_distance(beginWord, word) == 1]
            new_begin_words = set([k[1] if k[0] == beginWord else k[0] for k, v in word_word_ed.items()
                                   if v == 1 and beginWord in k])
            new_word_list = wordList[:]
            tmp2 = tmp[:]
            for word in new_begin_words:
                if word not in tmp:
                    tmp.append(word)
                else:
                    continue
                if len(tmp) < max_len:
                    if (word, endWord) in word_word_ed:
                        ed = word_word_ed.get((word, endWord))
                    else:
                        ed = word_word_ed.get((endWord, word))

                    if ed <= 1:
                        if word != endWord:
                            tmp.append(endWord)
                        if not res:
                            res.append(tmp[:])
                        elif len(tmp) < len(res[-1]):
                            res.clear()
                            res.append(tmp[:])
                        elif len(tmp) == len(res[-1]):
                            res.append(tmp[:])
                    else:
                        new_word_list = list(set(new_word_list) - set(new_begin_words))
                        helper(word, endWord, new_word_list, max_len, tmp)
                tmp = tmp2[:]

        res = []
        word_word_ed = {(w1, w2): self.edit_distance(w1, w2) for w1, w2 in itertools.combinations(
            set([beginWord] + wordList + [endWord]), 2)}
        helper(beginWord, endWord, wordList, len(wordList)+1, [])
        res = [[beginWord] + r for r in res]
        return res

    def findLadders0(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        def helper(beginWord: str, endWord: str, wordList: List[str], tmp=[]):
            if endWord not in wordList:
                return []
            new_begin_words = [word for word in wordList if self.edit_distance(beginWord, word) == 1]
            new_word_list = wordList[:]
            tmp2 = tmp[:]
            for word in new_begin_words:
                tmp.append(word)
                if self.edit_distance(word, endWord) <= 1:
                    if word != endWord:
                        tmp.append(endWord)
                    if not res:
                        res.append(tmp[:])
                    elif len(tmp) < len(res[-1]):
                        res.clear()
                        res.append(tmp[:])
                    elif len(tmp) == len(res[-1]):
                        res.append(tmp[:])
                else:
                    new_word_list = list(set(new_word_list) - set(new_begin_words))
                    helper(word, endWord, new_word_list, tmp)
                tmp = tmp2[:]

        res = []
        helper(beginWord, endWord, wordList, [])
        res = [[beginWord] + r for r in res]
        return res


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "cot", "dot", "dog", "lot", "log", "cog"]

    beginWord = "qa"
    endWord = "sq"
    wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca",
     "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au",
     "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga",
     "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er",
     "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]

    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log"]
    print(Solution().findLadders(beginWord, endWord, wordList))
