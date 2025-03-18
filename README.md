## Simple Grok request invoker

To use it perform following steps:

1. clone the repository

`git clone https://github.com/ArmoredStone/simple-grok-request-py.git`

2. navigate to cloned directory

`cd simple-grok-request-py`

3. create virtual environment

`python3 -m venv venv`

4. activate the virtual environment

`source venv/bin/activate`

5. install dependencies

`pip install requirements.txt`

6. configure the API key in .env file

`nano .env`

7. request grok with your prompt

`python3 grokrequest.py "Hello!"`
