import React, { useState, useEffect } from "react";
import { NavLink } from "react-router-dom";
import "./Recipes.css";

const Recipes = () => {
	const [allRecipes, setAllRecipes] = useState([]);
	const [recentRecipes, setRecentRecipes] = useState([]);
	const [previousRecipes, setPreviousRecipes] = useState([]);
	const [allLikes, setAllLikes] = useState([]);

	useEffect(() => {
		async function recipes() {
			const response = await fetch("/api/recipes");
			const responseData = await response.json();
			setAllRecipes(responseData);
		}

		async function recent_recipes() {
			const response = await fetch("/api/recipes/recent");
			const responseData = await response.json();
			setRecentRecipes(responseData);
		}

		// remember to exclude the first 5 from this array
		async function previous_recipes() {
			const response = await fetch("/api/recipes/previous");
			const responseData = await response.json();
			setPreviousRecipes(responseData);
		}

		async function all_likes() {
			const response = await fetch("/api/likes");
			const responseData = await response.json();
			setAllLikes(responseData);
		}

		recipes();
		recent_recipes();
		previous_recipes();
		all_likes();
	}, []);

	const recRecipes = recentRecipes?.recent;
	const prevRecipes = previousRecipes?.previous?.slice(5);

	const allLikesArr = allLikes?.likes;

	function counter(rec) {
		let count = 0;

		allLikesArr?.forEach((ele) => {
			if (ele?.recipeId == rec?.id) {
				count++;
			}
		});
		return count;
	}

	if (recRecipes) {
		console.log(recRecipes[0]?.medias[0]?.mediaUrl);
	}
	return (
		<main>
			<div className="home-wrapper-wrapper full-wrapper home-content clearfix">
				<div
					id="kitchen"
					className="home-content-rotator carousel carousel-fade"
				>
					<div className="home-content-rotator-slide-overlay">
						<div className="home-content-rotator-slide-wrap">
							<div className="home-content-adspot-wrap">
								<div
									style={{
										color: "#2196F2",
										textAlign: "center",
										width: "0px",
										margin: "0%",
									}}
									className="home-content-adspot-text"
								>
									<h1
										style={{
											color: "orange",
											lineHeight: "90px",
											fontSize: "100px",
										}}
									>
										Try
									</h1>
									<h1
										style={{
											color: "white",
											lineHeight: "90px",
											fontSize: "100px",
										}}
									>
										Something
									</h1>
									<h1
										style={{
											color: "#eee",
											lineHeight: "90px",
											fontSize: "100px",
										}}
									>
										New
									</h1>
								</div>
							</div>
						</div>
					</div>
				</div>

				<hr />

				<div className="home-content-explore">
					<div className="home-content-explore-wrap">
						<h2>Recipes</h2>
						<div
							className={`home-content-explore-category home-content-explore-category-recent clearfix`}
						>
							<NavLink
								to={"/recipes"}
								className="home-content-explore-link"
							>
								<h3>
									<span className="anchor-text">
										Most Recent
									</span>
									&nbsp;
									<i className="fas fa-angle-right fa-2x"></i>
								</h3>
							</NavLink>
							<div className="home-content-explore-category-wrap ">
								<div id="recentRecipes">
									{recRecipes?.map((recRecipe) => (
										<div className="home-content-explore-ible">
											<NavLink
												to={`/recipes/${recRecipe?.id}`}
											>
												<img
													className=" ls-is-cached lazyloaded"
													data-src={
														recRecipe?.medias[0]
															?.mediaUrl
													}
													src={
														recRecipe?.medias[0]
															?.mediaUrl
													}
													alt={recRecipe?.title}
												/>
												<noscript>
													<img
														src={
															recRecipe?.medias[0]
														}
														alt={recRecipe?.title}
													/>
												</noscript>
											</NavLink>
											<div className="home-content-explore-ible-info">
												<strong>
													<NavLink
														className="ible-title"
														to={`/recipes/${recRecipe?.id}`}
													>
														{recRecipe?.title}
													</NavLink>
												</strong>
												<span className="ible-author">
													&nbsp;by&nbsp;
													<NavLink
														to={`/users/${recRecipe?.author?.id}`}
													>
														{
															recRecipe?.author
																?.username
														}
													</NavLink>
												</span>
												<span className="ible-channel">
													&nbsp;in&nbsp;
													<NavLink
														to={`/recipes/${recRecipe?.tags[0]?.name?.toLowerCase()}`}
													>
														{recRecipe?.tags[0]?.name?.toLowerCase()}
													</NavLink>
												</span>
												<p className="ible-channel">
													Created on&nbsp;
													<span>
														{new Date(
															recRecipe?.time_created
														).toLocaleDateString()}
													</span>
												</p>
											</div>
											<div className="ible-stats">
												<span className="ible-stats-right-col">
													<span className="ible-favorites">
														<i
															className="fas fa-heart"
															title="Favorites Count"
														></i>
														&nbsp;&nbsp;
														{allLikesArr
															? counter(recRecipe)
															: ""}
														&nbsp;
													</span>
												</span>
											</div>
										</div>
									))}
								</div>
							</div>
						</div>

						<div>
							<NavLink
								to={"/recipes"}
								className="home-content-explore-link"
							>
								<h3>
									<span className="anchor-text">
										Previous
									</span>
									&nbsp;
									<i className="fas fa-angle-right fa-2x"></i>
								</h3>
							</NavLink>
							<div>
								<div id="recentRecipes">
									{prevRecipes?.map((prevRecipe) => (
										<div className="home-content-explore-ible">
											<NavLink
												to={`/recipes/${prevRecipe?.id}`}
											>
												<img
													className=" ls-is-cached lazyloaded"
													data-src={
														prevRecipes[0]
															?.medias[0]
															?.mediaUrl
													}
													src={
														prevRecipes[0]
															?.medias[0]
															?.mediaUrl
													}
													alt={prevRecipe?.title}
												/>
												<noscript>
													<img
														src={`/recipes/${prevRecipe?.medias[0]}`}
														alt={prevRecipe?.title}
													/>
												</noscript>
											</NavLink>
											<div className="home-content-explore-ible-info">
												<strong>
													<NavLink
														className="ible-title"
														to={`/recipes/${prevRecipe?.id}`}
													>
														{prevRecipe?.title}
													</NavLink>
												</strong>
												<span className="ible-author">
													&nbsp;by&nbsp;
													<NavLink
														to={`/users/${prevRecipe?.author?.id}`}
													>
														{
															prevRecipe?.author
																?.username
														}
													</NavLink>
												</span>
												<span className="ible-channel">
													&nbsp;in&nbsp;
													<NavLink
														to={`/recipes/${prevRecipe?.tags[0]?.name?.toLowerCase()}`}
													>
														{prevRecipe?.tags[0]?.name?.toLowerCase()}
													</NavLink>
												</span>
												<p className="ible-channel">
													Created on&nbsp;
													<span>
														{new Date(
															prevRecipe?.time_created
														).toLocaleDateString()}
													</span>
												</p>
											</div>
											<div className="ible-stats">
												<span className="ible-stats-right-col">
													<span className="ible-favorites">
														<i
															className="fas fa-heart"
															title="Favorites Count"
														></i>
														&nbsp;&nbsp;
														{allLikesArr
															? counter(
																	prevRecipe
															  )
															: ""}
														&nbsp;
													</span>
												</span>
											</div>
										</div>
									))}
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</main>
	);
};

export default Recipes;
