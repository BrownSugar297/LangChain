from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
from urllib.parse import urlparse, parse_qs


def extract_video_id(url: str) -> str:
    parsed = urlparse(url)

    if parsed.hostname in ["www.youtube.com", "youtube.com"]:
        query = parse_qs(parsed.query)
        if "v" in query:
            return query["v"][0]
        if parsed.path.startswith("/embed/"):
            return parsed.path.split("/embed/")[1]
        if parsed.path.startswith("/shorts/"):
            return parsed.path.split("/shorts/")[1]

    if parsed.hostname == "youtu.be":
        return parsed.path.lstrip("/")

    raise ValueError("Invalid YouTube URL or cannot extract video ID")


def get_youtube_transcript(url: str = "https://www.youtube.com/watch?v=u4ZoJKF_VuA") -> str:
    """
    Given a YouTube URL, returns its English transcript as a single string.
    Defaults to Simon Sinek's TED Talk - "How great leaders inspire action".
    """
    try:
        video_id = extract_video_id(url)
        api = YouTubeTranscriptApi()
        transcript_list = api.fetch(video_id=video_id, languages=['en'])
        transcript = " ".join(chunk.text for chunk in transcript_list)
        return transcript

    except TranscriptsDisabled:
        raise RuntimeError("Transcripts are disabled for this video.")
    except NoTranscriptFound:
        raise RuntimeError("No English transcript found for this video.")
    except VideoUnavailable:
        raise RuntimeError(f"Video is unavailable or removed: {url}")
    except Exception as e:
        raise RuntimeError(f"Error retrieving transcript: {e}")


if __name__ == "__main__":
    transcript = get_youtube_transcript()
    print(f"Transcript length: {len(transcript)} characters")
    print("\nFirst 500 characters preview:")
    print(transcript[:500])