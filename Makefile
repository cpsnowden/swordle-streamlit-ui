
install_requirements:
	@pip install -r requirements.txt

run:
	-@streamlit run Home.py

install:
	@pip install . -U
