import sqlite3
import json

def read_cookies(path, website):
    # Connect to the database
    conn = sqlite3.connect(f'{path}\\cookies.sqlite')
    
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
    # Ask the user to enter the path to their Firefox profile
    path = input("Enter the path to your Firefox profile: ")

    # create a loop to read cookies from multiple websites
    while True:
        website = input("Enter the website (enter 'q' to quit): ")
        if website == 'q':
            break
        read_cookies(path, website)
        print()

