# Useful scripts for an election judge

## Installation

Install Python, then install dependencies:

    make install

## Directions

1. Create a new file `settings.py` and populate it with these fields:

    ```python
    settings = dict(
        role='key judge',
        subject_name='Barbara Walters',
        location='Tolkien Academy',
        date_time='Monday, April 6',
    )
    ```
1. Scan a PDF in Dropbox
1. Copy the text and paste it into `judges.txt`
1. Correct OCR errors
1. Run `make page`
1. Console will say `Starting webserver at http://<ip address>:8000`
1. Visit `http://<ip address>:8000` in your phone browser
1. Tap each name under 'Inspection text messages' to send a text message to the given person
1. Copy everything on the page into a new document in your iPhone's Notes app

## Links

[2023 Judge of Election
Handbook](https://app.chicagoelections.com/Documents/general/M2023%20Election%20Judge%20Handbook.pdf)
