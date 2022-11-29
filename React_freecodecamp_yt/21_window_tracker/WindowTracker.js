import React from "react"

export default function WindowTracker() {

    const [windowWidth, setWidnowWidth] = React.useState(window.innerWidth)

    React.useEffect(() => {
        function watchWidth() {
            setWidnowWidth(window.innerWidth)
        }

        window.addEventListener("resize", watchWidth)

        // clean up function, prevent memory leaks
        return function() {
            window.removeEventListener("resize", watchWidth)
        }
    }, [])

    return (
        <h1>Window width: {windowWidth}</h1>
    )
}