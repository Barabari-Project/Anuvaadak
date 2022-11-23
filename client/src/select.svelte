<script>
    export let //
        options,
        selected;
</script>

<div class="select">
    <select bind:value={selected}>
        {#each options as op}
            <option value={op}>{op.text}</option>
        {/each}
    </select>
</div>

<style>
    :root {
        --gray: #34495e;
        --darkgray: #2c3e50;
    }

    select {
        /* Reset Select */
        appearance: none;
        outline: 0;
        border: 0;
        box-shadow: none;
        /* Personalize */
        font-size: 16px;
        flex: 1;
        padding: 0 0.75em;
        color: #fff;
        background-color: var(--darkgray);
        background-image: none;
        cursor: pointer;
    }
    /* Remove IE arrow */
    select::-ms-expand {
        display: none;
    }
    /* Custom Select wrapper */
    .select {
        position: relative;
        display: flex;
        width: 10em;
        height: 3em;
        border-radius: 0.25em;
        overflow: hidden;
    }
    /* Arrow */
    .select::after {
        content: "\25BC";
        position: absolute;
        top: 2px;
        right: 2px;
        padding: 0.82em;
        transition: 0.25s all ease;
        pointer-events: none;
    }
</style>
