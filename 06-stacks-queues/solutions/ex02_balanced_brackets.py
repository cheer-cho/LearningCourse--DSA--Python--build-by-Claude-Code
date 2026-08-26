_CLOSERS_TO_OPENERS = {")": "(", "]": "[", "}": "{"}
_OPENERS = set(_CLOSERS_TO_OPENERS.values())


def is_balanced(s: str) -> bool:
    # Pattern: stack of unresolved openers — each closer must match the
    # MOST RECENT opener (top of stack). That LIFO check is exactly
    # what rules out interleaving like "([)]", which a same-count
    # comparison per bracket type would wrongly accept.
    # Complexity: O(n) time, O(n) space.
    stack: list[str] = []
    for ch in s:
        if ch in _OPENERS:
            stack.append(ch)
        elif ch in _CLOSERS_TO_OPENERS and (
            not stack or stack.pop() != _CLOSERS_TO_OPENERS[ch]
        ):
            return False
    return not stack


def min_removals_to_balance(s: str) -> int:
    # Pattern: a single counter of unmatched '(' replaces the stack —
    # we only ever need the COUNT of pending openers, never their
    # identity (there's only one bracket type here). Anything that
    # isn't '(' or ')' is ignored.
    # Complexity: O(n) time, O(1) space.
    open_count = 0
    removals = 0
    for ch in s:
        if ch == "(":
            open_count += 1
        elif ch == ")":
            if open_count > 0:
                open_count -= 1
            else:
                removals += 1
    return removals + open_count
