text_df = pd.read_csv("data.csv")
text = list(text_df['sentence'].values)
joined_text = "".join(text)

