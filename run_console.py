from empyrean.empyrean import Empyrean

machine = Empyrean()

machine.addOutputListener(output)
machine.start()

print('Running Empyrean...')

while True:
  prompt = input()
  machine.input(prompt)
