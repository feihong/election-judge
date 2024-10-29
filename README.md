# Useful scripts for an election judge

## Installation

Install Python, then install dependencies:

    make install

## Directions

1. Scan a PDF in Dropbox
1. Copy the text for the judges section and paste it into a text editor
1. Remove OCR errors so that only the names of the judges and their phone numbers remain
1. Create a new file `settings.py` and populate it with these fields:

    ```python
    your_role='key judge'
    your_name='Bob Smith'
    polling_place='Sears Tower'
    inspection_date='Monday, November 4'
    inspection_time='4:00 PM'

    other_contacts = """
    Clerk: Henry Joe; 312-111-2222
    """

    handbook_url = 'https://server.com/downloads/ej-handbook.pdf'

    judges = """
    YUKO, MILO
    BABAA, EUGENE
    WAWAWA, SLIPPY
    217-222-3333 773-444-5555 312-666-7777
    """
    ```
1. Run `just page`
1. Console will say `Starting webserver at http://<ip address>:8000`
1. Visit `http://localhost:8000` in your browser
1. Copy everything on the page into a new note in your Notes app
1. Copy the Election Info note through iCloud on your iPhone
1. Tap each name under 'Inspection text messages' to send a text message to the given person

## Links

[2024 Judge of Election
Handbook](https://chicagoelections.gov/poll-workers/election-day-judges)
