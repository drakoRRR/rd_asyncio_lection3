import asyncio
import random

from config import SERVER_PORT, SERVER_HOST


async def generate_weather_data():
    while True:
        temperature = random.uniform(-10, 40)
        humidity = random.uniform(20, 100)
        data = f"Temperature: {temperature:.2f} C, Humidity: {humidity:.2f}%"
        yield data
        await asyncio.sleep(2)


async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Made connection from {addr[0]}:{addr[1]}")

    try:
        async for data in generate_weather_data():
            writer.write(data.encode())
            await writer.drain()
    except Exception as e:
        pass
    finally:
        try:
            writer.close()
            await writer.wait_closed()
        except Exception as e:
            pass
        print(f"Closed connection from {addr[0]}:{addr[1]}")


async def main():
    try:
        print("Starting server...")
        server = await asyncio.start_server(handle_client, SERVER_HOST, SERVER_PORT)
        print(f"Server started on {SERVER_HOST}:{SERVER_PORT}")
        async with server:
            await server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down server...")


if __name__ == '__main__':
    asyncio.run(main())