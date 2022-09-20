import React from "react"
import "./style.css"
import Navbar from "./components/Navbar"
import Main from "./components/Main"


export default function App() {
    return (
        <div className="container">
            <Navbar />
            <Main />
        </div>
    )
}