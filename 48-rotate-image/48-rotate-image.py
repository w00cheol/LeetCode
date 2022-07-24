class Solution:
    def rotate(self, matrix):
        matrix[:] = zip(*matrix[::-1])
        