from .encoding import Encoding
import numpy as np

class Language:
  def __init__(self, language: str):
    self.string = language

  def encode(self, encoding: Encoding) -> numpy.ndarray:
    return encoding.encode(self)

  def get_string(self) -> str:
    return self.string
