<script>
    export let isTranslate;
</script>

<h4 class:disabled={isTranslate}>Transcription URL</h4>
<input
    class="rx5 b0 p5"
    type="text"
    placeholder={isTranslate ? "disabled" : "Enter URL"}
    disabled={isTranslate}
/>
<br />
<h4 class:disabled={!isTranslate}>Raw Text</h4>
<textarea
    class="rx5 b0 p5"
    placeholder={!isTranslate ? "disabled" : "Enter Text To Translate"}
    id="input"
    disabled={!isTranslate}
/>

<style>
    .disabled {
        opacity: 0.5;
    }
    textarea,
    input[type="text"] {
        height: auto;
        min-width: 90%;
        background: #fff8;
    }
    textarea:disabled,
    input[type="text"]:disabled {
        background: #fff4;
        pointer-events: none;
    }
    textarea::placeholder,
    input[type="text"]::placeholder {
        color: #4448;
    }
</style>
