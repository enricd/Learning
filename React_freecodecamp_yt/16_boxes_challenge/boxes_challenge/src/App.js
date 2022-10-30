import React from "react"
import "./style.css"
import boxes from "./boxes"
import Box from "./components/Box"

export default function App(props) {
    const [squares, setSquares] = React.useState(boxes)

    function toggle(id) {
        setSquares(prevSquares => {
            return prevSquares.map((square) => {
                return square.id === id ? {...square, on: !square.on} : square
            })
        })
    }

    const squareElements = squares.map(square => (
        <Box
            key={square.id}
            on={square.on} 
            handleClick={() => toggle(square.id)}
        />
    ))

    return (
        <main>
            {squareElements}
        </main>
    )
}