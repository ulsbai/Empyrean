import os

class Empyrean:
  def __init__(self):
    self.running = False
    self.outputListeners = []

  def start(self):
    self.output

    self.running = True

    with open(os.path.join(os.path.dirname(__file__), 'introduction.txt')) as f:
      intro = f.read()

    self.output(intro, type='intro')
  
  def addOutputListener(self, output_func):
    self.outputListeners.append(output_func)
  
  def input(self, prompt):
    assert self.running == True, 'Model Not Running'
    self.output(prompt, type='echo')

  def output(self, text, type):
    for output_func in self.outputListeners:
      output_func(text, type)
