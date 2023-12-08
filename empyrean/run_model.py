class Empyrean:
  def __init__(self):
    self.running = False

  def begin(self):
    self.output

    self.running = True

    with open('introduction.txt') as f:
      intro = f.read()

    self.output(intro)
  
  def onoutput(self, output_func):
    self.output = output_func
  
  def input(self, prompt):
    assert self.running == True, 'Model Not Running'
    self.output(prompt)
