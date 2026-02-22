"""
Copyright (C) 2025, CEA

This program is free software; you can redistribute it and/or modify
it under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License.

You should have received a copy of the license along with this
program. If not, see <https://creativecommons.org/licenses/by-nc-sa/4.0/>.
"""

import logging

from multiprocessing import Queue

from src.color import color
from src.config import parse_config
from src.kafka import EngineKafkaConsumer

def main():

    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[logging.StreamHandler()],
        format=r"[%(asctime)s][%(name)s][%(levelname)s] %(message)s",
    )

    # disable Kafka logs
    logging.getLogger("kafka").setLevel(logging.WARNING)

    print("Starting example consumer...")

    config = parse_config("config.ini")

    queue_ingested = Queue()

    consumer = EngineKafkaConsumer(
        config["addr_server"], config["topic"], queue_ingested
    )
    consumer.start()


    try:
        while True:

            df = queue_ingested.get()
            print("Dataframe head:")
            print(df.head())

    except KeyboardInterrupt:

        if consumer and consumer.is_alive():
            logging.info("Stopping kafka consumer process...")
            consumer.terminate()


if __name__ == "__main__":
    main()
