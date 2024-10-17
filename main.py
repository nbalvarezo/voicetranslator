import gradio as gr
import whisper


def translator(audio_file):
    model = whisper.load_model("base")
    model.transcribe


web = gr.Interface(
    fn  = translator,
    inputs = gr.Audio(
        sources = "microphone",
        type = "filepath"
    ),
    outputs = [],
    title = "Traductor de Voz",
    description = "By _an0mia"
)

web.launch()

