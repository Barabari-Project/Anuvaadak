# Server
Currently server will be in Python on Sanic but in long term as stable release is out, server will move to Bun with FFIs for all optimizations for sake of speed and safety.

Create a `.env` file in root and add the following environment variables as needed
```shell
# For OpenAI GPT-3
OPENAI_GPT_KEY=""
```

While it is slightly painful to integrate them. `Bun` is like 3x faster than `Python` RAW in basically every possible metric. [Read More](https://medium.com/deno-the-complete-reference/hello-world-performance-bun-express-vs-python-fast-api-dc3c00960981)

![Benchmark](https://miro.medium.com/max/1400/1*CjKTA54ss1w2QwtoIdAWUg.webp)

## Patches
Since railway does not allow `yt-dlp` and `youtube-dl` we have used our own fork of it with a completely different name to pass the build.
`git+https://github.com/Barabari-Project/ydown#egg=ydown`

> **ydown is completely identical to *yt-dlp***