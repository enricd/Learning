import React from "react"
import "./style.css"


export default function Header() {
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


// otherwise:
// export default Header