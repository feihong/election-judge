"""
Export election flashcards using AnkiConnect extension
"""
from pathlib import Path
import requests
import util


output_file = Path('flashcards.txt')


def invoke(action, **params):
  data = {'action': action, 'version': 6}
  if params:
    data['params'] = params
  r = requests.post('http://127.0.0.1:8765', json=data)
  return r.json()


def get_election_cards():
  note_ids = invoke('findNotes', query='tag:election')['result']
  print(f'Found {len(note_ids)} election notes')
  for note in invoke('notesInfo', notes=note_ids)['result']:
    yield note['fields']['Text']['value']


with output_file.open('w') as fp:
  fp.write(util.header)

  for card in get_election_cards():
    fp.write(f'Cloze\telection\t{card}\n')
