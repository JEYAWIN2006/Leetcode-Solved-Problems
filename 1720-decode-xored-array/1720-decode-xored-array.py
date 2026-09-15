class Solution(object):
    def decode(self, encoded, first):
        encoded.insert(0, first)
        for i in range(1, len(encoded)):
            encoded[i] = encoded[i]^encoded[i-1]
        return encoded