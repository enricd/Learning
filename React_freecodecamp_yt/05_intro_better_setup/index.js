import React from "react"

// Challenge: find out what happens if we try to append JSX to our div#root using
// .append() instead of ReactDOM

const page = (
    <div>
        <h1>My awesome website in React</h1>
        <h3>Reasons I love React</h3>
        <ol>
            <li>It's composable</li>
            <li>It's declarative</li>
            <li>It's a hireable skill</li>
            <li>It's actively maintained by skilled people</li>
        </ol>
    </div>
)

document.getElementById.append(page)    // it will display [object Object] on the webpage
document.getElementById.append(JSON.stringify(page))   // will display the conten of the obje
// This was to show how JSX only returns plain JS objects which browser cannot display as we intended
// It's ReactDOM.render who properly handles them and display as intended


// ReactDOM.render(page, document.getElementById("root"))
