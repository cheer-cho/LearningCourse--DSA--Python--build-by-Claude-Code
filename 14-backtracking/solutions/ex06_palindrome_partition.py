def palindrome_partitions(s: str) -> list[list[str]]:
    # Pattern: backtracking, combinations-by-position — the "choice" at
    # each step is where the next piece ends; pruning = only recurse
    # into pieces that are themselves palindromes.
    # Why: a valid full partition is a sequence of valid next-pieces,
    # so trying every possible next-piece length and checking the
    # palindrome property before recursing is exactly choose/explore.
    # Complexity: O(n * 2^n) time worst case, O(n) recursion depth.
    results: list[list[str]] = []
    path: list[str] = []

    def is_palindrome(piece: str) -> bool:
        return piece == piece[::-1]

    def backtrack(start: int) -> None:
        if start == len(s):
            results.append(path.copy())
            return
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if not is_palindrome(piece):
                continue
            path.append(piece)
            backtrack(end)
            path.pop()

    backtrack(0)
    return results
