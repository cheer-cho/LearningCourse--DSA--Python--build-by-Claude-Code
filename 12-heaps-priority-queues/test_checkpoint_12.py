import random

import pytest
from checkpoint_12 import TriageQueue, k_most_urgent


def test_triage_queue_starts_empty():
    q = TriageQueue()
    assert q.waiting_count() == 0


def test_triage_queue_serves_highest_severity_first():
    q = TriageQueue()
    q.arrive("Alice", severity=2, timestamp=1.0)
    q.arrive("Bob", severity=5, timestamp=2.0)
    assert q.next_patient() == "Bob"
    assert q.next_patient() == "Alice"


def test_triage_queue_fifo_within_same_severity():
    q = TriageQueue()
    q.arrive("Alice", severity=3, timestamp=5.0)
    q.arrive("Bob", severity=3, timestamp=1.0)
    q.arrive("Cy", severity=3, timestamp=3.0)
    assert [q.next_patient() for _ in range(3)] == ["Bob", "Cy", "Alice"]


def test_triage_queue_waiting_count_tracks_arrivals_and_departures():
    q = TriageQueue()
    q.arrive("Alice", severity=1, timestamp=1.0)
    q.arrive("Bob", severity=2, timestamp=2.0)
    assert q.waiting_count() == 2
    q.next_patient()
    assert q.waiting_count() == 1


def test_triage_queue_next_patient_on_empty_raises():
    q = TriageQueue()
    with pytest.raises(IndexError):
        q.next_patient()


def test_triage_queue_mixed_severities_and_arrivals():
    q = TriageQueue()
    q.arrive("Low1", severity=1, timestamp=1.0)
    q.arrive("High1", severity=5, timestamp=2.0)
    q.arrive("Mid1", severity=3, timestamp=3.0)
    q.arrive("High2", severity=5, timestamp=4.0)
    q.arrive("Low2", severity=1, timestamp=5.0)

    order = [q.next_patient() for _ in range(5)]
    assert order == ["High1", "High2", "Mid1", "Low1", "Low2"]


def test_k_most_urgent_typical():
    records = [("Alice", 2, 1.0), ("Bob", 5, 2.0), ("Cy", 5, 0.5)]
    assert k_most_urgent(records, 2) == ["Cy", "Bob"]


def test_k_most_urgent_k_equals_all():
    records = [("Alice", 1, 1.0), ("Bob", 2, 2.0)]
    assert k_most_urgent(records, 2) == ["Bob", "Alice"]


def test_k_most_urgent_single_record():
    assert k_most_urgent([("Solo", 1, 0.0)], 1) == ["Solo"]


def test_triage_queue_large_stress_efficiency():
    rng = random.Random(42)
    q = TriageQueue()
    arrived = 0
    for i in range(100_000):
        if arrived == 0 or rng.random() < 0.6:
            q.arrive(f"patient-{i}", rng.randint(1, 10), float(i))
            arrived += 1
        else:
            q.next_patient()
            arrived -= 1
    assert q.waiting_count() == arrived


def test_triage_queue_matches_brute_force_ordering():
    rng = random.Random(5)
    q = TriageQueue()
    records = []
    for i in range(200):
        name = f"p{i}"
        severity = rng.randint(1, 5)
        timestamp = float(i)
        q.arrive(name, severity, timestamp)
        records.append((name, severity, timestamp))

    expected_order = [
        name
        for name, _severity, _timestamp in sorted(
            records, key=lambda r: (-r[1], r[2])
        )
    ]
    actual_order = [q.next_patient() for _ in range(len(records))]
    assert actual_order == expected_order
