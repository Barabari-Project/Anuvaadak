from scipy.io.wavfile import write
import torch

# TODO: MAP CUDA TO CPU ONLY
waveglow = torch.hub.load(
    'NVIDIA/DeepLearningExamples:torchhub', 'nvidia_waveglow', model_math='fp32')
# Prepare the WaveGlow model for inference
waveglow = waveglow.remove_weightnorm(waveglow)
waveglow = waveglow.to('cuda')
waveglow.eval()
# Load a pretrained Tacotron2 model
tacotron2 = torch.hub.load(
    'NVIDIA/DeepLearningExamples:torchhub', 'nvidia_tacotron2', model_math='fp32')
tacotron2 = tacotron2.to('cuda')
tacotron2.eval()

# MAIN
text = "hello world, I missed you so much"
utils = torch.hub.load(
    'NVIDIA/DeepLearningExamples:torchhub', 'nvidia_tts_utils')
sequences, lengths = utils.prepare_input_sequence([text])

with torch.no_grad():
    mel, _, _ = tacotron2.infer(sequences, lengths)
    audio = waveglow.infer(mel)
audio_numpy = audio[0].data.cpu().numpy()
rate = 22050

write("audio.wav", rate, audio_numpy)
