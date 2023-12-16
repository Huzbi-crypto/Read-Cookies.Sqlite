import os
import json
import sqlite3

def read_cookies(path, website):
    # print(os.path.join(path, 'cookies.sqlite'))
    # Connect to the database
    conn = sqlite3.connect(os.path.join(path, 'cookies.sqlite'))
    
    # Create a cursor object
    cur = conn.cursor()
    
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

if __name__ == '__main__':
    # Gets the path to the Firefox profile on Windows
    path = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Mozilla', 'Firefox', 'Profiles')
    # print(path)

    # get the list of profiles
    profiles_dir = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    # print(profiles_dir)

    # create a loop to read cookies from multiple websites
    while True:
        website = input("Enter the website (enter 'q' to quit): ")
        if website == 'q':
            break
        for profile in profiles_dir:
            path_with_profile = os.path.join(path, profile)
            # print(path_with_profile)
            read_cookies(path_with_profile, website)
        print()

