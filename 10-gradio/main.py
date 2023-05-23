from fastapi import FastAPI
import gradio as gr
import json


CUSTOM_PATH = "/"

app = FastAPI()

def greet(*args):
    return "Hello " + args[0] + "!"

with gr.Blocks(theme=gr.themes.Base(), css="footer {visibility:hidden}") as demo:
    # with gr.Row():
    #     with gr.Column(scale=5):
    #         md = gr.Markdown("## Hello World")
    #     with gr.Column(scale=1):
    #         btn_open = gr.Button("Open")
    #         btn_open.click(None, None, None,_js="() => alert('https://www.baidu.com');")
    with gr.Row():
        html = open("./test.html", "r").read()
        gr.HTML(html)

    with gr.Column():
        input1 = gr.Textbox(label="输入1", placeholder="subject")
        input2 = gr.Radio(["ate", "loved", "hated"])
        input3 = gr.Textbox(placeholder="object")

        output1 = gr.Textbox(label="output 1")
        output2 = gr.Textbox(label="verb")
        output3 = gr.Textbox(label="verb reversed")
        output4 = gr.Textbox(label="front end process and then send to backend")

        btn = gr.Button("Create sentence.")
        btn.click(greet, [input1, input2, input3], output1)


app = gr.mount_gradio_app(app, demo, path=CUSTOM_PATH)

    



