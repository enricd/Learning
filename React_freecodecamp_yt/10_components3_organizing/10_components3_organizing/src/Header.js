import React from "react"
import "./style.css"
import logo from "./react-logo.png"


export default function Header() {
    return (
        <header>
            <nav className="nav">
                <img src={logo} className="nav-logo" alt="react logo"/>
                <ul className="nav-items">
                    <li>Pricing</li>
                    <li>About</li>
                    <li>Contact</li>
                </ul>
            </nav>
        </header>
    )
}


// otherwise:
// export default Header

