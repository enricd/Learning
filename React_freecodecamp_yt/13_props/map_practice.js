// Challenge 1
const nums = [1, 2, 3, 4, 5]

const squared = nums.map(function(num) {
    return num * num
})

console.log(squared)


// Challenge 2
const names = ["alice", "bob", "charlie", "danielle"]

const uppercase = names.map((name) => {
    return name[0].toUpperCase() + name.slice(1)
})

console.log(uppercase)


// Challenge 3
const pokemon = ["Bulbasur", "Charmander", "Squirtle"]

const elements = pokemon.map(mon => `<p>${mon}</p>`)

console.log(elements)