from pathlib import Path
import re

input_file = Path('new-flashcards.txt')
output_file = Path('flashcards-to-import.txt')

header = """\
#separator:tab
#html:true
#notetype column:1
#tags column:2
"""

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
  fp.write(header)

  for line in get_cards():
    fp.write(line + '\n')
