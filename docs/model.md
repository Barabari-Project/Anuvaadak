# Model

<!-- ## VARIABLES -->
[BashIcon]: ./assets/bash.svg
[PytorchIcon]: ./assets/pytorch.svg
[tfIcon]: ./assets/tf.svg

[MsftIcon]: ./assets/microsoft.svg
[MetaIcon]: ./assets/meta.png
[NvidiaIcon]: ./assets/nvidia.svg
[GoogleIcon]: ./assets/google.svg
[DeepMindIcon]: ./assets/deepmind.png
[OpenAIIcon]: ./assets/openai.png

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
- [ ] ![pytorch.icon][PytorchIcon] [Indpenedent Tacotron2](https://github.com/Tomiinek/Multilingual_Text_to_Speech) [ ? | ?  ] : For Audio Synthesis

## Optimisations & Planned Features
- Whisper : https://github.com/openai/whisper/discussions/208 (CPP)
- https://developers.redhat.com/blog/2017/11/16/speed-python-using-rust#now_let_s_build_it_with_cargo
- https://sanic.dev/en/guide/getting-started.html#install
- https://github.com/mozilla/TTS#example-synthesizing-speech-on-terminal-using-the-released-models

## Tacotron
Tacotron models will probably have to be manually trained with Common Voice data - https://commonvoice.mozilla.org/en

[Check Here for Usage Example](https://github.com/s3nh/pytorch-tacotron2)