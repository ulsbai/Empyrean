from empyrean.empyrean import Empyrean
from termcolor import colored

machine = Empyrean()

def output(text, type):
  color = {'intro': 'red', 'echo': 'green'}[type]
  print(colored(text, color))

machine.addOutputListener(output)

print('Running Empyrean...')
print('Output will be in', colored('red for intro,', 'red'), 'and', colored('green for echo', 'green'))

machine.start()

while True:
  prompt = input()
  machine.input(prompt)
