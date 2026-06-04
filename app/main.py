"""Gradio UI — the 'face'.

This module knows nothing about *how* prediction works. It just wires the
upload widget to inference.predict() and renders the result.
"""
import gradio as gr

from app.inference import predict

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil", label="Upload an image"),
    outputs=gr.Label(num_top_classes=3, label="Predictions"),
    title="CV Platform — v0.0.1",
    description="Upload an image and get the top predictions from a pretrained model.",
)

if __name__ == "__main__":
    demo.launch()