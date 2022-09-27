import React from "react"


export default function App() {
    const colors = ["Red", "Blue", "Yellow", "Orange"]
    
    return (
        <div>
            {colors.map(color => `<h3>${color}</h3>`)}
        </div>
)}


const jokesData = [
    {
        setup: "joke 1 part 1",
        punchline: "joke 1 part 2"
    },
    {
        setup: "joke 2 part 1",
        punchline: "joke 2 part 2"
    }
]

export default function App_joke() {
    const jokeElements = jokesData.map(joke => {
        return <Joke setup={joke.setup} punchline={joke.punchline} />
    })
    return (
        <div>
            {jokeElements}
        </div>
    )
}



// Quiz

// The .map() array method takes a function as its parameter and takes every element 
// of the array where it is applied and returns the array of returned function values.

// In React, we use .map() to convert an array of raw data into an array of JSX elements
// that can be displayed on the page.

// Applying .map() in React makes our code more self-sustaining, not requiring additional
// changes whenever the data changes.