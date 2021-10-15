import React, { useState, useEffect } from "react";
import "./Recipes.css";


const Recipes = () => {
	const [allRecipes, setAllRecipes] = useState([]);
	const [recentRecipes, setRecentRecipes] = useState([]);
	const [previousRecipes, setPreviousRecipes] = useState([]);

	useEffect(() => {
		async function recipes() {
			const response = await fetch('/api/recipes');
			const responseData = await response.json();
			setAllRecipes(responseData);
		}

        async function recent_recipes() {
			const response = await fetch('/api/recipes/recent');
			const responseData = await response.json();
			setRecentRecipes(responseData);
		}

    // remember to exclude the first 5 from this array
        async function previous_recipes() {
			const response = await fetch('/api/recipes/previous');
			const responseData = await response.json();
			setPreviousRecipes(responseData);
		}

		recipes();
        recent_recipes();
        previous_recipes();
	}, []);

  const recRecipes = recentRecipes?.recent
  const prevRecipes = previousRecipes?.previous?.slice(5)


  return (
    <main>
      <div
				id="home-container"
				className="home-wrapper-wrapper full-wrapper home-content clearfix"
			>
        <h1>Hello World. I'm going to put some stuff here.</h1>

        <hr />

        <div className="home-content-explore">
          <div className="home-content-explore-wrap">
            <h2>Recipes</h2>
            <div className={`home-content-explore-category home-content-explore-category-recent clearfix`}>
              <NavLink
                to={'/recipes'}
                className="home-content-explore-link"
              >
                <h3>
                  <span className="anchor-text">Most Recent</span>
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
                        {/* ////////////after seeding media, copy data-src and paste into src below for each category!!!!//////////// */}
                        <img
                          className=" ls-is-cached lazyloaded"
                          data-src={
                            recRecipe?.medias[0]
                          }
                          src="https://images.unsplash.com/photo-1588195538326-c5b1e9f80a1b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2250&q=80"
                          alt={recRecipe?.title}
                        />
                        <noscript>
                          <img
                            src={
                              recRecipe
                                ?.medias[0]
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

            <div>
              <NavLink
                to={'/recipes'}
                className="home-content-explore-link"
              >
                <h3>
                  <span className="anchor-text">Previous</span>
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
                          data-src={`/recipes/${prevRecipe?.medias[0]}`}
                          src="https://images.unsplash.com/photo-1527275393322-8ddae8bd5de9?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2360&q=80"
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
  )






};

export default Recipes;
