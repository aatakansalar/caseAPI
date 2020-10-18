from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline


class TransformerModel:
    def __init__(self, src="savasy/bert-base-turkish-sentiment-cased"):
        self.model = AutoModelForSequenceClassification.from_pretrained(src)
        self.tokenizer = AutoTokenizer.from_pretrained(src)
        self.pipeline = pipeline("sentiment-analysis", tokenizer=self.tokenizer, model=self.model)

    def analyse(self, text: str):
        return self.pipeline(text)[0]
