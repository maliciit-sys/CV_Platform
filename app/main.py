"""Gradio UI — the 'face'.

v0.0.2 adds a History tab backed by the database. The UI still knows nothing
about how prediction or storage works — it just wires widgets to functions.
"""
import gradio as gr

from app import database
from app.inference import predict

# Ensure the database and table exist before the app starts.
database.init_db()


def classify(image):
    """Predict, persist, and return the labels for display."""
    predictions = predict(image)
    database.save_prediction(image, predictions)
    return predictions


with gr.Blocks(title="CV Platform — v0.0.2") as demo:
    gr.Markdown(
        "# CV Platform — v0.0.2\n"
        "Upload an image to classify it. Every prediction is saved to History."
    )

    with gr.Tab("Classify"):
        image_input = gr.Image(type="pil", label="Upload an image")
        label_output = gr.Label(num_top_classes=3, label="Predictions")
        classify_btn = gr.Button("Classify", variant="primary")
        classify_btn.click(fn=classify, inputs=image_input, outputs=label_output)

    with gr.Tab("History"):
        gr.Markdown("Recent predictions, newest first.")
        history_table = gr.Dataframe(
            headers=["Time", "Top prediction", "Confidence"],
            interactive=False,
        )
        refresh_btn = gr.Button("Refresh")
        refresh_btn.click(fn=database.get_history, inputs=None, outputs=history_table)

    # Populate history when the app loads.
    demo.load(fn=database.get_history, inputs=None, outputs=history_table)


if __name__ == "__main__":
    demo.launch()