import fastapi
from fastapi import FastAPI
import gradio as gr
import json


CUSTOM_PATH = "/"

app = FastAPI()

def greet(*args):
    print(*args)
    request = gr.Request()
    print("Request headers dictionary:", request.headers)
    print("IP address:", request.client.host)
    return "Hello " + args[0] + "!"

with gr.Blocks(theme=gr.themes.Base(), css="footer {visibility:hidden}") as demo:
    with gr.Row():
        html = open("./test.html", "r").read()
        gr.HTML(html)

    with gr.Column():
        input1 = gr.Textbox(label="输入1", placeholder="subject")
        input2 = gr.Radio(["ate", "loved", "hated"])

        output1 = gr.Textbox(label="output")

        btn = gr.Button("Create sentence.")
        btn.click(greet, [input1, input2], output1)
    


app = gr.mount_gradio_app(app, demo, path=CUSTOM_PATH)

    



