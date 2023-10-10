# interview-bot


Ver1 interview bot based off this YouTube tutorial: https://www.youtube.com/watch?v=4y1a4syMJHM

Ver2 interview bot based off this YouTube tutorial: https://www.youtube.com/watch?v=x7PmlpUiTAY 

### Running the python backend (fastAPI)
```
uvicorn main:app --reload
```
note: dont use the `--reload` in production environments
### Running the react frontend
```
yarn dev    # for dev environment
yarn build  # check code syntax
yarn start  # run code to site
```
## Setup 
### Backend
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

#### Run
```
uvicorn main:app --reload
```

### Frontend
```
sudo npm install --global yarn --force
```
```
npm install -g create-vite
npm install -D tailwindcss postcss autoprefixer
yarn install
```
Start the project
```
yarn create vite . 
```

make sure that you have set a `.nvmrc` file to `16` and run 
```
nvm use 16
or 
nvm use
```

#### Run
```
yarn dev    # for dev environment
yarn build  # check code syntax
yarn start  # run code to site
```
