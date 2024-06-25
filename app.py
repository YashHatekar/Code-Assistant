import requests
import json
import gradio as gr

url = 'http://localhost:11434/api/generate'

headers = {
    'Content-Type':'application/json'
}
history = []

def gen_resp(prompt):
    history.append(prompt)
    final_prompt = '\n'.join(history)
    
    data = {
        'model':'TeachCode',
        'prompt':final_prompt,
        'stream':False
    }
    
    response = requests.post(url, headers=headers,data=json.dumps(data))
    
    if response.status_code==200:
        response= response.text
        data = json.loads(response)
        actual_resp = data['response']
        return actual_resp
    else:
        print('Error: ', response.text)
interface = gr.Interface(
    fn = gen_resp,
    inputs = gr.Textbox(lines=4, placeholder='Enter your prompt'),
    outputs = 'text'
)
interface.launch()