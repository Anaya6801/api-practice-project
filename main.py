# Line 1: Import the 'requests' tool we installed.
# This gives our script the ability to talk to websites.
import requests

# Line 2: Store the API's web address in a variable.
# This is the address of the "kitchen" we want to order from.
api_url = "https://jsonplaceholder.typicode.com/posts"

# Line 3: Send a request to the API and store the response.
# This is like the waiter taking our order and bringing back food.
print("Asking the API for blog posts...")
response = requests.get(api_url)
print("Got a response!")

# Line 4: Convert the response data into a Python list.
posts = response.json()

# Line 5: Print a header.
print("")
print("--- Here are the first 3 blog post titles ---")
print("")

# Line 6: Loop through the first 3 posts and print each title.
for post in posts[:3]:
    print("Title:", post["title"])
    print("")
