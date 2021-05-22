from transformers import BertTokenizer, BertForSequenceClassification
import torch
import torch.nn as nn
import re

model = BertForSequenceClassification.from_pretrained('./saved_model')
tokenizer = BertTokenizer.from_pretrained('./saved_model')
model.eval()

def clean(text):
    text = re.sub(r'http\S+', " ", text)
    text = re.sub(r'@\w+',' ',text)
    text = re.sub(r'#\w+', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    text = re.sub(r'<.*?>',' ', text)
    return text

def classification (title, body):
  user_input = tokenizer(title,
                        body,
                        padding=True,
                        truncation=True,
                        return_tensors="pt")

  with torch.no_grad():
      outputs = model(user_input['input_ids'], token_type_ids=None, 
                      attention_mask=user_input['attention_mask'])
  logits = outputs[0][0][0]
  result = 1 if float(logits) > 0.5 else 0
  return result


