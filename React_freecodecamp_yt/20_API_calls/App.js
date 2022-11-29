import React from "react"

export default function App() {
    const [starWarsData, setStarWarsData] = React.useState({})
    const [count, setCount] = React.useState(1)

    // Side effects 
    // (anything that React isn't in charge of eg: localStorage, APIs, web sockets, syncing)
    React.useEffect(() => {
        // 1. GET the data (fetch)
        // 2. Save the data to state
        fetch(`https://swapi.dev/api/people/${count}`)
            .then(res => res.json())
            .then(data => setStarWarsData(data))
    }, [count])

    return (
        <div>
            <h2>The count in {count}</h2>
            <button onClick={() => setCount(prevCount => prevCount + 1)}>Get Next Character</button>
            <pre>{JSON.stringify(starWarsData, null, 2)}</pre>
        </div>
    )
}



// QUIZ

// 1. A side effect is any code you want to run that React is not in charge to handle

// 2. Anythin that React is in charge of, is not a side effect

// 3. Reacrt run the useEffect function as soon as the component loads (firs render).
//    On every re-render of the component (assuming no dependencies array).
//    Will NOT run the effect when the values in the dependencies in the array stay 
//    the same between renders.

// 4. The dependencies array is the second parameter to the useEffect function and 
//    it's a way for React to know wether it should re-run the effect function.