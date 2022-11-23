import server from "bunrest";
const app = server();

app.get('/test', (req, res) => {
    res.status(200).json({ message: req.query });
});

app.put('/test/:id', (req, res) => {
    res.status(200).json({ message: req.params.id });
});

app.post('/test/:id/:name', (req, res) => {
    res.status(200).json({ message: req.params });
});