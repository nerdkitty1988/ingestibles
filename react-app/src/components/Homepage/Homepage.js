import React, { useState, useEffect } from "react";
import { NavLink } from "react-router-dom";
import "./Homepage.css";

const Homepage = () => {
	const [cakeRecipes, setCakeRecipes] = useState([]);
	const [candyRecipes, setCandyRecipes] = useState([]);
	const [pastaRecipes, setPastaRecipes] = useState([]);
	const [saladRecipes, setSaladRecipes] = useState([]);

	useEffect(() => {
		const cake = async () => {
			const res = await fetch("/api/recipes/CAKE");
			const resData = await res.json();
			setCakeRecipes(resData.tagged);
		};

		const candy = async () => {
			const res = await fetch("/api/recipes/CANDY");
			const resData = await res.json();
			setCandyRecipes(resData.tagged);
		};

		const pasta = async () => {
			const res = await fetch("/api/recipes/PASTA");
			const resData = await res.json();
			setPastaRecipes(resData.tagged);
		};

		const salad = async () => {
			const res = await fetch("/api/recipes/SALAD");
			const resData = await res.json();
			setSaladRecipes(resData.tagged);
		};

		cake();
		candy();
		pasta();
		salad();
	}, []);


	return (
		<main>
			<div
				id="home-container"
				className="home-wrapper-wrapper full-wrapper home-content clearfix"
			>
				<div
					id="site-announcements-page"
					className="site-announcements-page"
				>
					<div className="site-announcements-page-content"></div>
				</div>
				<div
					id="home-content-rotator"
					className="home-content-rotator carousel carousel-fade"
				>
					<div className="home-content-rotator-inner carousel-inner">
						<div
							className="home-content-rotator-slide item home-content-rotator-slide-align-middle"
							data-link="https://www.instructables.com/halloween/"
							style={{
								backgroundImage:
									"url(https://images.unsplash.com/photo-1504674900247-0877df9cc836?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2340&q=80)",
							}}
						>
							<div className="home-content-rotator-slide-overlay" />
							<div className="home-content-rotator-slide-wrap">
								<div className="home-content-adspot-wrap">
									<div className="home-content-adspot-text">
										<h1>YOURS FOR THE MAKING</h1>
										<p>
											Ingestibles is a community for
											people who like to cook food. Come
											explore, share, and create your next
											recipe with us!
										</p>
									</div>
								</div>
							</div>
						</div>

						<div
							className="home-content-rotator-slide item  home-content-rotator-slide-align-middle"
							data-link="https://www.instructables.com/halloween/"
							style={{
								backgroundImage:
									"url(https://images.unsplash.com/photo-1605433247501-698725862cea?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1470&q=80)",
							}}
						>
							<div className="home-content-rotator-slide-overlay" />
							<div className="home-content-rotator-slide-wrap">
								<div className="home-content-adspot-wrap">
									<div className="home-content-adspot-text">
										<h1>YOURS FOR THE MAKING</h1>
										<p>
											Ingestibles is a community for
											people who like to food. Come
											explore, share, and create your next
											recipe with us!
										</p>
									</div>
								</div>
							</div>
						</div>

						<div
							className="home-content-rotator-slide item  home-content-rotator-slide-align-middle"
							data-link="https://www.instructables.com/halloween/"
							style={{
								backgroundImage:
									"url(https://images.unsplash.com/photo-1455619452474-d2be8b1e70cd?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1470&q=80)",
							}}
						>
							<div className="home-content-rotator-slide-overlay" />
							<div className="home-content-rotator-slide-wrap">
								<div className="home-content-adspot-wrap">
									<div className="home-content-adspot-text">
										<h1>YOURS FOR THE MAKING</h1>
										<p>
											Ingestibles is a community for
											people who like to food. Come
											explore, share, and create your next
											recipe with us!
										</p>
									</div>
								</div>
							</div>
						</div>

						<div
							className="home-content-rotator-slide item  home-content-rotator-slide-align-middle"
							data-link="https://www.instructables.com/halloween/"
							style={{
								backgroundImage:
									"url(https://images.unsplash.com/photo-1607198179219-cd8b835fdda7?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1469&q=80)",
							}}
						>
							<div className="home-content-rotator-slide-overlay" />
							<div className="home-content-rotator-slide-wrap">
								<div className="home-content-adspot-wrap">
									<div className="home-content-adspot-text">
										<h1>YOURS FOR THE MAKING</h1>
										<p>
											Ingestibles is a community for
											people who like to food. Come
											explore, share, and create your next
											recipe with us!
										</p>
									</div>
								</div>
							</div>
						</div>

						<div
							className="home-content-rotator-slide item  home-content-rotator-slide-align-middle"
							data-link="https://www.instructables.com/halloween/"
							style={{
								backgroundImage:
									"url(https://images.unsplash.com/photo-1498654896293-37aacf113fd9?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1470&q=80)",
							}}
						>
							<div className="home-content-rotator-slide-overlay" />
							<div className="home-content-rotator-slide-wrap">
								<div className="home-content-adspot-wrap">
									<div className="home-content-adspot-text">
										<h1>YOURS FOR THE MAKING</h1>
										<p>
											Ingestibles is a community for
											people who like to food. Come
											explore, share, and create your next
											recipe with us!
										</p>
									</div>
								</div>
							</div>
						</div>

						<div
							className="home-content-rotator-slide item  home-content-rotator-slide-align-middle active"
							data-link="https://www.instructables.com/halloween/"
							style={{
								backgroundImage:
									"url(https://images.unsplash.com/photo-1540432797114-187727adf19b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2274&q=80",
							}}
						>
							<div className="home-content-rotator-slide-overlay" />
							<div className="home-content-rotator-slide-wrap">
								<div className="home-content-adspot-wrap">
									<div className="home-content-adspot-text">
										<h1>YOURS FOR THE MAKING</h1>
										<p>
											Ingestibles is a community for
											people who like to food. Come
											explore, share, and create your next
											recipe with us!
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div className="home-content-rotator-indicator-wrap">
						<ol className="home-content-rotator-indicator carousel-indicators">
							<li
								data-target="#home-content-rotator"
								data-slide-to="0"
								className=""
							></li>
							<li
								data-target="#home-content-rotator"
								data-slide-to="1"
								className=""
							></li>
							<li
								data-target="#home-content-rotator"
								data-slide-to="2"
								className=""
							></li>
							<li
								data-target="#home-content-rotator"
								data-slide-to="3"
								className=""
							></li>
							<li
								data-target="#home-content-rotator"
								data-slide-to="4"
								className=""
							></li>
							<li
								data-target="#home-content-rotator"
								data-slide-to="5"
								className=""
							></li>
						</ol>
					</div>
				</div>
				<div className="home-content-text">
					<div className="home-content-text-wrap">
						<div className="home-content-text-box">
							<h2>Step-by-step</h2>
							<p>
								We make it easy to learn how to cook anything,
								one step at a time. From the stovetop to the
								dinner table, you are sure to be inspired by the
								awesome creations that are shared everyday.
							</p>
						</div>
						<div className="home-content-text-box">
							<h2>Made By You</h2>
							<p>
								Ingestibles are created by you. No matter who
								you are, we all have secret cooking skills to
								share. Come join our community of curious
								makers, innovators, teachers, and life long
								learners who love to share what they make.
							</p>
						</div>
						<div className="home-content-text-box">
							<h2>A Happy Place</h2>
							<p>
								Making things makes people happy. We can't prove
								it, but we know it to be true. Find your happy
								place, and join one of the friendliest online
								communities anywhere.
							</p>
						</div>
					</div>
				</div>
				<hr />

				<div className="home-content-explore">
					<div className="home-content-explore-wrap">
						<h2>Explore Recipes</h2>
						<div className="home-content-explore-category home-content-explore-category-cake clearfix">
							<a
								href="/recipes/cake"
								className="home-content-explore-link"
							>
								<h3>
									<span className="anchor-text">Cake</span>
									&nbsp;
									<i className="fas fa-angle-right fa-2x"></i>
								</h3>
							</a>
							<div className="home-content-explore-category-wrap ">
								<div className="home-content-explore-ibles">
									{cakeRecipes?.map((cakeRecipe) => (
										<div className="home-content-explore-ible">
											<a
												href={`/recipes/${cakeRecipe?.id}`}
											>
												{/* ////////////after seeding media, copy data-src and paste into src below for each category!!!!//////////// */}
												<img
													className=" ls-is-cached lazyloaded"
													data-src={
														cakeRecipe?.medias[0]
													}
													src="https://images.unsplash.com/photo-1588195538326-c5b1e9f80a1b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2250&q=80"
													alt={cakeRecipe?.title}
												/>
												<noscript>
													<img
														src={
															cakeRecipe
																?.medias[0]
														}
														alt={cakeRecipe?.title}
													/>
												</noscript>
											</a>
											<div className="home-content-explore-ible-info">
												<strong>
													<a
														className="ible-title"
														href={`/recipes/${cakeRecipe?.id}`}
													>
														{cakeRecipe?.title}
													</a>
												</strong>
												<span className="ible-author">
													&nbsp;by&nbsp;
													<a
														href={`/users/${cakeRecipe?.author?.id}`}
													>
														{
															cakeRecipe?.author
																?.username
														}
													</a>
												</span>
												<span className="ible-channel">
													&nbsp;in&nbsp;
													<a
														href={`/recipes/${cakeRecipe?.tags[0]?.name?.toLowerCase()}`}
													>
														{cakeRecipe?.tags[0]?.name?.toLowerCase()}
													</a>
												</span>
											</div>
											<div className="ible-stats">
												<span className="ible-stats-left-col ible-featured">
													<span>
														<i
															title="Featured Project"
															className="icon icon-featured"
														></i>
														<span className="thumb-divider"></span>
													</span>
												</span>
												<span className="ible-stats-right-col">
													<span className="ible-favorites">
														<i
															title="Favorites Count"
															className="icon icon-favorite"
														></i>
														&nbsp;1&nbsp;
													</span>
													<span className="ible-views">
														<i
															title="Views Count"
															className="icon icon-views1"
														></i>
														&nbsp;253&nbsp;
													</span>
												</span>
											</div>
										</div>
									))}
								</div>
							</div>
						</div>

						<div className="home-content-explore-category home-content-explore-category-candy clearfix">
							<a
								href="/recipes/candy"
								className="home-content-explore-link"
							>
								<h3>
									<span className="anchor-text">Candy</span>
									&nbsp;
									<i className="fas fa-angle-right fa-2x"></i>
								</h3>
							</a>
							<div className="home-content-explore-category-wrap ">
								<div className="home-content-explore-ibles">
									{candyRecipes?.map((candyRecipe) => (
										<div className="home-content-explore-ible">
											<a
												href={`/recipes/${candyRecipe?.id}`}
											>
												<img
													className=" ls-is-cached lazyloaded"
													data-src={`/recipes/${candyRecipe?.medias[0]}`}
													src="https://images.unsplash.com/photo-1527275393322-8ddae8bd5de9?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2360&q=80"
													alt={candyRecipe?.title}
												/>
												<noscript>
													<img
														src={`/recipes/${candyRecipe?.medias[0]}`}
														alt={candyRecipe?.title}
													/>
												</noscript>
											</a>
											<div className="home-content-explore-ible-info">
												<strong>
													<a
														className="ible-title"
														href={`/recipes/${candyRecipe?.id}`}
													>
														{candyRecipe?.title}
													</a>
												</strong>
												<span className="ible-author">
													&nbsp;by&nbsp;
													<a
														href={`/users/${candyRecipe?.author?.id}`}
													>
														{
															candyRecipe?.author
																?.username
														}
													</a>
												</span>
												<span className="ible-channel">
													&nbsp;in&nbsp;
													<a
														href={`/recipes/${candyRecipe?.tags[0]?.name?.toLowerCase()}`}
													>
														{candyRecipe?.tags[0]?.name?.toLowerCase()}
													</a>
												</span>
											</div>
											<div className="ible-stats">
												<span className="ible-stats-left-col ible-featured">
													<span>
														<i
															title="Featured Project"
															className="icon icon-featured"
														></i>
														<span className="thumb-divider"></span>
													</span>
												</span>
												<span className="ible-stats-right-col">
													<span className="ible-favorites">
														<i
															title="Favorites Count"
															className="icon icon-favorite"
														></i>
														&nbsp;1&nbsp;
													</span>
													<span className="ible-views">
														<i
															title="Views Count"
															className="icon icon-views1"
														></i>
														&nbsp;253&nbsp;
													</span>
												</span>
											</div>
										</div>
									))}
								</div>
							</div>
						</div>

						<div className="home-content-explore-category home-content-explore-category-pasta clearfix">
							<a
								href="/recipes/pasta"
								className="home-content-explore-link"
							>
								<h3>
									<span className="anchor-text">Pasta</span>
									&nbsp;
									<i className="fas fa-angle-right fa-2x"></i>
								</h3>
							</a>
							<div className="home-content-explore-category-wrap ">
								<div className="home-content-explore-ibles">
									{pastaRecipes?.map((pastaRecipe) => (
										<div className="home-content-explore-ible">
											<a
												href={`/recipes/${pastaRecipe?.id}`}
											>
												<img
													className=" ls-is-cached lazyloaded"
													data-src={`/recipes/${pastaRecipe?.medias[0]}`}
													src="https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2360&q=80"
													alt={pastaRecipe?.title}
												/>
												<noscript>
													<img
														src={`/recipes/${pastaRecipe?.medias[0]}`}
														alt={pastaRecipe?.title}
													/>
												</noscript>
											</a>
											<div className="home-content-explore-ible-info">
												<strong>
													<a
														className="ible-title"
														href={`/recipes/${pastaRecipe?.id}`}
													>
														{pastaRecipe?.title}
													</a>
												</strong>
												<span className="ible-author">
													&nbsp;by&nbsp;
													<a
														href={`/users/${pastaRecipe?.author?.id}`}
													>
														{
															pastaRecipe?.author
																?.username
														}
													</a>
												</span>
												<span className="ible-channel">
													&nbsp;in&nbsp;
													<a
														href={`/recipes/${pastaRecipe?.tags[0]?.name?.toLowerCase()}`}
													>
														{pastaRecipe?.tags[0]?.name?.toLowerCase()}
													</a>
												</span>
											</div>
											<div className="ible-stats">
												<span className="ible-stats-left-col ible-featured">
													<span>
														<i
															title="Featured Project"
															className="icon icon-featured"
														></i>
														<span className="thumb-divider"></span>
													</span>
												</span>
												<span className="ible-stats-right-col">
													<span className="ible-favorites">
														<i
															title="Favorites Count"
															className="icon icon-favorite"
														></i>
														&nbsp;1&nbsp;
													</span>
													<span className="ible-views">
														<i
															title="Views Count"
															className="icon icon-views1"
														></i>
														&nbsp;253&nbsp;
													</span>
												</span>
											</div>
										</div>
									))}
								</div>
							</div>
						</div>

						<div className="home-content-explore-category home-content-explore-category-salad clearfix">
							<a
								href="/recipes/salad"
								className="home-content-explore-link"
							>
								<h3>
									<span className="anchor-text">Salad</span>
									&nbsp;
									<i className="fas fa-angle-right fa-2x"></i>
								</h3>
							</a>
							<div className="home-content-explore-category-wrap ">
								<div className="home-content-explore-ibles">
									{saladRecipes?.map((saladRecipe) => (
										<div className="home-content-explore-ible">
											<a
												href={`/recipes/${saladRecipe?.id}`}
											>
												<img
													className=" ls-is-cached lazyloaded"
													data-src={`/recipes/${saladRecipe?.medias[0]}`}
													src="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2360&q=80"
													alt={saladRecipe?.title}
												/>
												<noscript>
													<img
														src={`/recipes/${saladRecipe?.medias[0]}`}
														alt={saladRecipe?.title}
													/>
												</noscript>
											</a>
											<div className="home-content-explore-ible-info">
												<strong>
													<a
														className="ible-title"
														href={`/recipes/${saladRecipe?.id}`}
													>
														{saladRecipe?.title}
													</a>
												</strong>
												<span className="ible-author">
													&nbsp;by&nbsp;
													<a
														href={`/users/${saladRecipe?.author?.id}`}
													>
														{
															saladRecipe?.author
																?.username
														}
													</a>
												</span>
												<span className="ible-channel">
													&nbsp;in&nbsp;
													<a
														href={`/recipes/${saladRecipe?.tags[0]?.name?.toLowerCase()}`}
													>
														{saladRecipe?.tags[0]?.name?.toLowerCase()}
													</a>
												</span>
											</div>
											<div className="ible-stats">
												<span className="ible-stats-left-col ible-featured">
													<span>
														<i
															title="Featured Project"
															className="icon icon-featured"
														></i>
														<span className="thumb-divider"></span>
													</span>
												</span>
												<span className="ible-stats-right-col">
													<span className="ible-favorites">
														<i
															title="Favorites Count"
															className="icon icon-favorite"
														></i>
														&nbsp;1&nbsp;
													</span>
													<span className="ible-views">
														<i
															title="Views Count"
															className="icon icon-views1"
														></i>
														&nbsp;253&nbsp;
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

export default Homepage;
