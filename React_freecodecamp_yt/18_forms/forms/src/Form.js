import React from "react"
import "./styles.css"

export default function Form() {
    const [formData, setFormData] = React.useState(
        {
            firstName: "", 
            lastName: "", 
            email: "", 
            comments: "",
            isFriendly: true,
            employment: "",
            favColor: ""
        }
    )

    function handleChange(event) {
        const {name, value, type, checked} = event.target
        setFormData(prevFormData => {
            return {
                ...prevFormData,
                [name]: type === "checkbox" ? checked : value
            }
        })
    }

    function handleSubmit(event) {
        event.preventDefault()
        // submitToApi(formData)
        console.log(formData)
    }


    return (
        <form onSubmit={handleSubmit}>
            <input
                type="email"
                placeholder="Email"
                onChange={handleChange}
                name="email"
                value={formData.email}
            />
            <input
                type="password"
                placeholder="Password"
                onChange={handleChange}
                name="password"
                value={formData.password}
            />
            <input
                type="password"
                placeholder="Confirm password"
                onChange={handleChange}
                name="confirmPassword"
                value={formData.confirmPassword}
            />
            <input
                type="checkbox"
                id="isNewsletter"
                checked={formData.isNewsletter}
                onChange={handleChange}
                name="isNewsletterly"
            />
            <label htmlFor="isNewsletter">I want to join the newsletter</label>
            <br />
            <br />

            <button>Sign up</button>
        </form>
    )    
}



// QUIZ

// 1. In a vanilla JS app, the data from a form is gathered right before the form
// is submitted.

// 2. In a React app we don't allow the form elements to mantain thei own internal
// state but instead the component that houses the entire form has some React state
// that is updated at every change of the form, as it is being filled out.

// 3. The "name" attribute of a form element should match the property name being
// held in state for that input.

// 4. In checkbox we look for the checked property to be the same value as the 
// value property of the specific checkbox element.

// 5. In order to trigger a form submit, with a button click in the form you
// trigger the onSubmit handler funciton.