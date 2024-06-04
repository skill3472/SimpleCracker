## numcracker by skill347
A simple Python script for cracking a range of numbers, from a hash pattern.

---
## Usage
```
usage: numcracker [-h] [--mode {sha512,sha256,sha1,md5}] [--out OUT] [--verbose] range expression

Crack simple number hashes.

positional arguments:
  range                 Range of numbers to crack. Example: 100-250
  expression            RegEx expression to match.

options:
  -h, --help            show this help message and exit
  --mode {sha512,sha256,sha1,md5}, -m {sha512,sha256,sha1,md5}
                        Select the hashing algorithm. Default is SHA512.
  --out OUT, -o OUT     Output filename.
  --verbose, -v         Verbose mode.
```

