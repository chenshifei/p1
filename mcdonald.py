def printverse(animal, sound):
    print('Old MacDonald had a farm\n'
          + 'E-I-E-I-O\n'
          + 'And on this farm he had a ' + animal + '\n'
          + 'E-I-E-I-O\n'
          + 'With a ' + sound + ' ' + sound + ' here\n'
          + 'And a ' + sound + ' ' + sound + ' there\n'
          + 'Here a ' + sound + ' there a ' + sound + '\n'
          + 'Everywhere a ' + sound + ' ' + sound + '\n'
          + 'Old MacDonald had a farm\n'
          + 'E-I-E-I-O\n')
    
def printsong():
    printverse('cow', 'moo')
    printverse('dog', 'wang')
    printverse('dark', 'quack')
