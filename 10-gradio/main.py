from fastapi import FastAPI
import gradio as gr
import json


CUSTOM_PATH = "/"

app = FastAPI()

get_window_url_params = """
    function(url_params) {
        const params = new URLSearchParams(window.location.search);
        return params.get('t');
        }
    """

def greet(*args):
    print(*args)

    return "Hello " + args[2] + "!"

with gr.Blocks(theme=gr.themes.Base(), css="footer {visibility:hidden}") as demo:
    # with gr.Row():
    #     with gr.Column(scale=5):
    #         md = gr.Markdown("## Hello World")
    #     with gr.Column(scale=1):
    #         btn_open = gr.Button("Open")
    #         btn_open.click(None, None, None,_js="() => alert('https://www.baidu.com');")
    url_params = gr.Textbox(label="url_params", visible=True)
    with gr.Row():
        html = open("./test.html", "r").read()
        gr.HTML(html)

    with gr.Column():
        input1 = gr.Textbox(label="输入1", placeholder="subject")
        input2 = gr.Radio(["ate", "loved", "hated"])

        output1 = gr.Textbox(label="output")

        btn = gr.Button("Create sentence.")
        btn.click(greet, [input1, input2, url_params], output1)
    
    demo.load(
        inputs=None,
        outputs=[url_params],
        queue=True,
        _js=get_window_url_params
    )


app = gr.mount_gradio_app(app, demo, path=CUSTOM_PATH)

    



