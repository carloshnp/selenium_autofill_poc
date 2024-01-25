import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.post('/login', (req, res) => {
    const { email, password } = req.body;
    console.log(`Email: ${email}, Password: ${password}`);
    return res.send({ message: 'Logged in successfully!' }).status(200);
});

app.post('/info', (req, res) => {
    const { text } = req.body;
    console.log(`Text: ${text}`);
    return res.send({ message: 'Info received successfully!' }).status(200);
})

const port = 3000;
app.listen(port, () => console.log(`Server running on http://localhost:${port}`));
