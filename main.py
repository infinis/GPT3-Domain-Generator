import openai
import requests
import json

# put your openAI API key here
openai.api_key = "YOUR-OPENAI-KEY"

def check_domain_availability(domain):
  
    endpoint = "https://api.domainsdb.info/v1/domains/search"
    params = {'query': domain}

    
    response = requests.get(endpoint, params=params)

    # checking if it's up
    if response.status_code == 200:
        return 'available'
    else:
        return 'unavailable'

    # parsing the response
    results = json.loads(response.text)

    # checking domain availability
    if results['status'] == 'success':
        if results['domains'][0]['status'] == 'available':
            return 'available'
        else:
            return 'unavailable'
    else:
        return "An error occurred: " + results['status']

# grab user's input
keywords = input("Enter keywords related to your business: ")
business_description = input("Enter a short description about your business: ")

# this part generates business name ideas using davinci003 model
response = openai.Completion.create(
    engine="text-davinci-003", max_tokens=4000,
    prompt=(f"I'm looking to start a business related to these keywords: {keywords}. This is a short description of what my business is about: {business_description}. Generate 30 unique and creative business name ideas in different styles for example: compound names, misspelled names, short and catchy names and abstract names.")
)

# extract name ideas 
name_ideas = response.choices[0].text.strip().split("\n")

for name in name_ideas:
    domain = name.replace(" ", "").lower() + ".com"
    availability = check_domain_availability(domain)
    print(f"{domain} - {availability}")
