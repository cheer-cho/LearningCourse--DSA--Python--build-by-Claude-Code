ANSWER_SET = {"O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)", "O(2^n)"}


def classify_snippets() -> dict[str, str]:
    # Pattern: read complexity from code shape (sequential adds, nested
    # multiplies, halving is log, branching recursion is exponential).
    # No loops/recursion at runtime here — this is a fixed lookup table.
    return {
        "constant_lookup": "O(1)",
        "print_all": "O(n)",
        "binary_search_style": "O(log n)",
        "two_separate_loops": "O(n)",
        "sort_then_scan": "O(n log n)",
        "nested_loop_all_pairs": "O(n^2)",
        "triangular_nested_loop": "O(n^2)",
        "recursive_subsets": "O(2^n)",
    }
