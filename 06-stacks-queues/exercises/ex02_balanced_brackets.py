# Scenario: a code-formatting linter checks bracket nesting before it
# ever touches syntax highlighting. Concepts: stack as "the most recent
# unresolved opener"; interleaving traps; when a counter beats a stack.
# Run: uv run pytest 06-stacks-queues -k ex02


def is_balanced(s: str) -> bool:
    """Return True if every bracket in `s` is closed in the right order.

    `s` may contain '()[]{}' plus any other characters, which are
    ignored. A closer must match the MOST RECENT unclosed opener —
    interleaved brackets like "([)]" are NOT balanced even though each
    bracket type appears the same number of times on each side.

    is_balanced("f([a, b])") -> True
    is_balanced("([)]") -> False
    is_balanced("(]") -> False
    is_balanced(")(") -> False
    is_balanced("") -> True

    Target complexity: O(n) time, O(n) space.
    """
    raise NotImplementedError


def min_removals_to_balance(s: str) -> int:
    """Return the minimum number of characters to delete from `s` so
    what remains is balanced, counting only '(' and ')'.

    `s` may contain other characters besides '(' and ')' — they are
    ignored (not counted, not removed).

    min_removals_to_balance("()") -> 0
    min_removals_to_balance("(()") -> 1
    min_removals_to_balance("())(") -> 2
    min_removals_to_balance(")(") -> 2
    min_removals_to_balance("") -> 0
    min_removals_to_balance("a(b(c)d") -> 1

    Target complexity: O(n) time, O(1) extra space — you only ever need
    a running COUNT of unmatched openers, not a real stack.
    """
    raise NotImplementedError
