import React from "react"
import ReactDOM from "react-dom"


function Page() {
    return (
        <div>
            <h1>Ordered List:</h1>
            <ol>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ol>
        </div>
    )
}

ReactDOM.render(<Page />, document.getElementById("root"))