from agents import weather_agent
import asyncio
from tools import WeatherDeps

async def main(prompt, **kwargs):
    result = await weather_agent.run(prompt, **kwargs)
    print(result.output)


if __name__ == "__main__":
    asyncio.run(main("What is the weather in Skövde?", deps = WeatherDeps(city="Skövde")))    
    asyncio.run(main("Tell me a programming joke", deps=WeatherDeps(city="London")))    