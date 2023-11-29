import sqlite3
import json

# Ask the user to enter the path to their Firefox profile
path = input("Enter the path to your Firefox profile: ")

# Connect to the database
conn = sqlite3.connect(f'{path}\\cookies.sqlite')

# Create a cursor object
cur = conn.cursor()

# Get the website from the user
website = input("Enter the website: ")

# Execute the query
cur.execute('SELECT name, value FROM moz_cookies WHERE host LIKE ?', ('%' + website + '%',))

# Fetch all the data returned by the query
cookies = cur.fetchall()

# Convert the cookies into a dictionary
cookies_dict = {cookie[0]: cookie[1] for cookie in cookies}

# Convert the dictionary into a JSON string
cookies_json = json.dumps(cookies_dict, indent=4)

# Write to JSON file
with open('cookies.json', 'w') as f:
    f.write(cookies_json)
    
# print the cookies
for cookie in cookies:
    print(f"Name: {cookie[0]}, Value: {cookie[1]}")

# Close the connection
conn.close()

# Ask the user to press enter to quit the program
input("Press ENTER to exit...")