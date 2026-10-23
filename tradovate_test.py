import json
import getpass
import urllib.request
import urllib.error
import uuid

# Tradovate demo authentication endpoint
URL = "https://demo.tradovateapi.com/v1/auth/accesstokenrequest"

print("Tradovate Demo API Test")
print("-----------------------")
print("Enter your credentials locally. They won't be saved in this script.\n")

username = input("Tradovate username: ")
password = getpass.getpass("Tradovate password: ")

# These are example application values from the documentation.
# They may need to be replaced with credentials for an authorized API app.
payload = {
    "name": username,
    "password": password,
    "appId": "Sample App",
    "appVersion": "1.0",
    "cid": 8,
    "sec": "f03741b6-f634-48d6-9308-c8fb871150c2",
    "deviceId": str(uuid.uuid4())
}

request = urllib.request.Request(
    URL,
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(request, timeout=20) as response:
        raw = response.read().decode("utf-8")
        result = json.loads(raw)

        print("\nResponse type:", type(result).__name__)

        if isinstance(result, dict):
            print("Response fields:", list(result.keys()))
            print("Error message:", result.get("errorText", "Not provided"))
            print("Error code:", result.get("errorCode", "Not provided"))
        else:
            print("Response content:", str(result)[:1000])

      

    print("\nResponse received!")
    print("User status:", result.get("userStatus", "Not provided"))
    print("Market data flag:", result.get("hasMarketData", "Not provided"))
    print("Live access flag:", result.get("hasLive", "Not provided"))
    print("Expiration:", result.get("expirationTime", "Not provided"))

    if result.get("accessToken"):
        print("\nDemo authentication: SUCCESS")
        print("An access token was returned (not displayed).")
    else:
        print("\nNo access token was returned. Check the API response.")

except urllib.error.HTTPError as error:
    print("\nHTTP error:", error.code)
    print("Tradovate rejected the request.")
    print("The example app credentials may be invalid,")
    print("or the account may not be authorized for this API.")

except urllib.error.URLError:
    print("\nCould not connect. Check your internet connection and try again.")

except (json.JSONDecodeError, TimeoutError):
    print("\nCould not read a valid response. Try again.")