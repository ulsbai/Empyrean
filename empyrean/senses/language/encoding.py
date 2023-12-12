import wordnet
import numpy as np

class Encoding:
  def __init__(self, words):
    self._num_tokens = 0
    self._tokens = {}
    self.append_tokens(words)

  def append_token(self, word):
    self._tokens[word] = num_tokens
    self._num_tokens += 1

  def append_tokens(self, words):
    for word in words:
      self.append_token(word)

  def encode_single_token(self, word):
    return self._tokens[word]

  def encode(self, language):
    words = language.tokenize()
    return np.array([self.encode_single_token(word) for word in words])
