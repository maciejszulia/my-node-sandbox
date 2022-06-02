const greeting = () => {

    console.log("hello node!")
}

const add = (a, b) => {
    console.log(a + b)
}

console.log('Loaded.')

module.exports = {
    greeting,
    add
}
