# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.

import requests

###1. Importing module
###   import requests
👉 We import the requests library to call APIs (make HTTP requests) from Python.
👉 Here, we use it to talk to GitHub and get pull request data.

# URL to fetch pull requests from the GitHub API
url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'
##### Note: it is a GitHub API endpoint
👉 It means:
repo = kubernetes/kubernetes
/pulls = give all pull requests

👉 This API returns active (open) pull requests by default


# Make a GET request to fetch pull requests data from the GitHub API
response = requests.get(url)  # Add headers=headers inside get() for authentication

###### 👉 .get() = “Go to this URL and bring me data”

###********** 🔹 4. Status code   and 5. Convert JSON → Python
# Only if the response is successful
if response.status_code == 200:
    # Convert the JSON response to a dictionary    ### 👉 Data comes from API in JSON format
    pull_requests = response.json()   ####   👉 .json() converts it into Python list of dictionaries    👉 Important: It’s NOT a single dictionary and It’s a list of dictionaries

  ##### 👉 200 means success (data received correctly)
👉 Not “pull all requests” — it just means the API call worked 


#####🔹 6. Empty dictionary
    # Create an empty dictionary to store PR creators and their counts
    pr_creators = {}
############# Note: 
👉 This is just an empty dictionary
👉 It will store:
Eg: 
{
  "user1": count,
  "user2": count
}


####### 🔹 7. Loop through pull requests
    # Iterate through each pull request and extract the creator's name
    for pull in pull_requests:      #####   👉 We are looping through each pull request , 👉 pull = one PR (a dictionary)
        creator = pull['user']['login']    
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

Note: 
##### 
🔹 8. Extract creator
creator = pull['user']['login']

👉 Each PR has data like:

"user": {
    "login": "username"
}

👉 So:

pull['user'] → user info
['login'] → username


####  🔹 9. Counting logic (VERY IMPORTANT)
if creator in pr_creators:
    pr_creators[creator] += 1
else:
    pr_creators[creator] = 1

Let’s simplify this:

👉 If user already exists → increase count
👉 If new user → start count = 1

Example:

First time:

{"john": 1}

Next PR from john:

{"john": 2}
❌ Your comment correction:
Not “display”
It is counting how many PRs each user created

    # Display the dictionary of PR creators and their counts
    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")

#### Note : Note :  ##### 🔹 10. Printing result
for creator, count in pr_creators.items():
    print(f"{creator}: {count} PR(s)")

👉 .items() gives:

key → creator
value → count

👉 So it prints like:

john: 3 PR(s)
alice: 2 PR(s)

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

🔹 11. Else condition
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

✅ Your understanding is correct:

👉 If API fails → show error code








  
    print(f"Failed to fetch data. Status code: {response.status_code}")
