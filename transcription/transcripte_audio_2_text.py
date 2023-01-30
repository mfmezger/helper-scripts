import nemo.collections.asr as nemo_asr

asr_model = nemo_asr.models.ASRModel.from_pretrained("nvidia/stt_en_conformer_transducer_xlarge")

transcriptions = asr_model.transcribe(["audio.mp3"])

# save the transcpription to a file
with open('transcription.txt', 'w') as f:
    # save the string to file
    f.write(transcriptions)

