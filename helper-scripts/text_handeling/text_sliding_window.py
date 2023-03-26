"""This script is used to split text with overlap."""
import re
from typing import List


def sliding_window_text(text: str, amount_of_splits: int = 10) -> List:
    """This function is used to split text with overlap.

    :param text: One string of text
    :type text: str
    :param amount_of_sentences: , defaults to 10
    :type amount_of_sentences: int, optional
    :return: array of strings
    :rtype: list
    """

    results = []
    # loop over the text
    # take the length of the text and divide it by the amount of sentences
    amount = len(text) // amount_of_splits
    for i in range(amount_of_splits):
        # select the amount of sentences but include the last three sentences then move the window
        # make sure that the last sentence is not cut off

        if i == amount_of_splits - 1:
            selected_texts = text[i * amount :]
        else:
            print(i * amount, (i + 1) * amount + 5)
            selected_texts = text[i * amount : (i + 1) * amount + 5]

        # join the selected texts into a single string
        selected_texts = "".join(selected_texts)

        results.append(selected_texts)

    return results


# read the text file
with open("podcast.txt") as tmp_file:
    original_Text = tmp_file.readlines()

# combine the lines into a single string
ORGINAL_TEXT = "".join(original_Text)

# split the text after every . or ? or !
ORGINAL_TEXT = re.split(r"(?<=[.?!]) +", ORGINAL_TEXT)

result_strings = sliding_window_text(ORGINAL_TEXT, 10)
# save the results
for j, r in enumerate(result_strings):
    with open(f"text_{j}.txt", "w") as f:
        f.write(r)
