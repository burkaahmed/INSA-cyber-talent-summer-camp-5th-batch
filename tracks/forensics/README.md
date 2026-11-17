# Forensics Track

## Evidence Handling

1. Preserve original evidence.
2. Work from copies.
3. Record timestamps and tools.
4. Avoid changing metadata.

## Useful Commands

```bash
file evidence.bin
sha256sum evidence.bin
xxd evidence.bin | head
exiftool evidence.jpg
strings evidence.bin | less
```

## Analysis Questions

- What is the file's real format?
- Could its extension be misleading?
- Is there hidden or appended data?
- Do timestamps support a timeline?
