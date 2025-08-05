from transformers import MarianMTModel, MarianTokenizer
import torch

class DualTranslator:
    def __init__(self):
        self.en_fr_model_name = "Helsinki-NLP/opus-mt-en-fr"
        self.fr_en_model_name = "Helsinki-NLP/opus-mt-fr-en"

        self.en_fr_tokenizer = MarianTokenizer.from_pretrained(self.en_fr_model_name)
        self.en_fr_model = MarianMTModel.from_pretrained(self.en_fr_model_name)

        self.fr_en_tokenizer = MarianTokenizer.from_pretrained(self.fr_en_model_name)
        self.fr_en_model = MarianMTModel.from_pretrained(self.fr_en_model_name)

    def en_to_fr(self, text: str) -> str:
        tokens = self.en_fr_tokenizer.prepare_seq2seq_batch([text], return_tensors="pt", truncation=True)
        with torch.no_grad():
            translated = self.en_fr_model.generate(**tokens)
        return self.en_fr_tokenizer.decode(translated[0], skip_special_tokens=True)

    def fr_to_en(self, text: str) -> str:
        tokens = self.fr_en_tokenizer.prepare_seq2seq_batch([text], return_tensors="pt", truncation=True)
        with torch.no_grad():
            translated = self.fr_en_model.generate(**tokens)
        return self.fr_en_tokenizer.decode(translated[0], skip_special_tokens=True)
