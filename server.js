const http = require('http')
const port = 3000


const handler = (request, response) => {
    console.log("new user!")
    response.end('Hello node')
}
const server = http.createServer(handler)

server.listen(port, (err) => {
    if (err){
        return console.log('Something is wrong...')
    }

    console.log("Running...")

})
