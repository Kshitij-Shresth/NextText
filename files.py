text_df = pd.read_csv("data.csv")
text = list(text_df['sentence'].values)
joined_text = "".join(text)

tokenizer = RegexpTokenizer(r"\w+")
tokens = tokenizer.tokenize(partial_text.lower())
