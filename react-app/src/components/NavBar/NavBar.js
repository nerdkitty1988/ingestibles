import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./NavBar.css";

const NavBar = ({ loaded }) => {
	const sessionUser = useSelector((state) => state.session?.user);

	const [searchTerm, setSearchTerm] = useState("");
	const [recipes, setRecipes] = useState();

	useEffect(() => {
        if(searchTerm){
            async function fetchData() {
                const response = await fetch(`/api/search/${searchTerm}`);
                const responseData = await response.json();
                console.log("!!!!", responseData);
                setRecipes(responseData.recipes);
            }
            fetchData();
        }
	}, [searchTerm]);

	let searchBlock;

	if (recipes) {
        console.log(recipes)
		searchBlock = recipes.map((recipe) => {
			return (
				<a href={`/recipes/${recipe.id}`} className="recipeNav">
					<div key={`liked'_${recipe.id}`} className="singleRecipe">
						<img
							alt={recipe.name}
							className="recipePic"
							src={
								recipe.medias && recipe.medias[0]
									? recipe.medias[0]['mediaUrl']
									: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARMAAAC3CAMAAAAGjUrGAAAAKlBMVEXg4OD////j4+Pd3d36+vri4uLw8PDs7Oz29vb09PTa2tr5+fnm5ubx8fF4aKZkAAABUUlEQVR4nO3Z246CMBRAUWjBgQ78/+8OeMVR4E0TzlovJpUY3DnBglUFAAAAAAAAAAAAAAAAAAAAAAAAAMAh5DZtq/K3T/HTclfv6YNFyf1ukro+ffssPyvX9bg9BtMg/cYalKnJz06TU93EazK/tENa+eJRm+Rxump0K0cEbXI6X0q7t189aJN8/X1p3x4Ru8nwWO7uQxO0Sbk2eax2j51a0CbVcNma3UejW2xfozbJqZley22tW+7pozapcinleUruUcI2Wa4sbgrnKLGbpPPC033yFCV0k2ben/x/dNDnwE1yM2/aXp+mlMBN5iR18/qAKW6T85S8FbfJapKwTdanJHCT9SSaaDLT5NWlSWrXpMh7tpW3g97v9CkN61LqwjUZN64lNzv/AB1O2f+/eCz7H3MspeRtJVwSAAAAAAAAAAAAAAAAAAAAAAAAAICj+gOmbQmv8zyqjAAAAABJRU5ErkJggg=="
							}
						/>
						<h4 className="recipeTitle">
							{recipe.title.slice(0, 25) + "..."}
						</h4>
						<p className="authorName">
							by: {recipe.author.username} in{" "}
							{recipe.tags ? recipe.tags[0].name : "All Recipes"}
						</p>
					</div>
				</a>
			);
		});
	}

	let sessionLinks;
	if (sessionUser) {
		sessionLinks = <ProfileButton user={sessionUser} />;
	} else {
		sessionLinks = (
			<div id="you-menu-container" className="right-col">
				<div id="login-menu">
					<NavLink
						id="login"
						to="/login"
						exact={true}
						activeClassName="active"
					>
						Log In
					</NavLink>
					<span className="pipe">|</span>
					<NavLink
						id="sign-up"
						to="/sign-up"
						exact={true}
						activeClassName="active"
					>
						Sign Up
					</NavLink>
				</div>
			</div>
		);
	}

	return (
		<header id="site-header" className="site-header">
			<div className="site-header-top">
				<div className="left-col">
					<nav
						className="site-header-nav site-header-primary-nav"
						aria-label="Categories menu"
					>
						<ul className="category-nav-link">
							<li>
								<a href="/">
									<i className="fas fa-home"></i>
								</a>
							</li>
							<li>
								<a href="/recipes/beef">Beef</a>
							</li>
							<li>
								<a href="/recipes/chicken">Chicken</a>
							</li>
							<li>
								<a href="/recipes/desserts">Desserts</a>
							</li>
							<li>
								<a href="/recipes/fish">Fish</a>
							</li>
							<li>
								<a href="/recipes/pasta">Pasta</a>
							</li>
							<li>
								<a href="/recipes/pastries">Pastries</a>
							</li>
							<li>
								<a href="/recipes/vegetarian">Vegetarian</a>
							</li>
						</ul>
					</nav>
				</div>
				{loaded && sessionLinks}
			</div>
			<div className="site-header-bottom">
				<div className="left-col">
					<a className="site-logo " href="/">
						<img
							className="ingestibles-logo"
							alt="Ingestibles"
							src="/logo.png"
						/>
						<span id="site-header-category-brand">ingestibles</span>
						<span className="site-header-category category-"></span>
					</a>
					<a href="/recipes" className="btn btn-category-header">
						Recipes
					</a>
					<a
						href="/recipes/my_plate"
						className="btn btn-category-header"
					>
						My Plate
					</a>
				</div>
				<div className="right-col">
					<nav
						className="site-header-nav site-header-secondary-nav"
						aria-label="Contest and classes"
					>
						<ul>
							<li>
								<a
									id="site-header-secondary-link"
									href="/recipes/new_recipe"
								>
									PUBLISH
								</a>
							</li>
						</ul>
					</nav>
					<form
						id="header-search-form"
						className="site-search-form"
						title="Search Form"
					>
						<label className="sr-only">Enter search term</label>
						<input
							className="input-medium site-search-input"
							id="site-search-input"
							type="text"
							placeholder="Let's Make..."
							onChange={(e) => setSearchTerm(e.target.value)}
						/>
						<button className="submit-btn" type="button">
							<i className="fas fa-search fa-sm fa-flip-horizontal"></i>
						</button>
					</form>
				</div>
			</div>
			{searchTerm ? (
				<div className="searchReultsContainer">
					<h1 className="plateHeadings">Search reults for: </h1>
					<h2 className="searchTerm">{searchTerm}</h2>
					<ul className="searchedRecipes">{searchBlock}</ul>
				</div>
			) : null}
		</header>
	);
};

export default NavBar;
