install:
	pip install --requirement requirements.txt

page:
	python generate_page.py

flashcards:
	python generate_flashcards.py

export:
	python export_flashcards.py
