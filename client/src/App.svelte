<script>
  import Select from "./select.svelte";
  let funcs = [
    { id: 1, text: `Translate` },
    { id: 2, text: `Transcribe` },
  ];
  let langs = [
    { id: 1, text: `Hindi` },
    { id: 2, text: `Bengali` },
  ];
  let //
    selected,
    lang;

  const getState = (state, lang) => {
    let output = "";
    if (state) output += state.text;
    if (lang) output += " to " + lang.text;
    return output;
  };
</script>

<form class="p10" style="background:rgb(97,65,204);">
  <div class="head p20">
    <h1>Barabari Anuvaadak: <i>{getState(selected, lang)}</i></h1>
    <Select options={funcs} bind:selected />
    <Select options={langs} bind:selected={lang} />
  </div>

  <div class="f fw w-100 tc" style="min-height: 75vh;height:auto;">
    <div class="lrc">
      LHS
      <textarea class="rx5 b0" name="out" id="out" />
    </div>
    <div class="f-col j-ct" style="flex:1;">
      <div
        class="p5 rx20 mx-a fw7"
        style="font-size:1.25rem;line-height: 1em;background:var(--yellow);color:#222;width:1.5em;height:1.5em;"
      >
        &rarr;
      </div>
    </div>
    <div class="lrc">
      <h2>Output</h2>
      <textarea class="rx5 b0" name="out" id="out" />
    </div>
  </div>
</form>

<style>
  form {
    min-width: 100vw;
    min-height: 100vh;
  }
  .lrc {
    border: 1px solid green;
    flex: 4;
    height: auto;
  }
  .head {
    width: calc(100% - 40px);
  }
  textarea {
    min-height: 300px;
    height: auto;
    min-width: 90%;
    background: #fff8;
  }
  :root {
    --purple: #a4f;
    --yellow: #fadf0b;
  }
</style>
