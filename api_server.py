'''
Loads and serves model generations over port 5000.
'''


from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
#import os
#os.environ["CUDA_VISIBLE_DEVICES"]="1,2"


app = Flask(__name__)

model_id = "tiiuae/falcon-40b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map={"": 0},
)

pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

@app.route('/generate', methods=['POST'])
def generate():
    content = request.json
    inp = content.get("text", "")

    sequences = pipeline(
        inp,
        max_length=1024,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
    )

    decoded = sequences[0]['generated_text']
    return jsonify({'generated_text': decoded})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Set the host to '0.0.0.0' to make it accessible from your local network
