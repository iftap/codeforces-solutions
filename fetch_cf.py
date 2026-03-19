import requests
import os
import re

handle = "nullptr__07"   # change to your handle

url = f"https://codeforces.com/api/user.status?handle={handle}"
data = requests.get(url).json()

solved = set()

for sub in data['result']:
    if sub['verdict'] == "OK":
        p = sub['problem']

        if 'rating' not in p:
            continue

        key = (p['contestId'], p['index'])

        if key in solved:
            continue

        solved.add(key)

        rating = str(p['rating'])

        name = re.sub(r'[\\/*?:"<>|]', '', p['name'])
        name = name.replace(" ", "_")

        contest = p['contestId']
        index = p['index']

        folder = rating
        os.makedirs(folder, exist_ok=True)

        filename = f"{folder}/{contest}{index}_{name}.cpp"

        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write(f"""/*
Problem: {p['name']}
Rating: {rating}
Link: https://codeforces.com/problemset/problem/{contest}/{index}
*/

#include <bits/stdc++.h>
using namespace std;

int main(){{
    return 0;
}}
""")

print("Done!")
