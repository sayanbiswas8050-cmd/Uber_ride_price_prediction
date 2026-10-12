# Uber_ride_price_prediction

## Workflows

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update te pipeline
8. update the main.py 
9. update the app.py

# How to run?
### STEPS:

**Create the virtual environment with Python 3.11**
```bash
py -3.11 -m venv venv
```

**Activate the environment**
```bash
Set-ExecutionPolicy RemoteSigned -Scope Process
venv\Scripts\activate
```
#### requirements.txt
```bash
pandas
matplotlib
seaborn
scikit-learn
holidays
geopy
streamlit
xgboost
pydantic
fastapi
uvicorn
python-box
ensure
pyYAML
types-PyYAML
-e . 
```
`geopy: help to get coordinates from addresses, cities, countries, and landmarks worldwide .`

`python-box: It also automatically and recursively converts nested dictionaries or lists into Box and BoxList objects .`

`ensure:  used to write expressive, readable condition checks and enforce function signature annotations .`

`pyYAML: It converts raw YAML data into native Python dictionaries, lists, and basic data types .`

`-e .: Whenever you edit, add, or delete functions inside your src/ folder, your Python code/notebook immediately reflects those changes without having to run .`

**Install dependencies**
```bash
pip install -r requirements.txt
```

