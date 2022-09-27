import React from "react"
import photo_grid from "../images/images_grid.png"


export default function Hero() {
    return (
        <section className="hero">
            <img src={photo_grid} className="hero--photo" alt="hero img grid" />
            <h1 className="hero--header">Online Experiences</h1>
            <p className="hero--text">Join unique interactive activites led by
            one-of-a-kind hosts-all without leaving home.</p>
        </section>
    )
}