import logging
import datetime
from media_agent.agent import MediaAgent

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    agent = MediaAgent()
    agent.run_daily()
    print("Daily media agent completed at", datetime.datetime.now())
