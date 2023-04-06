import re
from pathlib import Path
from jinja2 import Template
from settings import settings


def parse_text(text):
  name_lines = []
  number_lines = []

  lines = (l.strip() for l in text.splitlines() if l.strip())

  for line in lines:
    if line[0].isdigit():
      number_lines.append(line)
    else:
      name_lines.append(line)

  return zip(get_names(name_lines), get_numbers(number_lines))

def get_names(lines):
  for line in lines:
    parts = [n.capitalize() for n in re.split(r',?[ ]+', line.strip()) if n.strip()]
    family_name, *rest = parts
    yield ' '.join(rest + [family_name])

def get_numbers(lines):
  for line in lines:
    for part in line.split():
      yield part

text = Path('judges.txt').read_text()
items = list(parse_text(text))

# Print contact list
print('Contacts\n')
for name, number in items:
  print(f'{name}  {number}')

print("""
Election Central  312-269-7870
Equipment & supplies  773-247-4065
Polling Places Department  312-269-7976
Registration Deparment  312-269-7960""")

template = Template("""\
Hi {{first_name}}, this is your {{role}}, {{subject_name}}. I plan to go to {{location}} on {{date}} at {{time}} to inspect \
the voting equipment. Can you make it?""")

print('\n\nText messages\n')

for name, number in items:
  first, _rest = name.split(' ', 1)
  settings['first_name'] = first
  text = template.render(**settings)
  print(text)
  print(number + '\n')
