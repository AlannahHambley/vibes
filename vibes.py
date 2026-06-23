import argparse
import random

PLAYLISTS = {
    "happy": [
        "Happy - Pharrell Williams",
        "Can't Stop the Feeling - Justin Timberlake",
        "Uptown Funk - Bruno Mars",
        "Good as Hell - Lizzo",
        "Walking on Sunshine - Katrina and the Waves",
    ],
    "sad": [
        "The Night We Met - Lord Huron",
        "Someone Like You - Adele",
        "Fix You - Coldplay",
        "Skinny Love - Bon Iver",
        "Liability - Lorde",
    ],
    "chill": [
        "Redbone - Childish Gambino",
        "Motion Picture Soundtrack - Radiohead",
        "Coffee - beabadoobee",
        "Sunset Lover - Petit Biscuit",
        "Breathe - Télépopmusik",
    ],
    "hype": [
        "HUMBLE. - Kendrick Lamar",
        "Power - Kanye West",
        "Till I Collapse - Eminem",
        "Lose Yourself - Eminem",
        "DNA. - Kendrick Lamar",
    ],
}


def generate_playlist(mood: str) -> list[str]:
    if mood not in PLAYLISTS:
        raise ValueError(f"Unknown mood '{mood}'. Choose from: {', '.join(PLAYLISTS)}")
    tracks = PLAYLISTS[mood].copy()
    random.shuffle(tracks)
    return tracks


def main():
    parser = argparse.ArgumentParser(description="Generate a mood-based playlist.")
    parser.add_argument("--mood", required=True, help="Your current mood")
    args = parser.parse_args()

    try:
        playlist = generate_playlist(args.mood)
        print(f"\nYour {args.mood} playlist:\n")
        for i, track in enumerate(playlist, 1):
            print(f"  {i}. {track}")
        print()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
