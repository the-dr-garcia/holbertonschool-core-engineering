#!/usr/bin/env python3
"""WebSocket echo server."""
import asyncio

import websockets


async def connection_handler(websocket):
    """Echo back every text message received on the connection."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the server on 127.0.0.1:8765 and run forever."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
