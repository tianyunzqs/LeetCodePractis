# -*- coding: utf-8 -*-
# @Time        : 2019/6/16 13:39
# @Author      : tianyunzqs
# @Description ：

"""
30. Substring with Concatenation of All Words
Hard

You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once
and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
"""


def findSubstring(s, words):
    if not s or not words or not words[0]:
        return []
    result = []
    item_len = len(words[0])
    words_str_len = item_len * len(words)
    words_str = ''.join(sorted(words))
    for i in range(len(s) - words_str_len + 1):
        candidate_words = [s[i + cnt*item_len: i + (cnt+1)*item_len] for cnt in range(len(words))]
        candidate_words_sorted = sorted(candidate_words)
        if ''.join(candidate_words_sorted) == words_str:
            result.append(i)

    return result


if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    print(findSubstring(s=s, words=words))