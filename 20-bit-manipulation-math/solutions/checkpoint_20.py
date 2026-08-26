def parity_report(packets: list[int]) -> dict[str, object]:
    # Pattern: Kernighan popcount per packet + XOR fold across all
    # packets for the checksum. Time: O(sum of popcounts). Space:
    # O(n) for the output list.
    bit_counts = []
    checksum = 0
    for packet in packets:
        n = packet
        count = 0
        while n:
            n &= n - 1
            count += 1
        bit_counts.append(count)
        checksum ^= packet
    return {"per_packet_bit_counts": bit_counts, "overall_checksum": checksum}


def find_faulty_sensor(readings: list[int]) -> int:
    # Pattern: XOR fold. Every duplicated pair cancels to 0, leaving
    # the unpaired reading. Time: O(n). Space: O(1).
    result = 0
    for reading in readings:
        result ^= reading
    return result


def firmware_grid_rotate(grid: list[list[int]]) -> None:
    # Pattern: transpose + reverse rows. Time: O(n^2). Space: O(1).
    n = len(grid)
    for r in range(n):
        for c in range(r + 1, n):
            grid[r][c], grid[c][r] = grid[c][r], grid[r][c]
    for row in grid:
        row.reverse()


def prime_channel_ids(limit: int) -> list[int]:
    # Pattern: Sieve of Eratosthenes, crossing multiples starting at
    # p*p. Time: O(limit log log limit). Space: O(limit).
    if limit < 2:
        return []
    is_composite = [False] * (limit + 1)
    primes = []
    for p in range(2, limit + 1):
        if not is_composite[p]:
            primes.append(p)
            for multiple in range(p * p, limit + 1, p):
                is_composite[multiple] = True
    return primes
