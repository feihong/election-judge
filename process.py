import re
from pathlib import Path
import socket
import http.server
from jinja2 import Template
from settings import settings


output_file = Path('index.html')

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
    # Reformat from "Smith, John A" to "John A Smith"
    parts = [n.capitalize() for n in re.split(r',?[ ]+', line.strip()) if n.strip()]
    family_name, *rest = parts
    yield ' '.join(rest + [family_name])

def get_numbers(lines):
  for line in lines:
    for part in line.split():
      yield part
  
def start_web_server():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(('10.255.255.255', 1))
  ip = s.getsockname()[0]

  server_address = ('', 8000)
  httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
  print(f'Starting webserver at {ip}:8000\n')
  httpd.serve_forever()


text = Path('judges.txt').read_text()
judges = list(parse_text(text))
election_departments = [line.split('  ') for line in """\
Election Central  312-269-7870
Equipment & supplies  773-247-4065
Polling Places Department  312-269-7976
Registration Deparment  312-269-7960""".splitlines()]

html_template = Template("""\
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Election Info</title>
</head>
<body>
<h1>Election Info</h1>

<h2>Election Judges</h2>
<pre>
{% for name, number in judges -%}
{{ name }}&nbsp; <a href="tel:{{ number }}">{{ number }}</a>
{% endfor %}
</pre>

<h2>Election Departments</h2>
<pre>
{% for name, number in election_departments -%}
{{ name }}&nbsp; <a href="tel:{{ number }}">{{ number }}</a>
{% endfor %}
</pre>

<h2>Inspection text messages</h2>

<ul>
{% for name, number, mesg in text_messages %}
  <li>
    <a href="sms:{{ number }}?&body={{ mesg|urlencode }}">{{ name }}</a>
  </li>
{% endfor %}
</ul>

</body>
""")

text_message_template = Template("""\
Hi {{first_name}}, this is your {{role}}, {{subject_name}}. I plan to go to {{location}} on {{date_time}} to inspect the voting equipment. Can you make it?""")

def get_judges_with_text_messages(judges):
  for name, number in judges:
    if not number[0].isdigit():
      continue
    settings['first_name'] = name.split(' ', 1)[0]
    mesg = text_message_template.render(**settings)
    yield name, number, mesg

with output_file.open('w') as fp:
  html = html_template.render(
    judges=judges,
    election_departments=election_departments,
    text_messages=get_judges_with_text_messages(judges))
  fp.write(html)

start_web_server()
