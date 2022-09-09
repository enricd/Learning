import React from "react"
import ReactDOM from "react-dom"

const page = (
    <div>
        <img src="../images/react-logo.png" width="40px" />
        <h1>Fun facts about React</h1>
        <ul>
            <li>Was first released in 2013</li>
            <li>Ws originally created by Jordan Walker</li>
            <li>Has well over 100K stars on GitHub</li>
            <li>Is maintained by Facebook</li>
            <li>Powers thousands of enterprise apps, including mobile apps</li>
        </ul>
    </div>
)

ReactDOM.render(page, document.getElementById("root"))


// --- Pop quiz ---

// React defines and is required by JSX
// console.log(page) will display a JS object
// We need our JSX to be nested under a single parent element
// React is declarative, so we only tell what to do and not how
// React is composable, it makes small pieces that together form the webpage