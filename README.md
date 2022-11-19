<div align="center">
<a  href="//youtu.be/ip51Y5v3WLk">
    <img width="250px" src="./client/public/images/logo.svg" alt="Prime <3"/>
</a>
<h2>Barabari Anuvaadak</h2>
</div>

A translator wrapper for TBP internal usage, will probably extend with APIs to automatically generate resources like forms

> Project currently is both in progress and experimental. Please assume basically everything can change.

## Resources
We will use the following as models
- [OpenAI/Whisper](https://github.com/openai/whisper) - Transcription & Translation
- [OpenAI/GPT3](https://openai.com/api/) - Text Translation

## Structure
- Server: Python Based (with API)
- Model: Idk yet frankly
- Frontend: SvelteKit (JS)
- Docs: Docsify Vue Docs

## Optimisations
Whisper - https://github.com/openai/whisper/discussions/208 (CPP)
