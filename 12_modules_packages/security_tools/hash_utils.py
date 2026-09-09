Hash Utility Module

import hashlib


def generate_sha256(data):
    """Generate a SHA-256 hash for the given text."""

    return hashlib.sha256(data.encode()).hexdigest()
  
* Understand the function
data.encode()
converts the text into bytes because hashlib works with bytes.

Then:
hashlib.sha256(...)
creates the SHA-256 hash.

Finally:
.hexdigest()
converts the hash into a readable hexadecimal string.

For example:
generate_sha256("hello")

returns a SHA-256 hash.
