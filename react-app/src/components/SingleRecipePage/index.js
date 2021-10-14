import { React, useEffect, useState } from "react";
import { useSelector} from "react-redux";
import { useParams } from "react-router";
import Instruction from "../Instruction"
import "./SingleRecipePage.css"

const SingleRecipePage = () => {
  const { recipeId } = useParams();
  const sessionUser = useSelector((state) => state.session.user);
  console.log(sessionUser)
  const [currentRecipe, setCurrentRecipe] = useState({});
  const [otherRecipes, setOtherRecipes] = useState([]);

  // async function retrieveRecipe() {
  //   const recipeFetch = await fetch(`/api/recipes/${recipeId}`)
  //   const currentRecipeData = await recipeFetch.json();
  //   const recipeData = currentRecipeData.recipe[0]
  //   setCurrentRecipe(recipeData)
  // }

  // async function retrieveOtherRecipes() {
  //   const recipeData = await fetch(`/api/recipes`)
  //   const currentRecipeData = await recipeData.json();
  //   const recipeArray = currentRecipeData.recipes.filter(recipe => recipe.authorId === currentRecipe.authorId)
  //   const othersArray = recipeArray.filter(recipe => recipe.id !== currentRecipe.id)
  //   console.log("WE GET HERE")
  //   setOtherRecipes(othersArray)
  // }
  const fetchData = () => {
   const thisRecipe =  fetch(`/api/recipes/${recipeId}`).then((res) => res.json())//.then((data) => setCurrentRecipe(data.recipe[0]))
   const others = fetch(`/api/recipes`).then((res) => res.json())//.then((data) => setOtherRecipes([...data recipes.filter(recipe => recipe.authorId === currentRecipe.authorId && recipe.id !== currentRecipe.id)]))
  Promise.all([thisRecipe, others]).then((allData) => {
    setCurrentRecipe(allData[0].recipe[0])
    setOtherRecipes(allData[1].recipes)})
  }

  useEffect(() => {
    fetchData()
    //console.log(recipeFetch)
    //retrieveOtherRecipes()
    //console.log("NOW IM GOING")
  },[])



  console.log("IM AT THE END", currentRecipe.comments, otherRecipes)
  const whatIWant = otherRecipes.filter(recipe => recipe.authorId === currentRecipe.authorId && recipe.id !== currentRecipe.id)
  console.log("RIGHT AFTER", whatIWant)
  const recipeImages = currentRecipe?.instructions?.map(instruction => instruction.imageUrl)
  const authorsIds = otherRecipes.map(recipe => recipe.author.id)
  console.log("authorsIds ===>>>",authorsIds)
  const authorsImages = otherRecipes.map(recipe => recipe.author.profilePic)
  console.log("authorsImages ===>>>",authorsImages)

  const authorIdsArr = [...new Set(authorsIds)]
  console.log("authorsIdsArr ===>>>",authorIdsArr)
  const authorImagesArr = [...new Set(authorsImages)]
  console.log("authorImagesArr ====>>>", authorImagesArr)


  const authorsObject = {}
  for(let i = 0; i < authorIdsArr.length; i++){
    let image = authorImagesArr[i];
    let id = authorIdsArr[i];
    authorsObject[id] = image;
  }

  console.log(authorsObject);

  const today  = new Date();

  console.log(today.toLocaleDateString("en-US"));
  return (
    <div id="main">
    <div id="recipe-info">
      <h1>{currentRecipe.title}</h1>
      <p>By {currentRecipe?.author?.username} {">"}</p>
    </div>
    <div id="like-license-buttons">
      <button id="like-button">
        <i className="fas fa-heart"></i>Like
      </button>
    </div>
    <div id="recipe-images">
      <img src={recipeImages && recipeImages[recipeImages.length - 1]} alt="meat" />
    </div>
    <div id="author-info">
      <div id="top-author-info">
        <div id="author-image">
          <img className="profileCircle" src={currentRecipe?.author?.profilePic} alt="profile" />
        </div>
        <div id="more-by-author">
          <p id="more-by-author-text">More by <br/>
                                      the author:</p>
          <div id="other-recipes-by-author">
            {whatIWant && whatIWant.map(recipe => {
              return (<><a href={`/recipes/${recipe.id}`}>{recipe.title}</a> <br/></>)
            })}
          </div>
        </div>
      </div>
      <div id="author-bio-container">
        <div id="author-bio">
          <p>About: {currentRecipe?.author?.biography}</p>
        </div>
      </div>
    </div>
    <div id="recipe-description">
      <p>{currentRecipe?.description}</p>
    </div>
    <div id="comment-button-container">
      <a href="#comments-section" id="comment-button"><i className="fas fa-comments"></i>Comment</a>
    </div>
    {currentRecipe?.instructions?.map((instruction, index) => {
      return (
        <div key={index} id="step">
        <p><strong> Step {index + 1}: {instruction.stepTitle}</strong></p>
        <Instruction instruction={instruction}/>
      </div>
      )
    })}
    <div id="comments-section">
      <h1>{currentRecipe?.comments?.length} comments </h1>
      {currentRecipe?.comments?.map((comment) => {
        return (
          <div id="comment">
            <div id="comment-image-username-date">
              <img className="profileCircle" id="comment-owner-image" src={authorsObject[comment.userId]} alt="author"/>
              <a id="comment-owner-username" href={`/users/${comment.userId}`}>MyUserName{comment.userId}</a>
              <p id="comment-date">{today.toLocaleDateString("en-US")}</p>
            </div>

            <p id="comment-text">{comment.comment}</p>
        </div>
        )
      })}
    </div>
  </div>
  )
}

export default SingleRecipePage
