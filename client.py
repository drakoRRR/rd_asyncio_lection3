import asyncio

from config import SERVER_PORT, SERVER_HOST


async def read_weather_data():
    reader, writer = await asyncio.open_connection(SERVER_HOST, SERVER_PORT)
    try:
        while True:
            data = await reader.read(100)
            if not data:
                break
            print(f"Received: {data.decode()}")
    finally:
        writer.close()
        await writer.wait_closed()


if __name__ == '__main__':
    asyncio.run(read_weather_data())
