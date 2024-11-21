import json

# Load both JSON files
with open('followers_1.json', 'r') as file1, open('following.json', 'r') as file2:
    followers_data = json.load(file1)
    following_data = json.load(file2)

# Extracting "value" fields from "followers_1.json"
followers_values = {
    item["value"]
    for entry in followers_data
    for item in entry["string_list_data"]
}

# Extracting "value" fields from "following.json"
following_values = {
    item["value"]
    for entry in following_data["relationships_following"]
    for item in entry["string_list_data"]
}

# Find values that are in following but not in followers
unique_following = following_values - followers_values

# Write unique values to 'followers.txt', each on a new line
with open('followers.txt', 'w') as output_file:
    output_file.write("\n".join(unique_following))
