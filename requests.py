import json

ppl = []

   
    

with open('pending_follow_requests.json') as igfile:
    data=igfile.read()       
    
    
obj = json.loads(data)

values_list = [
    item["value"]
    for request in obj["relationships_follow_requests_sent"]
    for item in request["string_list_data"]
]

print(" ".join(values_list))

with open('pending.txt', 'w') as output_file:
    output_file.write("\n".join(values_list))