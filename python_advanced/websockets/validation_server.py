#!/usr/bin/env python3
"""WebSocket server that validates incoming messages."""
import asyncio

import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """Reply OK:<message> for valid messages and ERR:EMPTY otherwise."""
    try:
        async for message in websocket:
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
    except ConnectionClosed:
        pass


async def main():
    """Start the server on 127.0.0.1:8765 and run forever."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
