# wycheproof-c

---

## Overview

`wycheproof-c` is a C project that converts [Wycheproof](https://github.com/google/wycheproof) JSON test vectors into C header files. This allows developers to test cryptographic algorithms in C using standardized test vectors.

---

## Directory Structure

```text
/Wycheproof-c
├─ /vectors                    # Original Wycheproof JSON test vectors
├─ /parsed_vectors             # Generated C headers from JSON vectors
├─ /parser                     # Parser implementation
│   ├─ /logic                  # Parsing logic for each algorithm
│   └─ parser.py               # Main script to convert JSONs to headers
├─ LICENSE
└─ README.md
```

### Parsed Algorithms

The parser currently supports generating headers for the following algorithms:
- AES (CBC, GCM, CMAC, GMAC)
- ChaCha20-Poly1305 / XChaCha20-Poly1305
- HMAC (SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA-3 variants)
- HKDF (SHA-1, SHA-256, SHA-384, SHA-512)
- KMAC128 / KMAC256
- PBKDF2-HMAC (SHA-1, SHA-224, SHA-256, SHA-384, SHA-512)

---

## Usage

1. Place the Wycheproof JSON files in the `/vectors` directory.
2. Run the parser:

```bash
python parser/parser.py
```

3. Generated `.h` files will appear in `/parsed_vectors`.

The parser is modular: each algorithm has its own module under `/parser/logic`.

---

## License and Attribution

This project is licensed [Apache-2.0](LICENSE), following the same license as Wycheproof itself. The original JSON test vectors, located in `/vectors`, are sourced from [Google Wycheproof](https://github.com/google/wycheproof). This repository parses these JSON files into C headers for testing purposes, while the Wycheproof vectors retain their original license and attribution.