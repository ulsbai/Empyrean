from run_model import Empyrean

print('Running Empyrean...')

machine = Empyrean()

machine.onoutput(print)
machine.begin()

while True:
  prompt = input()
  machine.input(prompt)
