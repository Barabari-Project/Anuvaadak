// https://github.com/lau1944/bunrest
import type { BunRequest, BunResponse } from "./index.d.ts"
import server from "bunrest";

const app = server();
const PORT = process.env.port || 3000;

app.get('/test', (req: BunRequest, res: BunResponse) => {
    res.status(200).json({ message: req.query });
});

app.put('/test/:id', (req: BunRequest, res: BunResponse) => {
    res.status(200).json({ message: req.params?.id });
});

app.post('/test/:id/:name', (req: BunRequest, res: BunResponse) => {
    res.status(200).json({ message: req.params });
});

app.listen(PORT, () => console.log('App is listening on port ' + PORT));