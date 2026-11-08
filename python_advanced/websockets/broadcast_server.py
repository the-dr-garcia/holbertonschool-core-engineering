#!/usr/bin/env python3
"""WebSocket server that broadcasts every message to all clients."""
import asyncio

import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def broadcast(message):
    """Send message to every connected client, skipping closed ones."""
    for client in list(connected_clients):
        try:
            await client.send(message)
        except ConnectionClosed:
            connected_clients.discard(client)


async def connection_handler(websocket):
    """Track the client and broadcast B:<message> to all clients."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await broadcast(f"B:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the server on 127.0.0.1:8765 and run forever."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
