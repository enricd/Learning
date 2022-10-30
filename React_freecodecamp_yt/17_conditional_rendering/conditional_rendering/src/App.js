import React from "react"
import "./styles.css"
import Joke from "./Joke"
import jokesData from "./jokesData"

export default function App() {

    const [messages, setMessages] = React.useState(["a", "b"])

    let display_message = ""
    if (messages.length === 1) {
        display_message = "You have 1 unread message"
    } else if (messages.length > 1) {
        display_message = `You have ${messages.length} unread messages`
    } else {
        display_message = "You're all caught up!"
    }

    const jokeElements = jokesData.map(joke => {
        return (
            <Joke 
                key={joke.id}
                setup={joke.setup} 
                punchline={joke.punchline} 
            />
        )
    })


    return (
        <div>
            {
                <h1>{display_message}</h1>
            }
            <hr />
            <hr />
            {jokeElements}
        </div>
    )
}



// Quiz

// Condition rendering is a way to consider or not a thing should be displayed or what
// should be displayed

// The && operator is good for display something or not {bool && display_string}

// The ternary operator is good to choose which of two options should be displayed

// If there are more than 2 options to be displayed, use regular if, else if, else logic 
// or a switch