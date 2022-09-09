// ReactDOM.render(<h1 className="header">Hello, React!</h1>, document.getElementById("root"))

const h1 = document.createElement("h1")
h1.textContent = "This is an imperative way to program"
h1.className = "header"
document.getElementById("root").append(h1)