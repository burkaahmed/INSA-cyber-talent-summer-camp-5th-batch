# Linux and Networking

## Core Commands

```bash
pwd
ls -la
find . -type f
grep -R "word" .
file suspicious.bin
strings suspicious.bin | head
```

## Networking

```bash
ip addr
ping <lab-ip>
ss -tunlp
curl -v http://<lab-ip>
dig example.test
traceroute <lab-ip>
```

## Permissions Lab

Inspect with:

```bash
ls -l
stat ./target
find /tmp -perm -0002 -ls
```

Answer:

1. What do `rwxr-x---` and `chmod 750` mean?
2. What is the difference between a file and directory execute bit?
3. Which files should never be world-writable?
