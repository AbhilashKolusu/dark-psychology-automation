.PHONY: install setup run clean test activate validate

install:
	python3 -m venv venv
	source venv/bin/activate && pip install -r requirements.txt

setup:
	cp .env.example .env
	@echo "Please edit .env file with your API keys and social media accounts"

activate:
	@echo "Run: source venv/bin/activate"

run:
	source venv/bin/activate && python main.py

validate:
	source venv/bin/activate && python validate_config.py

clean:
	rm -f content_*.json
	rm -rf __pycache__/
	rm -rf venv/

test:
	source venv/bin/activate && python -c "import main; print('Import successful')"