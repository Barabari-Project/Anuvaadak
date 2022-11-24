<script>
  import Select from "./select.svelte";
  import Input from "./inputs.svelte";
  import { YT, ws, langs, funcs, ider } from "./lib";
  import { onDestroy, onMount } from "svelte";

  export let _GET, _POST;

  let //
    func = funcs[0],
    lang = langs[0],
    id = ider();

  let //
    outText = "",
    inText = "",
    inURL = "";

  $: isTranslate = func?.text === "Translate";

  onMount(() => {
    ws.onmessage = ({ data }) => console.log(data);
    setInterval(() => ws.send("ping"), 5e3);
  });
  onDestroy(() => ws.close());

  const onSubmit = () => {
    console.log(inText, inURL);
    id = ider();
  };
</script>

<form
  class="p10"
  style="background:rgb(97,65,204);min-width: 100vw;min-height: 100vh;"
  on:submit|preventDefault={onSubmit}
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
      <Input {isTranslate} bind:inURL bind:inText />
    </div>
    <div class="f-col j-ct" style="flex:1;">
      <div
        class="p5 rx20 mx-a fw7 hover_scale"
        style="line-height:1em;background:var(--yellow);color:#222;width:2.5em;height:2.5em;"
      >
        <input
          style="font-size:1.55rem;"
          class="rpm-0 b0 fw7 "
          type="submit"
          value="&rarr;"
        />
      </div>
      <div class="rpm-10" style="background:var(--yellow);color: #000;">
        ID: {id}
      </div>
    </div>
    <div class="lrc">
      <h2>Output</h2>
      <textarea class="rx5 b0 p5" id="output" bind:value={outText} />
    </div>
  </div>
</form>

<style>
  .lrc {
    border: 1px solid green;
    flex: 4;
    height: auto;
  }
  textarea {
    height: auto;
    min-width: 90%;
    background: #fff8;
  }
  textarea:disabled {
    background: #fff4;
    pointer-events: none;
  }
  textarea::placeholder {
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
