import json
import subprocess


def get_audio_metadata(url: str):
    """
    Use ffprobe to retrieve audio metadata from a url
    """
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", url],
        stdout=subprocess.PIPE,
    )

    if result.stderr:
        raise subprocess.CalledProcessError(returncode=result.returncode, cmd=result.args, stderr=result.stderr)

    if result.stdout:
        output = result.stdout.decode("utf-8")
        data = json.loads(output)

        return {
            "title": data.get("format").get("tags").get("title"),
            "artist": data.get("format").get("tags").get("artist"),
            "album": data.get("format").get("tags").get("album"),
            "duration": float(data.get("format").get("duration")),
        }

    return {}
