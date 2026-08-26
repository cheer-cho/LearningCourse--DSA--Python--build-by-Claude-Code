def heap_sort(nums: list[int]) -> list[int]:
    # Pattern: classic in-place heap sort on a MAX-heap.
    # 1) heapify bottom-up: O(n).
    # 2) n rounds of "swap max to the tail, shrink heap by one, sift
    #    down the new root": O(log n) each -> O(n log n) total.
    # Time: O(n log n). Space: O(n) for the working copy, O(1) extra.
    arr = list(nums)
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        _sift_down(arr, i, n)

    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        _sift_down(arr, 0, end)

    return arr


def _sift_down(arr: list[int], i: int, size: int) -> None:
    while True:
        left, right = 2 * i + 1, 2 * i + 2
        largest = i
        if left < size and arr[left] > arr[largest]:
            largest = left
        if right < size and arr[right] > arr[largest]:
            largest = right
        if largest == i:
            break
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest
