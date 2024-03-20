const express = require('express');
const app = express();
const PORT = 3000;

app.post('/create-db', (req, res) => {
    
    res.json({ message: 'DB criação com sucesso!' });
});

app.listen(PORT, () => {
    console.log(`API Gateway rodando na porta ${PORT}`);
});
