import { React, useEffect, useState } from "react";
import { useDispatch} from "react-redux";
import { useParams } from "react-router";
import Instruction from "../Instruction"
import "./SingleRecipePage.css"

const SingleRecipePage = () => {
  const dispatch = useDispatch()
  const { recipeId } = useParams();
  const [currentRecipe, setCurrentRecipe] = useState([])
  async function retrieveRecipe(recipeId) {
    const recipeData = await fetch(`/api/recipes/${recipeId}`)
    const currentRecipeData = await recipeData.json();
    setCurrentRecipe(...currentRecipeData.recipe)
  }
  useEffect(() => {
    retrieveRecipe(recipeId)
  }, [dispatch, recipeId])
  const recipeImages = currentRecipe?.instructions?.map(instruction => instruction.imageUrl)
  console.log("RECIPE IMAGES", recipeImages)
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
      <div id="author-image">
        <img className="profileCircle" src={currentRecipe?.author?.profilePic} alt="profile" />
      </div>
      <div id="more-by-author">
        <p id="more-by-author-text">More by the author:</p>
      </div>
      <div id="author-bio">
        <p>About: {currentRecipe?.author?.biography}</p>
      </div>
    </div>
    <div id="recipe-description">
      <p>{currentRecipe?.description}</p>
    </div>
    <div id="comment-button-container">
      <button id="comment-button"><i className="fas fa-comments"></i>Comment</button>
    </div>
    {currentRecipe?.instructions?.map((instruction, index) => {
      return (
        <div id="step">
        <p><strong> Step {index + 1}: {instruction.stepTitle}</strong></p>
        <Instruction instruction={instruction}/>
      </div>
      )
    })}
  </div>
  )
}

export default SingleRecipePage
