import tensorflow as tf 
import numpy as np
import discord 

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

from tensorflow import keras


async def generatePoem(Interaction, opener):
    f = open("sl-poem-data.txt",encoding = "utf-8")
    dat = f.read()
    f.close()

    from keras.models import load_model
    model = load_model('poet.keras')

    tokenizer = Tokenizer()
    corpus = dat.lower().split('\n')
    tokenizer.fit_on_texts(corpus)
    total_words = len(tokenizer.word_index)+1

    input_sequences = []

    for line in corpus:
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i+1]
            input_sequences.append(n_gram_sequence)

    max_sequence_len = max([len(x) for x in input_sequences])

    input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding = 'pre'))

    seed_text = opener
    next_words = 20

    for i in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = np.argmax(model.predict(token_list), axis=-1)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += f" {output_word}"

    count = 0
    for i in range(len(seed_text)):
        if seed_text[i] == " ":
            count+=1
        if count ==4:
            count =0
            seed_text = seed_text[:i] + '\n' + seed_text[(i+1):]
    seed_text+="\n~Silverlight"

    await Interaction.response.send_message(f"{seed_text} ")