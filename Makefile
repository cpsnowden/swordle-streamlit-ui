install_requirements:
	@pip install -r requirements.txt

run_local:
	-@BACKEND_URL=http://0.0.0.0:8000 streamlit run Home.py

run:
	-@streamlit run Home.py

install:
	@pip install . -U
