const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const app = express();
const port = 30005;
const API_KEY = 'adb34e2491e6eb3fbe5c1d142e9f749015af3afcb07071864696c0b53fa0dab6';
app.use(express.json());
app.use(bodyParser.json)

app.post('/istek', async (req, res) => {
  console.log(req.body);
  const url = req.body.url;

  if(!url){
    return res.status(400).json({error: "url gerekli"})
  }

  try {
    const response = await axios.post('https://www.virustotal.com/api/v3/urls',
      { url },
      { headers: { 'x-apikey': API_KEY } }
    );
    res.json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'hata' });
  }
});

app.listen(port, () => {
  console.log(`Sunucu ${port} nolu portta çalışıyor`);
});