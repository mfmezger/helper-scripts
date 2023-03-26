from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor

processor = AutoProcessor.from_pretrained("openai/whisper-large")

model = AutoModelForSpeechSeq2Seq.from_pretrained("openai/whisper-large")
