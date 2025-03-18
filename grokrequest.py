import requests
import json
import os
import sys
from dotenv import load_dotenv

def make_api_request(url, data=None, headers=None, method='GET', timeout=30):
    """
    Perform an API request and return the response.
    
    Args:
        url (str): The API endpoint URL
        data (dict, optional): JSON data to send in the request body
        headers (dict, optional): Request headers
        method (str, optional): HTTP method (GET, POST, PUT, DELETE, etc.)
        timeout (int, optional): Request timeout in seconds

    Returns:
        dict: The response data
    """
    if headers is None:
        headers = {'Content-Type': 'application/json'}
    
    try:
        # Only supports post requests
        response = requests.post(url, data=json.dumps(data), headers=headers, timeout=timeout)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Try to parse JSON response
        try:
            return response.json()
        except json.JSONDecodeError:
            return {"text": response.text}
            
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        sys.exit(1)

def get_argument():
    """
    Get the prompt string from the command line.
    """
    if len(sys.argv) != 2:
        print("Usage: python grokrequest.py \"<your-prompt>\"")
        sys.exit(1)
    return sys.argv[1]

def main():
    # Data preparation
    prompt = get_argument()
    print(f"Your prompt:")
    print("\n\n")
    print(prompt)
    print("\n\n")
    api_url = "https://api.x.ai/v1/chat/completions"
    request_data = {
        "messages": [
            {
                "role": "user",
                "content": "%s" % prompt
            }],
        "model": "grok-2-latest",
        "stream": False,
        "temperature": 0
        }

    # Headers
    load_dotenv()    
    api_key = os.environ.get('GROK_KEY')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % api_key
    }
    
    # Make the API request
    response = make_api_request(
        url=api_url,
        data=request_data,
        headers=headers,
        method='POST'
    )

    # Print the results
    print("Your response:")
    print("\n\n")
    print(json.dumps(response, indent=4))
    print("\n\n")
    print(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    main()
