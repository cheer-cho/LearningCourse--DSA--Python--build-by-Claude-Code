def reverse_words(s: str) -> str:
    # Pattern: build-then-join. `split()` with no argument already treats
    # any run of whitespace as one separator and drops empty pieces, so
    # the "collapse extra spaces" requirement falls out for free.
    # Time: O(n) — split, reverse, and join are each linear. Space: O(n).
    words = s.split()
    words.reverse()
    return " ".join(words)


def run_length_encode(s: str) -> str:
    # Pattern: build-then-join with a reader/writer-style scan. Never
    # concatenate onto a growing string in a loop (each `+=` would copy
    # the whole string so far — O(n^2) total); collect pieces in a list
    # and join once.
    # Time: O(n) — one pass over s. Space: O(n) for the pieces + result.
    if not s:
        return ""
    pieces: list[str] = []
    current_char = s[0]
    run_length = 1
    for ch in s[1:]:
        if ch == current_char:
            run_length += 1
        else:
            pieces.append(current_char + str(run_length))
            current_char = ch
            run_length = 1
    pieces.append(current_char + str(run_length))
    return "".join(pieces)


def run_length_decode(s: str) -> str:
    # Pattern: build-then-join. Scan (character, digit-run) pairs and
    # expand each into `count` copies of `character` via string
    # repetition, collecting pieces instead of concatenating in the loop.
    # Time: O(n) where n is the decoded length. Space: O(n).
    pieces: list[str] = []
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        digits_start = i
        while i < len(s) and s[i].isdigit():
            i += 1
        count = int(s[digits_start:i])
        pieces.append(char * count)
    return "".join(pieces)
