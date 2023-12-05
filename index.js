import express from "express";
import OpenAI from "openai";


const app = express();
const PORT = 3000;

app.use(express.json());


app.get("/", (req, res) => {
    res.send("Hello World!");
});

app.post("/ObtenerReceta", (req, res) => {
    const parametro1 = req.body.parametro1;
    const parametro2 = req.body.parametro2;

    // Hacer algo con los parámetros
    res.json({ resultado: `Parámetro 1: ${parametro1}, Parámetro 2: ${parametro2}` });
});

app.listen(PORT, () => {
    console.log(`El servidor está escuchando en http://localhost:${PORT}`);
});