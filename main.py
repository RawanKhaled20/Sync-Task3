import requests

def shorten_url(long_url, bitly_token):
    endpoint = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {bitly_token}",
        "Content-Type": "application/json",
    }
    payload = {
        "long_url": long_url,
        "domain": "bit.ly",  # You can customize the domain if you have a custom Bitly domain
    }

    response = requests.post(endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        short_url = data.get("id")
        return short_url
    else:
        print(f"Failed to shorten URL. Status code: {response.status_code}")
        return None

# Example usage:
long_url = "https://www.examplethmkk.com"
bitly_token = "13d8070683f3f66d9d76054d872e04248b19ac79"  # Replace with your Bitly API token

short_url = shorten_url(long_url, bitly_token)

if short_url:
    print(f"Shortened URL: {short_url}")
