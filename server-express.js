const express = require("express")
const port = 3001

const app = express()
app.set('view engine', 'hbs')

app.get('/', function (req, res) {
    res.send('Hello express')
})

app.get('/kontakt', function (req, res) {
    res.send('Catch me at maciej.szulia@gmail.com')
})

app.listen(port)