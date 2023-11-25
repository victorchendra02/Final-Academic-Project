import json
import pandas as pd
# from ..packages.textstyling import TextStyle


def read_json(fname: str) -> dict:
    with open(fname, "r") as file:
        data = json.load(file)
    return data

def display_dictionary(d: dict):
    print(json.dumps(d, indent=4))


data = read_json("./data/data.json")
data = data["Contest Collections"]["International Contests"]
df = pd.DataFrame(
    {
        "id_key": [0],
        "no": ["Default"],
        "contest_category": ["Default"],
        "contest_name": ["Default"],
        "year": ["Default"],
        "link": ["Default"],
        "pdf": ["Default"],
        "post_rendered": ["Default"],
        "post_canonical": ["Default"],
        "label": ["Default"]
    }
)

for i, contest_name in enumerate(list(data.keys())[1:]):
    for j, year in enumerate(list(data[contest_name].keys())):
        new_record = {
            "id_key": [None],
            "no": [None],
            "contest_category": ["International Contest"],
            "contest_name": [contest_name],
            "year": [year],
            "link": [data[contest_name][year]['link']],
            "pdf": [data[contest_name][year]['pdf']],
            "post_rendered": [None],
            "post_canonical": [None],
            "label": [None]
        }
        
        for item in data[contest_name][year]['items']:
            new_record['id_key'] = [df.iloc[-1]['id_key'] + 1]
            new_record['no'] = [str(item["no"])]
            new_record['post_rendered'] = [str(item["post_rendered"])]
            new_record['post_canonical'] = [str(item["post_canonical"])]
            new_record['label'] = [str(item["label"])]
            
            new_record = pd.DataFrame(new_record)
            df = pd.concat([df, new_record], ignore_index=True)


# bcolors = TextStyle()
df = df.iloc[1:]
df.to_csv('C:/wamp64/www/artofproblemsolving/data/data___.csv', index=False)
# print(bcolors.okgreen("Saved as csv!"))
print("Saved as csv!")
