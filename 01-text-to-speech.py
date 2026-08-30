import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

load_dotenv()

speech_config = speechsdk.SpeechConfig(
    subscription=os.getenv("SPEECH_KEY"),
    endpoint=os.getenv("SPEECH_ENDPOINT")
)

# voice
speech_config.speech_synthesis_voice_name =  "en-US-AvaNeural"

# okay through computer speaker
audio_config = speechsdk.audio.AudioOutputConfig(
    use_default_speaker=True
)

synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config,
    audio_config=audio_config
)

# text = input("Enter text: ")
text = """
<speak version="1.0"
       xmlns="http://www.w3.org/2001/10/synthesis"
       xml:lang="en-US">

    <voice name="en-US-AvaNeural">

        Hello, world!

        <break time="700ms"/>

        I just don't know
        <break time="500ms"/>
        if I can handle this anymore.

    </voice>
</speak>
"""

result = synthesizer.speak_ssml_async(text).get()

# result = synthesizer.speak_text_async(text).get()
result = synthesizer.speak_ssml_async(text).get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized successfully!")

elif result.reason == speechsdk.ResultReason.Canceled:
    details = result.cancellation_details
    print("Speech synthesis canceled:", details.reason)

    if details.error_details:
        print("Error:", details.error_details)