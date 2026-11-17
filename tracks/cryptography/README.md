# Cryptography Track

## Rules of Thumb

- Encoding (Base64, hex) is reversible representation, not encryption.
- Encryption protects confidentiality under a key.
- Hashing verifies integrity and is generally one-way.
- Public-key cryptography uses different public and private keys.

## Starter Exercises

Try:

```bash
printf 'INSA' | xxd -p
printf 'SU5TQQ==' | base64 -d
```

Explore Caesar shifts and XOR with small examples. Never use custom cryptography for real authentication or secret storage.
