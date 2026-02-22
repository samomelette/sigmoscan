"""
Copyright (C) 2025, CEA

This program is free software; you can redistribute it and/or modify
it under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License.

You should have received a copy of the license along with this
program. If not, see <https://creativecommons.org/licenses/by-nc-sa/4.0/>.
"""

import configparser
from typing import TypedDict

class ConsumerConfig(TypedDict):
    addr_server: str
    topic: str


def parse_config(config_file: str) -> ConsumerConfig:
    config = configparser.ConfigParser()
    _ = config.read(config_file)

    return ConsumerConfig(
        addr_server=config["KAFKA"]["ADDRESS_SERVER"],
        topic=config["KAFKA"]["TOPIC_TRAFFIC"],
    )
