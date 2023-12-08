class Empyrean:
  def __init__(self):
    self.running = False

  def begin(self):
    output

    self.running = True

    with open('introduction.txt') as f:
      intro = f.read()

    output(intro)
  
  def onoutput(self, output_func):
    self.output = output_func
  
  def input(self, prompt):
    assert running == True, 'Model Not Running'
    self.output(prompt)
