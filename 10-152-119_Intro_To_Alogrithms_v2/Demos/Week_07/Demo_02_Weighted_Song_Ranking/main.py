"""Explain deterministic top-k ranking with normalized weighted tag similarity."""

import argparse
from math import isfinite

SONGS = [{"id": "S01", "tags": ["calm", "piano"]},
         {"id": "S02", "tags": ["calm", "acoustic"]},
         {"id": "S03", "tags": ["piano"]}, {"id": "S04", "tags": []}]


def weighted_similarity(tags, profile, weights):
    if any(type(value) not in (int, float) or not isfinite(value) or value < 0
           for value in weights.values()):
        raise ValueError("weights must be finite nonnegative numbers")
    tags, profile = set(tags), set(profile)
    union, matched = tags | profile, tags & profile
    contributions = {tag: weights.get(tag, 1) for tag in sorted(matched)}
    numerator = sum(contributions.values())
    denominator = sum(weights.get(tag, 1) for tag in union)
    score = numerator / denominator if denominator else 0.0
    return score, contributions, denominator


def rank_songs(songs, profile, weights, k=4):
    if type(k) is not int or k < 0:
        raise ValueError("k must be a nonnegative integer")
    scored = [(song["id"], *weighted_similarity(song.get("tags") or [], profile, weights))
              for song in songs]
    return sorted(scored, key=lambda row: (-row[1], row[0]))[:k]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--emphasis", choices=["calm", "piano"], default="calm")
    args = parser.parse_args()
    profile = {"calm", "piano"}
    print("WEIGHTED SONG RANKING: sum matched weights / sum union weights")
    print("Unspecified tag weight=1; empty or zero-weight union score=0; ties use ID.")
    for label, weights in (("Baseline (all weights 1)", {}),
                           (f"Emphasize {args.emphasis} (weight 4)", {args.emphasis: 4})):
        print(f"\n{label}")
        for place, (song_id, score, contributions, denominator) in enumerate(
                rank_songs(SONGS, profile, weights), 1):
            print(f"{place}. {song_id}: score={score:.3f}; matched={contributions}; union weight={denominator}")
    print("A defensible change in weights can change recommendations; no ML training is involved.")


if __name__ == "__main__":
    main()
