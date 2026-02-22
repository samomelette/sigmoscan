"""
Copyright (C) 2025, CEA

This program is free software; you can redistribute it and/or modify
it under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License.

You should have received a copy of the license along with this
program. If not, see <https://creativecommons.org/licenses/by-nc-sa/4.0/>.
"""

import socket

def check_existing_network_interface(interface: str) -> bool:
    """
    Checks if the given network interface exists.

    Args:
        interface: The name of the network interface to check (e.g. "eth0", "wlan0", etc.)
    """

    available_interfaces = [
        interface for _, interface in socket.if_nameindex()
    ]

    if interface in available_interfaces:
        return True
    else:
        available_interfaces_str = ",".join(available_interfaces)
        error_msg = f"Interface {interface} not in the list of available interfaces: {available_interfaces_str}."
        raise ValueError(error_msg)


