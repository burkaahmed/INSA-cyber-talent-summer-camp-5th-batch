# Reverse Engineering Track

## Beginner Workflow

1. Identify the file type.
2. Run it in an isolated environment.
3. Inspect strings and imports.
4. Map control flow.
5. Set breakpoints and observe state.
6. Document the expected and actual behavior.

## Safe Commands

```bash
file challenge
sha256sum challenge
strings -a challenge
readelf -h challenge
objdump -d challenge
```

Use test virtual machines for unknown binaries. Never execute malware from untrusted sources.
