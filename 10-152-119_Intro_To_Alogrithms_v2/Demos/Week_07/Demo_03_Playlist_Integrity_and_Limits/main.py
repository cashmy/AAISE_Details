"""A reproducible local metadata digest does not validate recommendation quality."""

from copy import deepcopy
import hashlib
import json

PLAYLIST = [{"id": "S01", "title": "Quiet Keys", "tags": ["calm", "piano"]},
            {"id": "S02", "title": "Soft Strings", "tags": ["calm", "acoustic"]}]


def canonical_bytes(playlist):
    ids = [song["id"] for song in playlist]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate song IDs")
    normalized = [{"id": song["id"], "title": song["title"],
                   "tags": sorted(set(song.get("tags") or []))} for song in playlist]
    normalized.sort(key=lambda song: song["id"])
    return json.dumps(normalized, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def digest(playlist):
    return hashlib.sha256(canonical_bytes(playlist)).hexdigest()


def rank(playlist, profile):
    scores = []
    for song in playlist:
        tags = set(song.get("tags") or [])
        union = tags | profile
        score = len(tags & profile) / len(union) if union else 0
        scores.append((song["id"], score))
    return sorted(scores, key=lambda row: (-row[1], row[0]))


def main():
    print("PLAYLIST INTEGRITY AND RECOMMENDATION LIMITS")
    profile = {"calm", "piano"}
    print("Baseline ranking:", rank(PLAYLIST, profile))
    missing = deepcopy(PLAYLIST)
    missing[0]["tags"] = []
    print("Missing S01 tags changes ranking:", rank(missing, profile))
    print("The music did not change; the authored metadata did.")
    original_digest = digest(PLAYLIST)
    renamed = deepcopy(PLAYLIST)
    renamed[0]["title"] = "Quiet Keys (edited title)"
    print("\nCanonical fields: ID, title, unique sorted tags; record order ignored.")
    print("Original SHA-256:", original_digest)
    print("Edited SHA-256:  ", digest(renamed))
    print("Title-only edit leaves tag ranking unchanged:", rank(renamed, profile))
    print("A digest checks this serialized snapshot, not authenticity, fairness, or source correctness.")
    print("Hashing metadata is not hashing audio, computing similarity, or encrypting data.")


if __name__ == "__main__":
    main()
