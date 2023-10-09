# interview-bot


Ver1 interview bot based off this YouTube tutorial: https://www.youtube.com/watch?v=4y1a4syMJHM

Ver2 interview bot based off this YouTube tutorial: https://www.youtube.com/watch?v=x7PmlpUiTAY 

Running the python backend (fastAPI)
```
uvicorn main:app --reload
```
note: dont use the `--reload` in production environments

### Setup
```
python3 -m venv venv 
```
```
source venv/bin/activate
```
```
deactivate
```

Install this manually:
```
pip3 install -r requirements.txt  
pip3 install "uvicorn[standard]" 
```