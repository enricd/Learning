import React from "react"
import ReactDOM from "react-dom"
import "./style.css"
import Header from "./Header"
import Content from "./Content"
import Footer from "./Footer"


export default function App() {
    return (
        <div>
            <Header />
            <Content />
            <Footer />
        </div>
    )
}

ReactDOM.render(<App />, document.getElementById("root"))


