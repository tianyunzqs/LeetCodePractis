# -*- coding: utf-8 -*-
# @Time        : 2019/7/2 16:55
# @Author      : tianyunzqs
# @Description : 

"""
68. Text Justification
Hard


Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""


def full_line(line_list, maxWidth, is_last=False):
    words_len = sum([len(w) for w in line_list])
    space_len = maxWidth - words_len
    space_num = len(line_list) - 1
    if space_num == 0:
        return line_list[0] + ' ' * (maxWidth - len(line_list[0]))
    if is_last:
        return ' '.join(line_list) + ' ' * (space_len - 1)

    every_space_num = space_len // space_num
    more_space = space_len % space_num
    tmp_str = ''
    for i, w in enumerate(line_list):
        if i < more_space:
            tmp_str += w + ' ' * (every_space_num + 1)
        else:
            if i == space_num:
                tmp_str += w
            else:
                tmp_str += w + ' ' * every_space_num

    return tmp_str


def fullJustify(words, maxWidth: int):
    result = []
    line_list = []
    line_word_len = 0
    for word in words:
        if line_word_len + len(word) + 1 > maxWidth:
            if line_word_len + len(word) == maxWidth:
                line_list.append(word)
                result.append(' '.join(line_list))
                line_word_len = 0
                line_list = []
            else:
                result.append(full_line(line_list, maxWidth))
                line_word_len = len(word) + 1
                line_list = [word]

        else:
            line_word_len += len(word) + 1
            line_list.append(word)

    if line_list:
            result.append(full_line(line_list, maxWidth, is_last=True))

    return result


words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
words = ["What","must","be","acknowledgment","shall","be"]
# words = ["This", "is", "an", "example", "of", "text", "justification."]
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
words = ["My","momma","always","said,","\"Life","was","like","a","box","of","chocolates.","You","never","know","what","you're","gonna","get."]

for res in fullJustify(words, 20):
    print(res)
