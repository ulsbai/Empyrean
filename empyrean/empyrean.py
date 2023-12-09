import os

class Empyrean:
  def __init__(self):
    self.running = False

  def start(self):
    self.output

    self.running = True

    with open(os.path.join(os.path.dirname(__file__), 'introduction.txt')) as f:
      intro = f.read()

    self.output(intro)
  
  def onoutput(self, output_func):
    self.output = output_func
  
  def input(self, prompt):
    assert self.running == True, 'Model Not Running'
    self.output(prompt)
