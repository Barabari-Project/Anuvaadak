<div align="center">
    <img width="250px" src="./client/public/logo.svg" alt="Anuvaadak Logo"/>
<h2><a href="//anuvaadak.nukes.in">Barabari Anuvaadak</a></h2>
</div>

A wrapper for multiple AI Models built by other people to make it easy to use. Planned API extensions for forms and docs

## Structure
- Server: Python Based (with API)
- Frontend: SvelteKit (JS)
- Docs: Docsify Vue Docs


<!-- ## VARIABLES -->
[BashIcon]: https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Bash_Logo_black_and_white_icon_only.svg/1024px-Bash_Logo_black_and_white_icon_only.svg.png?20180723054438
[PytorchIcon]: https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/PyTorch_logo_icon.svg/1200px-PyTorch_logo_icon.svg.png
[tfIcon]: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Tensorflow_logo.svg/1915px-Tensorflow_logo.svg.png

[MetaIcon]: https://www.freelogovectors.net/svg10/facebook-meta-logo-freelogovectors.net_.svg
[NvidiaIcon]: https://cdn-icons-png.flaticon.com/512/732/732230.png
[GoogleIcon]: https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/2048px-Google_%22G%22_Logo.svg.png
[DeepMindIcon]: https://avatars.githubusercontent.com/u/8596759?s=280&v=4
[OpenAIIcon]: https://seeklogo.com/images/O/open-ai-logo-8B9BFEDC26-seeklogo.com.png

<style>
    img[alt$=".icon"]{
        max-width: 16px;
        max-height: 16px;
        aspect-ratio: 1;
        object-fit: contain;
    }
</style>

## Current Plans for Used Models
| Icon                           | Name       |
|--------------------------------|------------|
| ![DeepMind.icon][DeepMindIcon] | DeepMind   |
| ![OpenAI.icon][OpenAIIcon]     | OpenAI     |
| ![Google.icon][GoogleIcon]     | Google     |
| ![Meta.icon][MetaIcon]         | Meta       |
| ![Nvidia.icon][NvidiaIcon]     | Nvidia     |
| ![tf.icon][tfIcon]             | TensorFlow |
| ![pytorch.icon][PytorchIcon]   | Pytorch    |
| ![bash.icon][BashIcon]   | Shell/Binary    |

Format: `NameLink [Model | Implementation(s)] - Usage`

- [x] ![bash.icon][BashIcon] [OpenAI/Whisper](https://github.com/openai/whisper) [![OpenAI.icon][OpenAIIcon] | ![OpenAI.icon][OpenAIIcon]] - Transcription followed by Translation
- [x]![bash.icon][BashIcon]  [OpenAI/GPT3](https://openai.com/api/) [![OpenAI.icon][OpenAIIcon] | ![OpenAI.icon][OpenAIIcon]] - Translation
- [] ![pytorch.icon][PytorchIcon] [Nvidia Tacotron2](https://pytorch.org/hub/nvidia_deeplearningexamples_tacotron2/) [ ![Google.icon][GoogleIcon] | ![Nvidia.icon][NvidiaIcon]  ] - For Audio Synthesis
- [] [Nvidia Tacotron2](https://pytorch.org/hub/nvidia_deeplearningexamples_tacotron2/) [ ![Google.icon][GoogleIcon] | ![Nvidia.icon][NvidiaIcon]  ] - For Audio Synthesis
- [] [Nvidia Tacotron2](https://pytorch.org/hub/nvidia_deeplearningexamples_tacotron2/) [ ![Google.icon][GoogleIcon] | ![Nvidia.icon][NvidiaIcon]  ] - For Audio Synthesis




## Optimisations & Planned Features
- Whisper - https://github.com/openai/whisper/discussions/208 (CPP)
- https://developers.redhat.com/blog/2017/11/16/speed-python-using-rust#now_let_s_build_it_with_cargo
- https://sanic.dev/en/guide/getting-started.html#install
- https://github.com/mozilla/TTS#example-synthesizing-speech-on-terminal-using-the-released-models


## Features
- Directly Transcribe and Translate Youtube Video from URL
- Translate english to [any more languages 0 config]
    - Bengali
    - English
    - Hindi