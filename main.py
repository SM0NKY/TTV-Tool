from Twitch import Viewer_Counter
import asyncio

async def start_bot() -> None:
    try:
        bot:object|Viewer_Counter = Viewer_Counter()
        await bot.start()
    except Exception as e:
        raise e
    

if __name__ == "__main__":
    asyncio.run(start_bot())



