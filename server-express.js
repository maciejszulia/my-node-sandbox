const express = require("express")
const port = 3001

const generateTitle = () => {
    var pageTitle = 'Node js'
    console.log('changed page title: ', pageTitle)
    return pageTitle
}

const generateBody = () => {
    var pageBody = 'Hello world!!'
    console.log('changed page body: ', pageBody)
    return pageBody
}

const app = express()
app.set('view engine', 'hbs')

app.get('/', function (req, res) {

    const title = generateTitle()
    const body = generateBody()

    res.render('index', {
        pageTitle: title,
        pageBody: body
    })
})

app.get('/kontakt', function (req, res) {
    res.send('Catch me at maciej.szulia@gmail.com')
})

app.listen(port)