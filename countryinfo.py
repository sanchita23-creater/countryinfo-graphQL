import requests
import pycountry

# GraphQL API URL
url = "https://countries.trevorblades.com/"

# User Input
country_name = input("Enter Country Name: ").strip()

try:
    # Convert country name to country code
    country = pycountry.countries.lookup(country_name)
    country_code = country.alpha_2

    # GraphQL Query
    query = f"""
    {{
      country(code: "{country_code}") {{
        name
        capital
        currency
        emoji
        continent {{
          name
        }}
      }}
    }}
    """

    # Send GraphQL Request
    response = requests.post(
        url,
        json={"query": query}
    )

    # Convert response to Python dictionary
    data = response.json()

    # Extract country information
    country_data = data["data"]["country"]
    print(country_data)

    # Display results
    print("\n===== Country Information =====")
    print(f"Country   : {country_data['name']} ({country_code})")
    print(f"Capital   : {country_data['capital']}")
    print(f"Currency  : {country_data['currency']}")
    print(f"Continent : {country_data['continent']['name']}")
    print(f"Flag      : {country_data['emoji']}")

except LookupError:
    print("Country not found. Please enter a valid country name.")

except Exception as e:
    print("An error occurred:", e)

