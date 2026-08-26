from typing import Literal

PATTERNS = (
    "hash-map/set",
    "two-pointers",
    "fixed-window",
    "variable-window",
    "prefix-sums",
    "monotonic-stack",
    "stack/queue",
    "binary-search",
    "BFS",
    "DFS/backtracking",
    "heap/priority-queue",
    "topological-sort",
    "union-find",
    "greedy",
    "DP-1D",
    "DP-2D",
    "Dijkstra",
    "segment-tree",
    "trie",
    "two-heaps",
)

Pattern = Literal[
    "hash-map/set",
    "two-pointers",
    "fixed-window",
    "variable-window",
    "prefix-sums",
    "monotonic-stack",
    "stack/queue",
    "binary-search",
    "BFS",
    "DFS/backtracking",
    "heap/priority-queue",
    "topological-sort",
    "union-find",
    "greedy",
    "DP-1D",
    "DP-2D",
    "Dijkstra",
    "segment-tree",
    "trie",
    "two-heaps",
]


def pattern_quiz() -> dict[str, Pattern]:
    # Pattern: this exercise IS the cue-recognition drill itself (see
    # LESSON.md's Cue Map) rather than a single module's pattern. Each
    # answer below cites the cue that gives it away.
    return {
        "q1": "hash-map/set",  # "appears more than once" -> seen-before lookup
        "q2": "two-pointers",  # sorted + two values hit a target
        "q3": "fixed-window",  # "7 consecutive days" -> exact-size window
        "q4": "variable-window",  # "longest ... no more than 2 distinct" -> shrink/grow window
        "q5": "prefix-sums",  # "sum to exactly zero", values can be negative -> prefix + hash map
        "q6": "monotonic-stack",  # "days until a strictly higher price" -> next greater element
        "q7": "stack/queue",  # "properly nested" -> LIFO matching
        "q8": "binary-search",  # sorted + "smallest score at least X" -> lower bound
        "q9": "BFS",  # "minimum number of hops", unweighted graph
        "q10": "DFS/backtracking",  # "generate every possible combination"
        "q11": "heap/priority-queue",  # "top 5" from a live/streaming feed
        "q12": "topological-sort",  # dependency-ordered install order
        "q13": "union-find",  # online connectivity queries after each edge
        "q14": "greedy",  # max non-overlapping intervals -> earliest-finish-time greedy
        "q15": "DP-1D",  # "distinct ways to climb" -> 1-D counting recurrence
        "q16": "DP-2D",  # edit distance between two strings -> two-sequence DP
        "q17": "Dijkstra",  # cheapest cost to ALL nodes, non-negative weights
        "q18": "segment-tree",  # range query AND frequent point updates
        "q19": "trie",  # autocomplete over a dictionary of strings
        "q20": "two-heaps",  # running median of a stream
    }
