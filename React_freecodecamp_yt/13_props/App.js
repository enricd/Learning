import React from "react"
import Contact from "./Contact"

function App() {
    return (
        <div className="contacts">
            <Contact 
                img=".images/mr-whiskerson.png"
                name="Mr. Whiskerson" 
                phone="(212) 555-1234"
                email="mr.whiskaz@catnap.meow"
            />
            <Contact 
                img=".images/fluffykins.png"
                name="Fluffykins" 
                phone="(212) 555-2674"
                email="fluffy@catnap.meow"
            />
            <Contact 
                img=".images/felix.png"
                name="Felix" 
                phone="(212) 444-1234"
                email="felix@catnap.meow"
            />
            <Contact 
                img=".images/pumpkin.png"
                name="Pumpkin" 
                phone="(212) 456-7234"
                email="pumpkin@catnap.meow"
            />
        </div>
    )
}


// QUIZ 

// props make components reusable
// you pass props to a component as they were attributes in a html element
// we cannot pass custom props to native DOM elements as they don't exist
// the components receives props as an object (commonly called props) and extracts them as props.x, props.y, props.whatever...