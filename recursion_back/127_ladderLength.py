# -*- coding: utf-8 -*-
# @Time        : 2021/5/27 16:57
# @Author      : tianyunzqs
# @Description :

"""
127. 单词接龙
字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列：

序列中第一个单词是 beginWord 。
序列中最后一个单词是 endWord 。
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典 wordList 中的单词。
给你两个单词 beginWord 和 endWord 和一个字典 wordList ，找到从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。
如果不存在这样的转换序列，返回 0。


示例 1：
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。

示例 2：
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。


提示：
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord、endWord 和 wordList[i] 由小写英文字母组成
beginWord != endWord
wordList 中的所有字符串 互不相同
"""

import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
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
        min_length = 0

        while queue:
            new_visited = set()
            # 依次输出队列中所有路径
            for _ in range(len(queue)):
                word, path = queue.pop()
                # 如果当前节点是endWord，保存路径
                if word == endWord:
                    # res.append(path)
                    min_length = min(min_length, len(path)) if min_length else len(path)

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

        return min_length


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

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    print(Solution().ladderLength(beginWord, endWord, wordList))

