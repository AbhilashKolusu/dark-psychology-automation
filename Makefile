.PHONY: install setup run clean

install:
	pip install -r requirements.txt

setup:
	cp .env.example .env
	@echo "Please edit .env file with your API keys"

run:
	python main.py

clean:
	rm -f content_*.json
	rm -rf __pycache__/

test:
	python -c "import main; print('Import successful')"