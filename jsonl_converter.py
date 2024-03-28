import json
import pandas as pd

DEFAULT_SYSTEM_PROMPT = 'Du bist ein Assisten unseres Kunden und hilfst ihm zu verstehen was auf unserer Webseite angeboten werden'

def create_dataset(question, answer):
    return {
        "messages": [
            {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer},
        ]
    }

if __name__ == "__main__":
    df = pd.read_csv("myFiles/file.csv", encoding='cp1252')
    with open("train2.jsonl", "w") as f:
        for _, row in df.iterrows():
            example_str = json.dumps(create_dataset(row["Question"], row["Answer"]))
            f.write(example_str + "\n")

