from empyrean.empyrean import Empyrean
from termcolor import colored

machine = Empyrean()

def output(text, type):
  assert type in ['intro', 'echo']
  color = 'red' if type == 'intro' else 'green' if type == 'echo'

machine.addOutputListener(output)
machine.start()

print('Running Empyrean...')
print('Output will be in', colored('red for intro,', 'red'), 'and', colored('green for echo', 'green'))

while True:
  prompt = input()
  machine.input(prompt)
