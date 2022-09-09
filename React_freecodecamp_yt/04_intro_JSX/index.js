const h1 = document.createElement("h1")
h1.textContent = "Hello world"
h1.className = "header"
console.log(h1)

// <h1 class="header">

const element = <h1 className="header">This is JSX</h1>
console.log(element)

/*   React turns a JS object:
{
    type: "h1",
    key: null,
    ref: null,
    props: {
        className: "header", 
        children: "This is JSX"
    },
    _owner: null,
    _store: {}
}
*/

// JSX (JavaScript XML), a sort of flavour of JS that looks a lot like HTML
ReactDOM.render(element, document.getElementById("root1"))


const page = (
    <div>
        <h1 className="header">This is also JSX</h1>
        <p>This is a paragraph</p>
    </div>
)

ReactDOM.render(
    page,
    document.getElementById("root2")
)


// Challenge: Create a navbarin JSX

const navbar = (
    <nav>
        <h1>Bob's Bistro</h1>
        <ul>
            <li>Menu</li>
            <li>About</li>
            <li>Contact</li>
        </ul>
    </nav>    
)

ReactDOM.render(navbar, document.getElementById("root3"))