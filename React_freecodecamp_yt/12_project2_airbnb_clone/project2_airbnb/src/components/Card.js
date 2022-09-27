import React from "react"
import start_icon from "../images/star_icon.webp"


export default function Card(props) {
    let badgeText
    if (props.item.openSpots === 0) {
        badgeText = "SOLD OUT"
    } else if (props.item.location === "Online") {
        badgeText = "ONLINE"
    }

    return (
        <div className="card">
            {
                badgeText && 
                <div className="card--badge">{badgeText}</div>
            }
            <img 
                src={`./images/${props.item.coverImg}`} 
                className="card--image" alt={props.item.title} 
            />
            <div className="card--stats">
                <img src={start_icon} className="card--star" alt="star icon"/>
                <span>{props.item.stats.rating}</span>
                <span className="gray">({props.item.stats.reviewCount})・</span>
                <span className="gray">{props.item.location}</span>
            </div>
            <p className="card--title">{props.item.title}</p>
            <p className="card--price">
                <span className="bold">From ${props.item.price}</span> / person
                </p>
        </div>
    )
}