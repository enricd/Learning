import React from "react"

export default function Joke(props) {

    const [isShown, setIsShown] = React.useState(false)

    function toggle() {
        setIsShown(prevIsShown => !prevIsShown)
    }

    return (
        <div>
            {props.setup && <h3>{props.setup}</h3>}
            {isShown && <p>{props.punchline}</p>}
            <button onClick={toggle}>{isShown ? "Hide" : "Show"} Punchline</button>
            <hr />
        </div>
    )
}