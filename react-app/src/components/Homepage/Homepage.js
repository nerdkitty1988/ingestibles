import React, { useState, useEffect } from "react";
import { NavLink } from "react-router-dom";
import "./Homepage.css";
import Carousel from "react-responsive-carousel/lib/js/components/Carousel/index";
import "react-responsive-carousel/lib/styles/carousel.min.css";

const Homepage = () => {

	const [randomRecipes, setRandomRecipes] = useState([]);
	const [tags1, setTags1] = useState([]);
	const [tags2, setTags2] = useState([]);
	const [tags3, setTags3] = useState([]);
	const [tags4, setTags4] = useState([]);
	const [tags5, setTags5] = useState([]);

	const [tagName1, setTagName1] = useState([]);
	const [tagName2, setTagName2] = useState([]);
	const [tagName3, setTagName3] = useState([]);
	const [tagName4, setTagName4] = useState([]);
	const [tagName5, setTagName5] = useState([]);

	useEffect(() => {
		async function randomFive() {
			const res = await fetch("/api/tags/random");
			const resData = await res.json();

			const newArr = [];

			(resData?.random)?.forEach(ele => {
				newArr.push(ele?.name)
			})

			const randomSet = new Set(newArr);
			const randomArr2 = Array.from(randomSet);
			const random5 = randomArr2.slice(0, 5);

			setRandomRecipes(random5);
		};

		randomFive();

	}, []);



	useEffect(() => {
		const one = async () => {
			const res = await fetch(`/api/recipes/${randomRecipes[0]}`);
			const resData = await res.json();
			setTags1(resData?.tagged);
			setTagName1((resData?.tagged)[0]?.tags?.find(ele => ele?.name === randomRecipes[0])?.name)
		};

		const two = async () => {
			const res = await fetch(`/api/recipes/${randomRecipes[1]}`);
			const resData = await res.json();
			setTags2(resData?.tagged);
			setTagName2((resData?.tagged)[0]?.tags?.find(ele => ele?.name === randomRecipes[1])?.name)
		};

		const three = async () => {
			const res = await fetch(`/api/recipes/${randomRecipes[2]}`);
			const resData = await res.json();
			setTags3(resData?.tagged);
			setTagName3((resData?.tagged)[0]?.tags?.find(ele => ele?.name === randomRecipes[2])?.name)
		};

		const four = async () => {
			const res = await fetch(`/api/recipes/${randomRecipes[3]}`);
			const resData = await res.json();
			setTags4(resData?.tagged);
			setTagName4((resData?.tagged)[0]?.tags?.find(ele => ele?.name === randomRecipes[3])?.name)
		};

		const five = async () => {
			const res = await fetch(`/api/recipes/${randomRecipes[4]}`);
			const resData = await res.json();
			setTags5(resData?.tagged);
			setTagName5((resData?.tagged)[0]?.tags?.find(ele => ele?.name === randomRecipes[4])?.name)
		};

		one();
		two();
		three();
		four();
		five();
	}, [randomRecipes]);


	return (
		<main>
			<div
				id="home-container"
				className="home-wrapper-wrapper full-wrapper home-content clearfix"
			>
				<div
					id="home-content-rotator"
					className="home-content-rotator carousel carousel-fade"
				>
					<div className="home-content-rotator-inner carousel-inner">

						<div className="home-content-rotator-slide-overlay">
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

						<Carousel id="slider" className="home-content-rotator-inner carousel-inner" infiniteLoop={true} autoPlay={true} showThumbs={false} showArrows={false} showIndicators={false} showStatus={false} interval={5000} stopOnHover={false}>
							<div>
								<img className="splash-images" alt="car1" src="https://images.unsplash.com/photo-1598023696416-0193a0bcd302?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1836&q=80" />
							</div>
							<div>
								<img className="splash-images" alt="car2" src="https://images.unsplash.com/photo-1626078297492-b7dc55294332?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1770&q=80" />
							</div>
							<div>
								<img className="splash-images" alt="car3" src="https://images.unsplash.com/photo-1607198179219-cd8b835fdda7?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1469&q=80" />
							</div>
							<div>
								<img className="splash-images" alt="car4" src="https://images.unsplash.com/photo-1455619452474-d2be8b1e70cd?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1470&q=80" />
							</div>
							<div>
								<img className="splash-images" alt="car5" src="https://images.unsplash.com/photo-1540432797114-187727adf19b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2274&q=80" />
							</div>
							<div>
								<img className="splash-images" alt="car6" src="https://images.unsplash.com/photo-1563379926898-05f4575a45d8?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1770&q=80" />
							</div>
						</Carousel>

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
						{tagName1&&tagName1!=='Undefined'&& <div className={`home-content-explore-category clearfix`}>
							<h3>
								<span className="anchor-text">{randomRecipes && tags1 && tagName1 && tagName1}</span>
								&nbsp;
								<i className="fas fa-angle-right fa-2x"></i>
							</h3>
							<div className="home-content-explore-category-wrap ">
								<div className="home-content-explore-ibles">
									{randomRecipes && tags1 && tags1?.map((tag1) => (
										<div key={tag1?.id} className="home-content-explore-ible">
											<NavLink
												to={`/recipes/${tag1?.id}`}
											>
												<img
													className=" ls-is-cached lazyloaded"
													data-src={tag1?.medias[0]?.mediaUrl}
													src={tag1?.medias[0]?.mediaUrl}
													alt={tag1?.title}
												/>
											</NavLink>
											<div className="home-content-explore-ible-info">
												<strong>
													<NavLink
														className="ible-title"
														to={`/recipes/${tag1?.id}`}
													>
														{tag1?.title}
													</NavLink>
												</strong>
												<span className="ible-author">
													&nbsp;by&nbsp;{tag1?.author?.username}
												</span>
											</div>
										</div>
									))}
								</div>
							</div>
						</div>}

						{tagName1&&tagName1!=='Undefined'&& <div className={`home-content-explore-category clearfix`}>
							<h3>
								<span className="anchor-text">{randomRecipes && tags2 && tagName2 && tagName2}</span>
								&nbsp;
								<i className="fas fa-angle-right fa-2x"></i>
							</h3>
							<div className="home-content-explore-category-wrap ">
								<div className="home-content-explore-ibles">
									{randomRecipes && tags2 && tags2?.map((tag2) => (
										<div key={tag2?.id} className="home-content-explore-ible">
											<NavLink
												to={`/recipes/${tag2?.id}`}
											>
												<img
													className=" ls-is-cached lazyloaded"
													data-src={tag2?.medias[0]?.mediaUrl}
													src={tag2?.medias[0]?.mediaUrl}
													alt={tag2?.title}
												/>
											</NavLink>
											<div className="home-content-explore-ible-info">
												<strong>
													<NavLink
														className="ible-title"
														to={`/recipes/${tag2?.id}`}
													>
														{tag2?.title}
													</NavLink>
												</strong>
												<span className="ible-author">
													&nbsp;by&nbsp;{tag2?.author?.username}
												</span>
											</div>
										</div>
									))}
								</div>
							</div>
						</div>}

						{tagName1&&tagName1!=='Undefined'&& <div className={`home-content-explore-category clearfix`}>
							<h3>
								<span className="anchor-text">{randomRecipes && tags3 && tagName3 && tagName3}</span>
								&nbsp;
								<i className="fas fa-angle-right fa-2x"></i>
							</h3>
							<div className="home-content-explore-category-wrap ">
								<div className="home-content-explore-ibles">
									{randomRecipes && tags3 && tags3?.map((tag3) => (
										<div key={tag3?.id} className="home-content-explore-ible">
											<NavLink
												to={`/recipes/${tag3?.id}`}
											>
												<img
													className=" ls-is-cached lazyloaded"
													data-src={tag3?.medias[0]?.mediaUrl}
													src={tag3?.medias[0]?.mediaUrl}
													alt={tag3?.title}
												/>
											</NavLink>
											<div className="home-content-explore-ible-info">
												<strong>
													<NavLink
														className="ible-title"
														to={`/recipes/${tag3?.id}`}
													>
														{tag3?.title}
													</NavLink>
												</strong>
												<span className="ible-author">
													&nbsp;by&nbsp;{tag3?.author?.username}
												</span>
											</div>
										</div>
									))}
								</div>
							</div>
						</div>}

						{tagName1&&tagName1!=='Undefined'&& <div className={`home-content-explore-category clearfix`}>
							<h3>
								<span className="anchor-text">{randomRecipes && tags4 && tagName4 && tagName4}</span>
								&nbsp;
								<i className="fas fa-angle-right fa-2x"></i>
							</h3>
							<div className="home-content-explore-category-wrap ">
								<div className="home-content-explore-ibles">
									{randomRecipes && tags4 && tags4?.map((tag4) => (
										<div key={tag4?.id} className="home-content-explore-ible">
											<NavLink
												to={`/recipes/${tag4?.id}`}
											>
												<img
													className=" ls-is-cached lazyloaded"
													data-src={tag4?.medias[0]?.mediaUrl}
													src={tag4?.medias[0]?.mediaUrl}
													alt={tag4?.title}
												/>
											</NavLink>
											<div className="home-content-explore-ible-info">
												<strong>
													<NavLink
														className="ible-title"
														to={`/recipes/${tag4?.id}`}
													>
														{tag4?.title}
													</NavLink>
												</strong>
												<span className="ible-author">
													&nbsp;by&nbsp;{tag4?.author?.username}
												</span>
											</div>
										</div>
									))}
								</div>
							</div>
						</div>}

						{tagName1&&tagName1!=='Undefined'&& <div className={`home-content-explore-category clearfix`}>
							<h3>
								<span className="anchor-text">{randomRecipes && tags5 && tagName5 && tagName5}</span>
								&nbsp;
								<i className="fas fa-angle-right fa-2x"></i>
							</h3>
							<div className="home-content-explore-category-wrap ">
								<div className="home-content-explore-ibles">
									{randomRecipes && tags5 && tags5?.map((tag5) => (
										<div key={tag5?.id} className="home-content-explore-ible">
											<NavLink
												to={`/recipes/${tag5?.id}`}
											>
												<img
													className=" ls-is-cached lazyloaded"
													data-src={tag5?.medias[0]?.mediaUrl}
													src={tag5?.medias[0]?.mediaUrl}
													alt={tag5?.title}
												/>
											</NavLink>
											<div className="home-content-explore-ible-info">
												<strong>
													<NavLink
														className="ible-title"
														to={`/recipes/${tag5?.id}`}
													>
														{tag5?.title}
													</NavLink>
												</strong>
												<span className="ible-author">
													&nbsp;by&nbsp;{tag5?.author?.username}
												</span>
											</div>
										</div>
									))}
								</div>
							</div>
						</div>}

					</div>
				</div>
			</div>
		</main>
	);
};

export default Homepage;
