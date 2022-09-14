import React from "react"
import ReactDOM from "react-dom"


function Header() {
    return (
        <header>
            <nav className="nav">
                <img src="../images/react-logo.png" className="nav-logo" />
                <ul className="nav-items">
                    <li>Pricing</li>
                    <li>About</li>
                    <li>Contact</li>
                </ul>
            </nav>
        </header>
    )
}

function Content() {
    return (
        <div>
            <h1>Learning React</h1>
            <ol>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ol>
        </div>
    )
}

function Footer() {
    return (
        <footer>
            <small>@ 2022 Enric development.</small>
        </footer>
    )
}

function Page() {
    return (
        <div>
            <Header />
            <Content />
            <Footer />
        </div>
    )
}

ReactDOM.render(<Page />, document.getElementById("root"))


// Quiz:

// A React component is a function that returns React elements.
// React elements are objects that are created when JSX is returned from a React component. (UI)
// React components can be reused many times.

// A React component needs to be created with Pacal case (First letter capitalized and camel case then)
// function MyComponent()

// ReactDOM.render(<Header />, document.getElementById("root"))
