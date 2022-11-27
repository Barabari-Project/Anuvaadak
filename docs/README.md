# Anuvaadak
<a
    href="//anuvaadak.nukes.in" class="try b0 d-ib rx10"
    style="font-size: 18px !important;line-height: 0.5em;padding: 12px 16px;background: var(--theme-color);color: #fff !important;"
    >
    <img class="b0 icon" src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/globe.svg" style="height: 1em;filter: invert(100%);margin-right: 5px;">
    <span class="p-rel" style="font-size:0.9em; top:-4px;">Try Now</span>
</a>

A translator wrapper for TBP internal usage, will probably extend with APIs to automatically generate resources like forms

<div align="center">
    <img class="mx-a b0" height="300px" width="300px" src="./assets/logo.svg" />
</div>


## Features
- Directly Transcribe and Translate Youtube Video from URL
- Translate english to [any more languages 0 config]
    - Bengali
    - English
    - Hindi


## Structure
```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server/FFI
    participant M as Model

    C->>S: Websocket Stream
    S->>M: Bulk Model Call
    activate M
    M->>S: Bulk Model Reply
    deactivate M
    S->>C: Websocket Stream
```
