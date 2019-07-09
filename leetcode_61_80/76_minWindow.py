# -*- coding: utf-8 -*-
# @time        : 2019/7/9 12:05
# @Author      : tianyunzqs
# @Description : 

"""
76. Minimum Window substring
Hard

Given a string s and a string t,
find the minimum window in s which will contain all the characters in t in complexity O(n).

Example:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Note:

If there is no such window in s that covers all characters in t, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in s.
"""

from collections import Counter


def minWindow1(s: str, t: str) -> str:
    """
    依次遍历源字符串s，并将其元素存入计数器中，
    若计数器中包含目标字符串t中的所有元素，则更新最佳位置下标，
    同时在计数器中去除源字符串中第i个位置的元素，i向前移动一步。
    :param s:
    :param t:
    :return:
    """
    tc = Counter(t)
    sc = Counter()

    best_i, best_j = 0, len(s)
    i = 0
    for j, char in enumerate(s):
        sc[char] += 1

        while sc & tc == tc:
            if j - i < best_j - best_i:
                best_i, best_j = i, j

            sc[s[i]] -= 1
            i += 1

    return s[best_i: best_j + 1] if best_j - best_i < len(s) else ""


def minWindow2(s: str, t: str) -> str:
    """
    时间复杂度O(N^2)
    保存t中元素在s中的下标，比较两两下标区间内容是否包含t，取最小长度的区间返回
    :param s:
    :param t:
    :return:
    """
    Cs = Counter(s)
    Ct = Counter(t)
    if Cs & Ct != Ct:
        return ''

    idxs = [i for i, ch in enumerate(s) if ch in t]
    if len(idxs) == 1:
        return s[idxs[0]]

    min_wind = s
    for _i, i in enumerate(idxs):
        for j in idxs[_i+1:]:
            if Counter(s[i: j+1]) & Ct == Ct:
                min_wind = s[i: j+1] if len(min_wind) > j-i+1 else min_wind
                break

    return min_wind


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "AABC"
    s = "ab"
    t = "a"
    s = "bdab"
    t = "ab"
    s = "xeaifhaqslynbcwxncwgeezbrjorzyuwevejcecuscjvgfutkrcqxbromihlgcjnzpybwcxqeglknhgzyiqxljnyrvlazvnyklbgoywugjftrltrvlrgueeobsoandazqbigbgbhqgdjtycojtwfydtbvjekmejdirjlymvquybnyddjxaoxfkyatckijvlrnwcnjxfdxgtvjweiyvfdhefaipkrnviaunpfmukkcdhlcmwcjbgqhnsqfdhsasuwhjbtfmdhrluvzqykugcbtutyzdqcxkyevaxcodjhogdpwbzsjducxpdzsvbpizvfbtirwtzmzebyhcqqfmueczdwveofgjkhesbamaolgrlpvcfcqbhubmtythdzspizijbwlqjrjvgfznhprqmudfsyoxzimhhutjsebcykxgpywznnpbhuizuwythkbohwzzacbanyhewdfmsvpzryamuyhdkkurgvrjysjntqrrvxfnuvonvqbrqjvbvpucklligu"
    t = "xbnpukocakzqzuhdlxoga"
    s = "tkopjjgknziznmfwvkgospwkujjklzugjiwvuefhepiteppbzyptplekwnwjmqqybovvsccyrnuxclyclnvbaznxojgdzydcmyxhacftpbrrnrvyftbfuoelxlozjtbyrbftdkoumhnbzlzgeblarslpdbqoutmnwrgzexvsejtfwulcxzcprqgwrykorxboqkpwhnonyjvuggwdfauyqauiafyseziwjztsojimvdiblegrhdrxdmhetfyxfitqjolaytmtyxwjdeckhuingptbxtyedtumihmgcbbayxkbdomliwyqnrrkmropllbvsqbvtexrdjugyirierzsksewktlxepsyhvvabttecpkayejevkyiedeqwsncjhascwudrnjteuwcahhxtffxkmoggdkpllhpjbvcqevuatzaaiyvpftarjixmtoxgxnraitsoqnpkormwpilxbnomwoypcwvclocvhvlxkajaswwjejghzxtvltmprjrcxwzetldfnnffjdrpoxynurkhmwxefqieoikhvooibvqmyhdpgbcdunkgljktatxqdiaywoizkynkhqzqretntftepgxrzvjcdjcbykcklpwufykycfnvngzcmzvnwerzotcogearvwncuaayfptsvvwkwtzsyrtokveqbgjwexyzxazepvzmqvymryeppxfbuluvrdtvcrwbtwikthwjevxvvdmmcrnyehvvnotrhrvcndmgkirofqkavwmzqcxwluuyinsrentuqfccqwqvocykbmltolpafjaqyshfhbbzidbybuwqwuczgnsxykxgvxwusdbbgcbrfcpjwnzvhbuqqpnrzmxujtqdyrfhvgydkpmjdlemoacgprzqdwnprfssxzz"
    t = "ufzxqojzrufekhitzcsphr"
    import time
    t1 = time.time()
    print(minWindow1(s, t))
    t2 = time.time()
    print(minWindow2(s, t))
    t3 = time.time()
    print(t2 - t1)
    print(t3 - t2)
