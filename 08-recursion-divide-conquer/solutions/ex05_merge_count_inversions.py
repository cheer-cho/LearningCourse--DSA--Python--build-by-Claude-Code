def count_inversions(nums: list[int]) -> int:
    # Pattern: divide & conquer riding along with merge sort. Split in
    # half, solve each half recursively (returns a sorted copy + its
    # inversion count), combine by merging while counting cross-half
    # inversions: whenever a right-half element is placed before the
    # remaining left-half elements, each of those forms an inversion.
    # Time: O(n log n), Space: O(n).
    def sort_and_count(arr: list[int]) -> tuple[list[int], int]:
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, left_count = sort_and_count(arr[:mid])
        right, right_count = sort_and_count(arr[mid:])

        merged: list[int] = []
        i = j = 0
        cross_count = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                cross_count += len(left) - i
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, left_count + right_count + cross_count

    _, total = sort_and_count(nums)
    return total
