#!/usr/bin/env python3
"""Encode a short CTF lesson note using Base64."""

import base64

message = "Practice only in systems you own or are authorized to test."
print(base64.b64encode(message.encode()).decode())
