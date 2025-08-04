from transformers import MarianMTModel, MarianTokenizer

class Translator:
    def __init__(self, model_name="Helsinki-NLP/opus-mt-en-fr"):
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)

    def translate(self, text: str, max_length=100) -> str:
        tokens = self.tokenizer.prepare_seq2seq_batch([text], return_tensors="pt", truncation=True)
        translated = self.model.generate(**tokens, max_length=max_length)
        return self.tokenizer.decode(translated[0], skip_special_tokens=True)
