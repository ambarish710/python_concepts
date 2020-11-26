# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
#
# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
#


# Logic
# Create a get_hash functions which creates a random 6 digit hash from all ascii letters and numbers
# Create a dict
# Key == random hash and value is the long url

# Encode
    # As part of encode, update the url_mappings dict
    # Where key is the hash and value is the long URL

# Decode
    # Fetch hash from the incoming small url
    # Fetch the long url from the url_mappings
    # Return the long url



import string
import random


class Codec:
    def __init__(self):
        self.url_mappings = {}


    def get_hash(self):
        total_chars = string.ascii_letters + string.digits
        hash_string = ""
        for i in range(6):
            hash_string += random.choice(total_chars)
        return hash_string


    def encode(self, longUrl: str) -> str:
        """
            Encodes a URL to a shortened URL.
        """
        hash_string = self.get_hash()
        self.url_mappings[hash_string] = longUrl
        return "http://tinyurl.com/" + hash_string


    def decode(self, shortUrl: str) -> str:
        """
            Decodes a shortened URL to its original URL.
        """
        hash_string = shortUrl.split("/")[3]
        return self.url_mappings[hash_string]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
