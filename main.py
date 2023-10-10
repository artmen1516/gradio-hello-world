import gradio as gr

title = "Welcome to Gradio!"
description = "This is a demo of a Gradio app."
ref = "Find the whole code [here](https://github.com/artmen1516/gradio-hello-world)."

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text", title=title, description=description, article=ref)
    
demo.launch(server_name="0.0.0.0", server_port=8080)
