#!/usr/bin/env python3
"""WebSocket client that sends one message and prints the reply."""
import asyncio

import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Connect to uri, send text once, and return the single response."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
    return str(response)


async def main():
    """Send the demo message to the echo server and print the reply."""
    response = await connect_and_send("ws://localhost:8765",
                                      "Hello WebSocket")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
