.DEFAULT_GOAL := help

help: ## Print this help message
	@echo "List of available make commands";
	@echo "";
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-22s\033[0m %s\n", $$1, $$2}';
	@echo "";

install: ## Install dependencies
	pip install --requirement requirements.txt

page: ## Generate the election info page
	python generate_page.py

flashcards: ## Generate flashcard file to import into Anki
	python generate_flashcards.py

export: ## Export all Anki flashcards with "election" tag
	python export_flashcards.py
