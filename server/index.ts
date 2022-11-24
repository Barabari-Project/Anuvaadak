// To run this example: bun --hot server.js
const str = data => typeof data === "string" ? data : JSON.stringify(data)

// Current-Total-UUID
type ID = `${number}-${number}-${string}`;
type Functor = "translate" | "transcribe";
type Input = `${ID}::${Functor}::${string}`;
// ID::functor::DATA

export default {
    websocket: {
        message (ws, msg: Input) {
            ws.send(`${str(msg)} ${Date.now()} HII`);
        },
    },
    fetch (req, server) {
        if (server.upgrade(req)) {
            console.log("SOCKED");

            return new Response("", { status: 101 });
        }
        return new Response("Hu");
    },
};