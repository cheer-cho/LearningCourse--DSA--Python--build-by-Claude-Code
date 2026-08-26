# Scenario: a CLI tool that lets users type an abbreviated command name
# ("st" for "status") — every command needs the shortest prefix that
# still identifies it uniquely, and the tool also wants the longest
# stretch every command name agrees on (for a shared help-text banner).
# Pattern: trie with pass-through counters (same idea as ex03) for the
# unique-prefix half; a plain trie spine walk for the common-prefix half.
# Run: uv run pytest 13-tries -k ex05


def shortest_unique_prefix(words: list[str]) -> list[str]:
    """For each word in `words`, return its shortest prefix that is not
    a prefix of any OTHER word in the list. Output is in the same
    order as `words`.

    Precondition: `words` has no duplicate entries (a word can't be
    "unique" from an identical twin — that's outside this exercise's
    scope).

    shortest_unique_prefix(["dog", "dove", "duck", "dodge"])
        -> ["dog", "dov", "du", "dod"]
    shortest_unique_prefix(["cat"]) -> ["c"]   (alone -> its first char is enough)

    Pin: if a word is itself a prefix of another word in the list (so
    no proper prefix — not even the full word — is unique to it), its
    entry in the result is the FULL word, e.g.
    shortest_unique_prefix(["do", "dog"]) -> ["do", "dog"].

    Build one trie over all of `words` where every node carries a
    pass-through counter (how many words go through it — same idea as
    `PrefixCounter` in ex03). Then, per word, walk from the root and
    stop at the first node whose counter is 1 — no other word reaches
    that point, so that prefix belongs to this word alone.

    Target complexity: O(N) time/space, N = total characters across
    `words` (build once, then one bounded walk per word).
    """
    raise NotImplementedError


def longest_common_prefix_all(words: list[str]) -> str:
    """Return the longest prefix shared by EVERY string in `words`.
    `""` if `words` is empty or the strings share no common prefix.

    longest_common_prefix_all(["flower", "flow", "flight"]) -> "fl"
    longest_common_prefix_all(["dog", "cat"]) -> ""
    longest_common_prefix_all(["same", "same"]) -> "same"
    longest_common_prefix_all([]) -> ""

    The classic alternative sorts `words` and compares only the first
    and last strings post-sort (their common prefix bounds everyone
    else's) — simple, but pays an O(n log n) sort just to answer one
    prefix question. The trie version builds the same structure this
    module has used all along: insert every word, then walk down the
    trie's "spine" — follow the single child a node has for as long as
    it has EXACTLY one child and no word ends there. The moment a node
    branches (more than one child) or a word terminates, the shared
    prefix can't extend any further.

    Target complexity: O(N) time, N = total characters across `words`.
    """
    raise NotImplementedError
