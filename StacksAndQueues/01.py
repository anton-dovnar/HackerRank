"""
Balanced Brackets

A bracket is considered to be any one of the following characters:
(, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket
(i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or })
of the exact same type. There are three types of matched pairs of
brackets: [], {}, and ().
"""


def is_balanced(s: str) -> str:
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    stack = []
    for b in s:
        if b not in brackets:
            stack.append(b)
        else:
            if not stack:
                return "NO"
            last_bracket = stack.pop()
            if brackets[b] != last_bracket:
                return "NO"

    return "YES" if not stack else "NO"


if __name__ == '__main__':
    s = '{{}('
    print(is_balanced(s))
