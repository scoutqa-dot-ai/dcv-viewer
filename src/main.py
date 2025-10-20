import json
from base64 import b64encode

from bedrock_agentcore.tools.browser_client import BrowserClient


def main():
    browser_client = BrowserClient(region="us-west-2")
    width = 1920
    height = 1080
    session_id = browser_client.start(
        session_timeout_seconds=900,
        viewport={"width": width, "height": height}
    )
    presigned_url = browser_client.generate_live_view_url(expires=300)
    config = {
        "presignedUrl": presigned_url,
        "width": width,
        "height": height,
    }
    base64_encoded = b64encode(json.dumps(config).encode("utf-8")).decode("utf-8")
    print('http://localhost:3000/#' + base64_encoded)


if __name__ == "__main__":
    main()
