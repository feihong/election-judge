from pathlib import Path
import re
import util

input_file = Path('new-flashcards.txt')
output_file = Path('flashcards-to-import.txt')


def get_lines():
  lines = input_file.read_text().splitlines()
  for line in lines:
    line = line.strip()
    if line == '':
      continue

    yield re.sub(r'\{(.*?)\}', r'{{c1::\1}}', line)


def get_cards():
  for line in get_lines():
    yield f'Cloze\telection\t{line}'


with output_file.open('w') as fp:
  fp.write(util.header)

  for line in get_cards():
    fp.write(line + '\n')
