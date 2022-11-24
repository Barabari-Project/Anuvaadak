<script>
    export let isTranslate;
    export let inURL, inText;
</script>

<h4 class:disabled={isTranslate}>Transcription URL</h4>
<input
    bind:value={inURL}
    class="rx5 b0 p5"
    type="text"
    placeholder={isTranslate ? "disabled" : "Enter URL"}
    disabled={isTranslate}
/>
<br />
<h4 class:disabled={!isTranslate}>Raw Text</h4>
<textarea
    bind:value={inText}
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
    textarea {
        min-height: 170px;
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
