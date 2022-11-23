<script>
  import Select from "./select.svelte";
  import { YT } from "./lib";

  export let _GET, _POST;

  let funcs = Object.freeze([
    { id: 1, text: "Translate" },
    { id: 2, text: "Transcribe" },
  ]);
  let langs = Object.freeze([
    { id: 1, text: "Hindi" },
    { id: 2, text: "Bengali" },
  ]);

  let //
    func = funcs[0],
    lang = langs[0];

  $: isTranslate = func?.text === "Translate";
</script>

<form
  class="p10"
  style="background:rgb(97,65,204);min-width: 100vw;min-height: 100vh;"
  on:submit|preventDefault={console.log}
>
  <div class="p20 f" style="width: calc(100% - 40px);">
    <h1>Barabari Anuvaadak:</h1>
    <div class="f p5" style="margin:0.75em 0;">
      <Select options={funcs} bind:selected={func} />
      <i class="fw7" style="padding: 15px 5px;">To</i>
      <Select options={langs} bind:selected={lang} />
    </div>
  </div>

  <div class="f fw w-100 tc" style="min-height: 75vh;height:auto;">
    <div class="lrc">
      <h2>{func?.text} Input</h2>
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
        name="out"
        id="out"
        disabled={!isTranslate}
      />
    </div>
    <div class="f-col j-ct" style="flex:1;">
      <div
        class="p5 rx20 mx-a fw7"
        style="line-height:1em;background:var(--yellow);color:#222;width:2.5em;height:2.5em;"
      >
        <!-- https://dribbble.com/shots/15041751-Download-animation -->
        <!-- Animations -->
        <input
          style="font-size:1.55rem;"
          class="rpm-0 b0 fw7"
          type="submit"
          value="&rarr;"
        />
      </div>
    </div>
    <div class="lrc">
      <h2>Output</h2>
      <textarea class="rx5 b0 p5" name="out" id="out" />
    </div>
  </div>
</form>

<style>
  .lrc {
    border: 1px solid green;
    flex: 4;
    height: auto;
  }
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
  input[type="submit"]:disabled {
    pointer-events: none;
    opacity: 0.5;
  }
  textarea {
    min-height: 300px;
  }
  :root {
    --purple: #a4f;
    --yellow: #fadf0b;
  }
</style>
