import { React, useEffect, useState } from "react";
import { useDispatch} from "react-redux";
import { useParams } from "react-router";
import Instruction from "../Instruction"
import SlideShow from "../SlideShow";
import "./SingleRecipePage.css"

const SingleRecipePage = () => {
  const dispatch = useDispatch()
  const { recipeId } = useParams();
  const [currentRecipe, setCurrentRecipe] = useState([])
  const recipeImages = currentRecipe?.instructions?.map(instruction => instruction.imageUrl)
  console.log(currentRecipe?.author)
  useEffect(() => {
    async function retrieveRecipe(recipeId) {
      const recipeData = await fetch(`/api/recipes/${recipeId}`)
      const currentRecipeData = await recipeData.json();
      setCurrentRecipe(...currentRecipeData.recipe)
    }
    retrieveRecipe(recipeId)
  }, [dispatch, recipeId])
  return (
    <div id="main">
    <div id="recipe-info">
      <h1>{currentRecipe.title}</h1>
      <p>By {currentRecipe?.author?.username} {">"} tag</p>
    </div>
    <div id="recipe-images">
      {recipeImages?.map(img => <img id="recipe-image" src={img} alt="instruction"/>
      )}
      <SlideShow recipeImages={recipeImages} />
    </div>
    <div id="author-info">
      <img className="profileCircle" src={currentRecipe?.author?.profilePic} alt="profile" />
      <p>{currentRecipe?.author?.biography}</p>
    </div>
    <div id="recipe-description">
      <p>{currentRecipe?.description}</p>
    </div>
    <button>Comment</button>
    {currentRecipe?.instructions?.map((instruction) => {
      return <Instruction instruction={instruction}/>
    })}
  </div>
  )
}

export default SingleRecipePage
