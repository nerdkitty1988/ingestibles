import React, { useState, useEffect } from "react";
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
            <NavLink to={`/api/recipes/${recipe.id}`} className="recipeNav">
			    <div key={recipe.id} className="singleRecipe">
                    <img className="recipePic" src={recipe.media ? recipe.media[0] : "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARMAAAC3CAMAAAAGjUrGAAAAKlBMVEXg4OD////j4+Pd3d36+vri4uLw8PDs7Oz29vb09PTa2tr5+fnm5ubx8fF4aKZkAAABUUlEQVR4nO3Z246CMBRAUWjBgQ78/+8OeMVR4E0TzlovJpUY3DnBglUFAAAAAAAAAAAAAAAAAAAAAAAAAMAh5DZtq/K3T/HTclfv6YNFyf1ukro+ffssPyvX9bg9BtMg/cYalKnJz06TU93EazK/tENa+eJRm+Rxump0K0cEbXI6X0q7t189aJN8/X1p3x4Ru8nwWO7uQxO0Sbk2eax2j51a0CbVcNma3UejW2xfozbJqZley22tW+7pozapcinleUruUcI2Wa4sbgrnKLGbpPPC033yFCV0k2ben/x/dNDnwE1yM2/aXp+mlMBN5iR18/qAKW6T85S8FbfJapKwTdanJHCT9SSaaDLT5NWlSWrXpMh7tpW3g97v9CkN61LqwjUZN64lNzv/AB1O2f+/eCz7H3MspeRtJVwSAAAAAAAAAAAAAAAAAAAAAAAAAICj+gOmbQmv8zyqjAAAAABJRU5ErkJggg=="} />
				    <h4 className="recipeTitle">{recipe.title}</h4>
				    <p className="authorName">by: {recipe.author.username} in {recipe.tags ? recipe.tags[0].name : "All Recipes"}</p>
			    </div>
            </NavLink>
		);
	});

	const createdRecipeBlock = createdRecipes.map((recipe) => {

		return (
            <NavLink to={`/api/recipes/${recipe.id}`} className="recipeNav">
			    <div key={recipe.id} className="singleRecipe">
                    <img className="recipePic" src={recipe.media ? recipe.media[0] : "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARMAAAC3CAMAAAAGjUrGAAAAKlBMVEXg4OD////j4+Pd3d36+vri4uLw8PDs7Oz29vb09PTa2tr5+fnm5ubx8fF4aKZkAAABUUlEQVR4nO3Z246CMBRAUWjBgQ78/+8OeMVR4E0TzlovJpUY3DnBglUFAAAAAAAAAAAAAAAAAAAAAAAAAMAh5DZtq/K3T/HTclfv6YNFyf1ukro+ffssPyvX9bg9BtMg/cYalKnJz06TU93EazK/tENa+eJRm+Rxump0K0cEbXI6X0q7t189aJN8/X1p3x4Ru8nwWO7uQxO0Sbk2eax2j51a0CbVcNma3UejW2xfozbJqZley22tW+7pozapcinleUruUcI2Wa4sbgrnKLGbpPPC033yFCV0k2ben/x/dNDnwE1yM2/aXp+mlMBN5iR18/qAKW6T85S8FbfJapKwTdanJHCT9SSaaDLT5NWlSWrXpMh7tpW3g97v9CkN61LqwjUZN64lNzv/AB1O2f+/eCz7H3MspeRtJVwSAAAAAAAAAAAAAAAAAAAAAAAAAICj+gOmbQmv8zyqjAAAAABJRU5ErkJggg=="} />
				    <h4 className="recipeTitle">{recipe.title}</h4>
				    <p className="authorName">by: {recipe.author.username} in {recipe.tags ? recipe.tags[0].name : "All Recipes"}</p>
			    </div>
            </NavLink>
		);
	});

	return (
		<>
            <div className="plateTop">
                <div className="plateTopCard">
                    <img src={sessionUser.profilePic} className="profileCircle"/>
                    <div className="profCard">
                        <h2>{sessionUser.username}</h2>
                        <div className="buttonDiv">
                            <NavLink to={`/${sessionUser.id}/profile`} className="profButton">View Profile</NavLink>
                            <NavLink to={`/${sessionUser.id}/profile/edit`} className="profButton">Edit Profile</NavLink>
                        </div>
                        <h5>Joined {sessionUser.createdAt}</h5>
                    </div>
                </div>
            </div>
			<div className="recipeBlock">
				<h1 className="plateHeadings">YOUR RECIPES </h1>
				<ul className="recipeList">{createdRecipeBlock}</ul>
			</div>
			<div className="recipeBlock">
				<h1 className="plateHeadings">RECIPES YOU LIKE </h1>
				<ul className="recipeList">{likedRecipeBlock}</ul>
			</div>
		</>
	);
}

export default MyPlate;
