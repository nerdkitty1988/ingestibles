import React, { useState, useEffect } from 'react';
import { useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import "./MyPlate.css";

function MyPlate() {
    const [createdRecipes, setCreatedRecipes] = useState([]);
    const [likedRecipes, setLikedRecipes] = useState([]);

    const sessionUser = useSelector((state) => state.session.user);
    const userId = sessionUser.id;

    useEffect(() => {
        async function fetchData() {
            const response = await fetch(`/api/recipes/my_plate/${userId}`);
            const responseData = await response.json();
            setCreatedRecipes(responseData.created);
            setLikedRecipes(responseData.liked);
        }
        fetchData();
    }, [userId]);

    const likedRecipeBlock = likedRecipes.map((recipe) => {
        return (
            <li key={recipe.id}>
                <NavLink to={`/api/recipes/${recipe.id}`}>{recipe.title}</NavLink>
            </li>
        );
    });

    const createdRecipeBlock = createdRecipes.map((recipe) => {
        return (
            <li key={recipe.id}>
                <NavLink to={`/api/recipes/${recipe.id}`}>{recipe.title}</NavLink>
            </li>
        );
    });

    return (
        <>
            <h1>User Recipes: </h1>
            <ul>{createdRecipeBlock}</ul>
            <h1>Liked Recipes: </h1>
            <ul>{likedRecipeBlock}</ul>
        </>
    );

}

export default MyPlate;
