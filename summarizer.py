import requests

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from bs4 import BeautifulSoup
from googletrans import Translator, constants

class NewsSummarizer:
    def __init__(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained("minhtoan/t5-finetune-cnndaily-news")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("minhtoan/t5-finetune-cnndaily-news")
        self.model.eval()
        self.translator = Translator()

    def summarize(self, text, translate_to_id = False):
        if text != "" and text != None:
            tokenized_text = self.tokenizer.encode(text, return_tensors='pt')
            output_id = self.model.generate(tokenized_text, max_length=400)
            output = self.tokenizer.decode(output_id[0], skip_special_tokens=True)
            if not translate_to_id:
                return output
            else:
                translation = self.translator.translate(output, dest='id', src='en')
                return translation.text
        else:
            return ""

    def summarize_url(self, url, translate_to_id = False):
        headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42"
        }
        content = requests.get(url, headers=headers)
        soup = BeautifulSoup(content.content, 'html.parser')
        news_content = "" 
        for item in soup.find_all('p')[:30]:
            if len(item.text) > 200:
                news_content += item.text.strip()

        news_content = " ".join(news_content.split()[:300]).replace(".",". ")

        summarized_text = self.summarize(news_content, translate_to_id=translate_to_id)
        return summarized_text