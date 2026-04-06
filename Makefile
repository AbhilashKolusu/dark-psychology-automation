.PHONY: install setup run clean test activate

install:
	python3 -m venv venv
	source venv/bin/activate && pip install -r requirements.txt

setup:
	cp .env.example .env
	@echo "Please edit .env file with your API keys"

activate:
	@echo "Run: source venv/bin/activate"

run:
	source venv/bin/activate && python main.py

clean:
	rm -f content_*.json
	rm -rf __pycache__/
	rm -rf venv/

test:
	source venv/bin/activate && python -c "import main; print('Import successful')"