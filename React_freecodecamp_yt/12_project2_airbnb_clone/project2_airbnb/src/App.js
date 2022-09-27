import React from "react"
import "./style.css"
import Navbar from "./components/Navbar"
import Hero from "./components/Hero"
import Card from "./components/Card"
import data from "./data"


export default function App() {

    const cards = data.map(item => {
        return (
            <Card
                key={item.id}
                item={item}
                //{...item}   // spread syntax
            />

            // <Card 
            //     key={item.id}
            //     img={item.coverImg}
            //     rating={item.stats.rating}
            //     reviewCount={item.stats.reviewCount}
            //     location={item.location}
            //     title={item.title}
            //     price={item.price}
            //     openSpots={item.openSpots}
            // />
        )
    })

    return (
        <div>
            <Navbar />
            <Hero />
            <section className="cards-list">
                {cards}
            </section>
        </div>
    )
}