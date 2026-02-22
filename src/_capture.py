"""
Copyright (C) 2025, CEA

This program is free software; you can redistribute it and/or modify
it under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License.

You should have received a copy of the license along with this
program. If not, see <https://creativecommons.org/licenses/by-nc-sa/4.0/>.
"""

import os
from sys import stderr
import time
import logging
import subprocess

from ._color import color

def capture_live_interface(
    interface: str | None,
    rotate_every_t_sec: float,
    temp_dir: str,
) -> subprocess.Popen[bytes]:

    pcap_file_pattern = os.path.join(temp_dir, r"temp_%Y%m%d%H%M%S.pcap")

    tcpdump_cmd = ["/usr/bin/tcpdump", "-G", str(rotate_every_t_sec), "-w", pcap_file_pattern]
    if interface is not None:
        logging.info(f"Capturing from interface: {interface}")
        tcpdump_cmd.append("-i")
        tcpdump_cmd.append(interface)
    else:
        logging.info(f"Capturing from default interface")

    logging.debug(f"Running tcpdump command: {tcpdump_cmd}")

    tcpdump_process = subprocess.Popen(
        tcpdump_cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )

    time.sleep(1)
    if tcpdump_process.poll() is not None:
        # process already exited, now it's safe to read stderr
        if tcpdump_process.stderr is None:
            logging.error(
                color(f"Fatal: Unknown tcpdump error, could not read stderr", "red")
            )
            return tcpdump_process
        err = tcpdump_process.stderr.read()
        if "Operation not permitted" in err.decode():


            logging.error(
                color(
                    f"Fatal: You don't have the necessary permissions to run tcpdump. {err.decode()}", 
                    "red"
                )
            )

    return tcpdump_process
