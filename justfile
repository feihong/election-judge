help:
	just --list

install: ## Install dependencies
	pip install --requirement requirements.txt

page: ## Generate the election info page
	python generate_page.py

flashcards: ## Generate flashcard file to import into Anki
	python generate_flashcards.py

export: ## Export all Anki flashcards with "election" tag
	python export_flashcards.py
