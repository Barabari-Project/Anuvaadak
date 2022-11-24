<script>
    export let //
        options,
        selected;
</script>

<div class="select hover_scale">
    <select bind:value={selected}>
        {#each options as op}
            <option value={op}>{op.text}</option>
        {/each}
    </select>
</div>

<style>
    :root {
        --darkgray: 250, 222, 10;
    }

    select {
        appearance: none;
        outline: 0;
        border: 0;
        box-shadow: none;
        /* Personalize */
        font-size: 16px;
        flex: 1;
        padding: 0 0.75em;
        color: #000;
        background-color: rgb(var(--darkgray));
        background-image: none;
    }

    /* Remove IE arrow */
    select::-ms-expand {
        display: none;
    }
    .select {
        position: relative;
        display: flex;
        width: 9em;
        height: 2.75em;
        border-radius: 0.25em;
        overflow: hidden;
    }
    /* Arrow */
    .select::after {
        content: "\25BC";
        color: #000;
        position: absolute;
        top: 4px;
        right: 2px;
        padding: 0.6em;
        transition: 0.25s all ease;
        pointer-events: none;
    }
</style>
