#!/usr/bin/env python3
"""Generate a harmless text-based networking exercise artifact."""

from pathlib import Path

LAB = """No.  Time  Source         Destination    Protocol  Info
1    0.001 10.10.10.21    10.10.10.1     DNS       Standard query A lab.local
2    0.004 10.10.10.1     10.10.10.21    DNS       Standard response A lab.local 10.10.10.50
3    0.010 10.10.10.21    10.10.10.50    TCP       SYN
4    0.011 10.10.10.50    10.10.10.21    TCP       SYN, ACK
5    0.012 10.10.10.21    10.10.10.50    TCP       ACK
6    0.014 10.10.10.21    10.10.10.50    HTTP      GET /camps HTTP/1.1
"""

Path("assets/capture.txt").write_text(LAB, encoding="utf-8")
print("Created assets/capture.txt")
