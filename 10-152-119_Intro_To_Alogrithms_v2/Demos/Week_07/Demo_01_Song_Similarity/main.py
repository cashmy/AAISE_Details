"""Compare raw overlap and Jaccard similarity on authored fictional song tags."""

SONGS = [
    {"id": "S01", "title": "Quiet Keys", "tags": ["calm", "piano"]},
    {"id": "S02", "title": "Soft Strings", "tags": ["calm", "acoustic"]},
    {"id": "S03", "title": "Piano Focus", "tags": ["piano"]},
    {"id": "S04", "title": "Unknown Track", "tags": None},
    {"id": "S05", "title": "Broad Mix", "tags": ["calm", "piano", "rock", "jazz", "upbeat", "acoustic"]},
]


def shared_count(left, right):
    return len(set(left) & set(right))


def jaccard(left, right):
    left, right = set(left), set(right)
    union = left | right
    return len(left & right) / len(union) if union else 0.0


def score_songs(songs, profile):
    scored = []
    for song in songs:
        tags = set(song.get("tags") or [])
        scored.append((song["id"], shared_count(tags, profile), jaccard(tags, profile),
                       sorted(tags & set(profile))))
    return scored


def main():
    profile = {"calm", "piano"}
    print("SONG SIMILARITY: fictional tags, not objective musical truth")
    print("Profile:", sorted(profile), "; empty union score=0; unknown tags become empty")
    scored = score_songs(SONGS, profile)
    print(f"\n{'ID':<5} {'Count':>6} {'Jaccard':>10} Matched tags")
    for song_id, count, normalized, matched in scored:
        print(f"{song_id:<5} {count:>6} {normalized:>10.3f} {matched}")
    print("Count order:", [row[0] for row in sorted(scored, key=lambda row: (-row[1], row[0]))])
    print("Jaccard order:", [row[0] for row in sorted(scored, key=lambda row: (-row[2], row[0]))])
    print("Normalization distinguishes a focused match from a broad tag collection.")


if __name__ == "__main__":
    main()
