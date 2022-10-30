import React from "react";
import ReactDOM from "react-dom";

function App() {
    const [things, setThings] = React.useState(["Thing 1", "Thing 2"])

    function addItem() {
        const newThingText = `Thing ${things.length + 1}`
        setThings(prevState => [...prevState, newThingText])
    }

    const thingsElements = things.map(thing => <p key={thing}>{thing}</p>)

    return (
        <div>
            <button onClick={addItem}>Add Item</button>
            {thingsElements}
        </div>
    )
}

ReactDOM.render(<App />, document.getElementById("root"))



// challenge

function greeting(name) {
    const date = new Date()
    const hours = date.getHours()
    
    let timeOfDay
    if(hours >= 4 && hours < 12) {
        timeOfDay = "morning"
    } else if(hours >= 12 && hours < 17) {
        timeOfDay = "afternoon"
    } else if(hours >= 17 && hours < 20) {
        timeOfDay = "evening"
    } else {
        timeOfDay = "night"
    }

    return `Good ${timeOfDay}, ${name}!`
}

console.log(greeting("Bob"))


// Quiz

// The concept of "state" is "the current way of how things are". It's a way for React
// to remember saved values from within a component.

// You would want to use props instead of state every time you want to pass data to a 
// component so that component can determine what will get displayed on the screen.

// You would want to use state instead of props anytime you want a component to maintain
// some values from within a component, and remember those values even when React re-renders
// the component.

// Immutable means unchanging, like props in a component, they shouldn't change inside a
// component. State is mutable.



// State example 3

export default function App2() {
    const [isImportant, setIsImportant] = React.useState("Yes")

    function handleClick() {
        setIsImportant("No")
    }

    return(
        <div className="state">
            <h1 className="state--title">Is state important to know?</h1>
            <div className="state--value" onClick={handleClick}>
                <h1>{isImportant}</h1>
            </div>
        </div>
    )
}



// State example 4

export default function App3() {

    const [count, setCount] = React.useState(0)

    function add() {
        // setCount(count + 1)
        // it's better to use callback function:
        setCount(prevCount => prevCount + 1)
    }

    function subtract() {
        setCount(prevCount => prevCount - 1)
    }

    return (
        <div className="counter">
            <button className="counter--minus" onClick={subtract}>-</button>
            <div className="counter--count">
                <h1>{count}</h1>
            </div>
            <button className="counter--plus" onClick={add}>+</button>
        </div>
    )
}


// Quiz

// You can pass 2 options to a state setter function (setCount), a new value of state
// or a Callback function that returns the new value for the state

// You can use the first option when you don't care about the previous state to 
// generate the new one

// The second is used when you need the previous state to calculate the new one



// state example 5

function App4() {
    const [thingsArray, setThingsArray] = React.useState(["Thing 1", "Thing 2"])

    function addItem() {
        setThingsArray(prevState => {
            return [...prevState, `Thing ${prevState.length + 1}`]
        })
    }

    const thingsElements = thingsArray.map(thing => <p key={thing}>{thing}</p>)

    return(
        <div>
            <button onClick={addItem}>Add Item</button>
            {thingsElements}
        </div>
    )

}



// state example 6

function Star(props) {
    const starIcon = props.isFilled ? "star-filled.png" : "star-empty.png"
    return (
        <img 
            src={`../images/${starIcon}`}
            className="card--favorite"
            onClick={props.handleClick}
        />
    )
}


export default function App5() {
    const [contact, setContact] = React.useState({
        firstName: "John",
        lastName: "Doe",
        phone: "+1 (719) 555-1212",
        email: "itsmyrealname@example.com",
        isFavorite: false
    })

    function toggleFavorite() {
        setContact(prevContact => ({
                ...prevContact,
                isFavorite: !prevContact.isFavorite
        }))
    }

    return (
        <main>
            <article className="card">
                <img src="./images/user.png" className="card--image" />
                <div className="card--info">
                    <Star isFilled={contact.isFavorite} handleClick={toggleFavorite} />
                    <h2 className="card--name">
                        {contact.firstName} {contact.lastName}
                    </h2>
                    <p className="card--contact">{contact.phone}</p>
                    <p className="card--contact">{contact.email}</p>
                </div>
            </article>
        </main>
    )
}

