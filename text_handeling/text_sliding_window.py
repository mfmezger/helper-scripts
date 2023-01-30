import re


def sliding_window_text(text, amount_of_sentences=10):

    results = []
    # loop over the text 
    # take the length of the text and divide it by the amount of sentences
    amount = int(len(text) / amount_of_sentences)
    for i in range(0, amount_of_sentences):
        # select the amount of sentences but include the last three sentences then move the window
        # make sure that the last sentence is not cut off

        if i == amount_of_sentences - 1:
            selected_texts = text[i*amount:]
        else:
            print(i*amount, (i+1)*amount+5)
            selected_texts = text[i*amount:(i+1)*amount+5]

        

        # join the selected texts into a single string
        selected_texts = ''.join(selected_texts)

        results.append(selected_texts)

    return results


# read the text file
with open('podcast.txt', 'r') as f:
    text = f.readlines()

# combine the lines into a single string
text = ''.join(text)

# split the text after every . or ? or !
text = re.split(r'(?<=[.?!]) +', text)

results = sliding_window_text(text, 10)
# save the results
for i, r in enumerate(results):
    with open(f'text_{i}.txt', 'w') as f:
        f.write(r)

