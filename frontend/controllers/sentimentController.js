import axios from 'axios';

export async function analyzeText(req, res) {
    const { text } = req.body;

    try {
        // Hacer solicitud POST al servidor Flask
        const response = await axios.post('http://localhost:5000/analyze', { text });
        
        // Enviar el resultado a la vista
        res.render('home', { result: response.data });
    } catch (error) {
        res.status(500).json({ error: 'Error al analizar el texto' });
    }
}

export async function renderHome(req, res) {
    res.render('home', { result: null });
}
