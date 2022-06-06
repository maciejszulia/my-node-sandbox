const express = require("express")
const setFunctions = require("./setFunctions.js")
const port = 3001


const app = express()
app.set('view engine', 'hbs')

app.get('/', function (request, response) {


    const title = setFunctions.generateTitle()
    const body = setFunctions.generateBody()

    response.render('index', {
        pageTitle: title,
        pageBody: body
    })
})

app.get('/kontakt', function (request, response) {
    response.send('Catch me at maciej.szulia@gmail.com')
})

// app.get('/parser', function (request, response){
//     response.render('parser'{
//         pageTitle: 'pyscript json maker'
//     })
// })

app.listen(port)