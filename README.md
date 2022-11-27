<div align="center">
    <img width="250px" src="./client/public/logo.svg" alt="Anuvaadak Logo"/>
<h2><a href="//anuvaadak.nukes.in">Barabari Anuvaadak</a></h2>
</div>

A wrapper for multiple AI Models built by other people to make it easy for the Barabari Team to use. Planned API extensions for forms and docs

<!-- ## VARIABLES -->
[BashIcon]: ./docs/assets/bash.svg
[PytorchIcon]: ./docs/assets/pytorch.svg
[tfIcon]: ./docs/assets/tf.svg

[MsftIcon]: ./docs/assets/microsoft.svg
[MetaIcon]: ./docs/assets/meta.png
[NvidiaIcon]: ./docs/assets/nvidia.svg
[GoogleIcon]: ./docs/assets/google.svg
[DeepMindIcon]: ./docs/assets/deepmind.png
[OpenAIIcon]: ./docs/assets/openai.png

## Current Model Plans
| Icon                           | Name       | |Icon| Name|
|--------------------------------|------------|-|-|-|
| ![DeepMind.icon][DeepMindIcon] | DeepMind   | | ![Microsoft.icon][MsftIcon]         | Microsoft |
| ![OpenAI.icon][OpenAIIcon]     | OpenAI     | | ![Meta.icon][MetaIcon]         | Meta       |
| ![Google.icon][GoogleIcon]     | Google     | | ![Nvidia.icon][NvidiaIcon]     | Nvidia     |

<!-- | ![tf.icon][tfIcon]             | TensorFlow |
| ![pytorch.icon][PytorchIcon]   | Pytorch    |
| ![bash.icon][BashIcon]   | Shell/Binary    | -->

Format: `NameLink [Model | Implementation(s)] : Usage`

- [x] ![bash.icon][BashIcon] [OpenAI/Whisper](https://github.com/openai/whisper) [![OpenAI.icon][OpenAIIcon] | ![OpenAI.icon][OpenAIIcon]] : Transcription followed by Translation
- [x] ![bash.icon][BashIcon]  [OpenAI/GPT3](https://openai.com/api/) [![OpenAI.icon][OpenAIIcon] | ![OpenAI.icon][OpenAIIcon]] : Translation
- [ ] ![pytorch.icon][PytorchIcon] [Nvidia Tacotron2](https://pytorch.org/hub/nvidia_deeplearningexamples_tacotron2/) [ ![Google.icon][GoogleIcon] | ![Nvidia.icon][NvidiaIcon]  ] : For Audio Synthesis [Repo](https://github.com/NVIDIA/tacotron2)
- [ ] ![pytorch.icon][PytorchIcon] [Silero Models](https://analyticsvidhya.com/blog/2022/06/multilingual-text-to-speech-models-for-indic-languages/) [ ? | ?  ] : For Indic Specific Audio Synthesis
- [ ] ![pytorch.icon][PytorchIcon] [Indpenedent Tacotron2](https://github.com/Tomiinek/Multilingual_Text_to_Speech) [ ? | ?  ] : For Audio Synthesis
- [ ] ![pytorch.icon][PytorchIcon] [Indpenedent Tacotron2](https://github.com/Tomiinek/Multilingual_Text_to_Speech) [ ? | ?  ] : For Audio Synthesis

## Optimisations & Planned Features
- Whisper : https://github.com/openai/whisper/discussions/208 (CPP)
- https://developers.redhat.com/blog/2017/11/16/speed-python-using-rust#now_let_s_build_it_with_cargo
- https://sanic.dev/en/guide/getting-started.html#install
- https://github.com/mozilla/TTS#example-synthesizing-speech-on-terminal-using-the-released-models


## Features
- Directly Transcribe and Translate Youtube Video from URL
- Translate english to x language
- Synthesize Speech from x text in same language