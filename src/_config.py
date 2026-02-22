"""
Copyright (C) 2025, CEA

This program is free software; you can redistribute it and/or modify
it under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License.

You should have received a copy of the license along with this
program. If not, see <https://creativecommons.org/licenses/by-nc-sa/4.0/>.
"""

import configparser
import ipaddress
import os

from typing import TypedDict

class KafkaConfig(TypedDict):
    addr_server: str
    topic: str

class ScannerConfig(TypedDict):
    interface: str | None
    ip_client: ipaddress.IPv4Address | ipaddress.IPv6Address
    temp_pcap_path: str
    kafka_config: KafkaConfig


def parse_config(config_file: str) -> ScannerConfig:
    config = configparser.ConfigParser()
    _ = config.read(config_file)

    interface = config["SCANNER"]["INTERFACE"]
    if interface == "default":
        interface = None

    try:
        ip_client = ipaddress.ip_address(config['KAFKA']['IP_CLIENT'])
    except ValueError:
        print(f"ValueError: IP_CLIENT in section [KAFKA] of the config is not a valid IPv4 or IPv6 address.")
        exit(-1)
   
    temp_pcap_path = config["SCANNER"]["TEMP_PCAP_PATH"]
    if not os.path.isdir(temp_pcap_path):
        os.makedirs(temp_pcap_path)

    addr_server = config['KAFKA']['ADDRESS_SERVER']
    topic = config["KAFKA"]["TOPIC"]

    return ScannerConfig(
        interface=interface,
        ip_client=ip_client,
        temp_pcap_path=temp_pcap_path,
        kafka_config=KafkaConfig(
            addr_server=addr_server,
            topic=topic,
        )
    )

