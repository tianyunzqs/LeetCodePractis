# -*- coding: utf-8 -*-
# @Time        : 2019/7/3 16:02
# @Author      : tianyunzqs
# @Description : 

"""
71. Simplify Path
Medium


Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.



Example 1:

Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:

Input: "/a/./b/../../c/"
Output: "/c"
Example 5:

Input: "/a/../../b/../c//.//"
Output: "/c"
Example 6:

Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
"""


def simplifyPath(path: str) -> str:
    path_parts = path.split('/')
    path_parts = list(filter(None, path_parts))
    result = []
    for p in path_parts:
        if p == '.':
            continue
        if p == '..':
            if result:
                result.pop()
        else:
            result.append(p)

    if not result:
        return '/'
    else:
        result.insert(0, '')
        return '/'.join(result)


path = "/a//b////c/d//././/.."
path = "/a/../../b/../c//.//"
path = "/a/./b/../../c/"
path = "/home//foo/"
path = "/../"
path = "/home/"
print(simplifyPath(path))
