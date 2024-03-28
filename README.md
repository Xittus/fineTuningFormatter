# CSV to JSONL Converter for Fine-Tuning OpenAI GPT

This program converts a CSV file containing questions and answers into a JSONL format suitable for fine-tuning your own OpenAI GPT model. The JSONL format is commonly used for training data in machine learning tasks.

## Usage

1. **Prepare your CSV file**: Ensure your CSV file is formatted with two columns - `Question` and `Answer`, where each row corresponds to a question and its corresponding answer.

2. **Modify Default System Prompt (Optional)**: By default, the system prompt used in the JSONL format is set to: "Du bist ein Assisten unseres Kunden und hilfst ihm zu verstehen was auf unserer Webseite angeboten werden". If you want to change this prompt, modify the `DEFAULT_SYSTEM_PROMPT` variable in the script according to your requirements.

3. **Run the Script**: Execute the provided Python script (`csv_to_jsonl.py`) by running `python csv_to_jsonl.py`. Make sure to replace `"myFiles/file.csv"` with the path to your CSV file. The script will read the CSV file, convert each row into the JSONL format, and write the output to a file named `train2.jsonl`.

## Script Explanation

The script uses Python and the pandas library to read the CSV file and json library to handle JSON data.

It defines a function `create_dataset(question, answer)` which takes a question and its corresponding answer and constructs a dictionary in the required JSONL format.

The main part of the script reads the CSV file, iterates through each row, creates the JSONL format using the `create_dataset` function, and writes it to the output file.

## Dependencies

- Python 3.x
- pandas library

## Example

Suppose you have a CSV file (`file.csv`) with the following content:
```
        Question,Answer
        Hello who are you?,I am a programmer
        How are you?,I'm fine thank you!
```


Running the script with this CSV file will generate a `train2.jsonl` file with the following content:

```
{"messages": [{"role": "system", "content": "Du bist ein Assistent unseres Kunden und hilfst ihm zu verstehen was auf unserer Webseite angeboten werden"}, {"role": "user", "content": "Hello who are you?"}, {"role": "assistant", "content": "I am a programmer"}]}
{"messages": [{"role": "system", "content": "Du bist ein Assistent unseres Kunden und hilfst ihm zu verstehen was auf unserer Webseite angeboten werden"}, {"role": "user", "content": "How are you?"}, {"role": "assistant", "content": "I'm fine, thank you!"}]}
```


This JSONL file can be used for fine-tuning an OpenAI GPT model.



