
install_requirements:
	@pip install -r requirements.txt

streamlit:
	-@streamlit run app.py

install:
	@pip install . -U
