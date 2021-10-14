import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import "./Recipes.css";


const Recipes = () => {
	const [allRecipes, setAllRecipes] = useState([]);

	const sessionUser = useSelector((state) => state.session?.user);

	useEffect(() => {
		async function recipes() {
			const response = await fetch('/api/recipes');
			const responseData = await response.json();
			setAllRecipes(responseData);
		}
		recipes();
	}, []);

  console.log(allRecipes?.recipes)


  return (
    <h1>Hello World</h1>
  )






};

export default Recipes;
