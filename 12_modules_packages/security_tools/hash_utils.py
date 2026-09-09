# Hash Utility Module

import hashlib


def generate_sha256(data):
    """Generate a SHA-256 hash for the given text."""

    return hashlib.sha256(data.encode()).hexdigest()
  

