# GPT3-Domain-Generator

<h1>Introduction</h1>
This script is a domain availability checker that uses GPT-3 to generate unique business name ideas based on the keywords and a short description provided by the user. The script first prompts the user to enter keywords related to their business and a short description about their business. The script then uses the OpenAI's GPT-3 API to generate name ideas based on the user's input. The script then checks the availability of the generated names using a domain availability checker API. The script prints the results of the availability check for each name idea, indicating whether the domain is available or not. 
<br><br>
<h1>Usage</h1><br>
1.) pip install -r requirements.txt<br>
2.) enter your OpenAI API key in main.py<br>
3.) python3 main.py<br>
4.) enter keywords<br>
5.) enter short business description<br>
6.) wait for results<br>
<br>
<h1>Development Ideas</h1>
- cut prompt into 3 different prompts, each one for different name style<br>
- add a feature where it would also include synonyms of provided keywords<br>
- build it as a web app with UI
