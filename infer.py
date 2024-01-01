import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


class Inference:
    def __init__(self):
        base_model_name = "cyberagent/open-calm-7b"
        self.tokenizer = AutoTokenizer.from_pretrained(base_model_name)
        self.base_model = AutoModelForCausalLM.from_pretrained(
            base_model_name,
            device_map='auto',
            load_in_8bit=True
        )

    def gen_text(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.base_model.device)
        with torch.no_grad():
            tokens = self.base_model.generate(
                **inputs,
                max_new_tokens=256,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                repetition_penalty=1.05,
                pad_token_id=self.tokenizer.pad_token_id,
            )

        outputs = self.tokenizer.batch_decode(tokens)
        output = outputs[0]
        return output
