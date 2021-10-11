import { React, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router";
import * as recipeActions from "../../store/recipe"

const SingleRecipePage = () => {
  const dispatch = useDispatch()
  const { recipeId } = useParams();
  const currentRecipe = useSelector(state => state.recipe)
  console.log("CURRENT RECIPE ====>>>", currentRecipe)
  useEffect(() => {
    dispatch(recipeActions.retrieveRecipe(recipeId))
  }, [dispatch, recipeId])
  return (
  <>
    <div id="recipe-info">
      <h1>{currentRecipe?.title}</h1>
      <p>By {currentRecipe?.author?.username} > insert tag name here</p>
    </div>
    <div id="recipe-image">
      list of images{currentRecipe?.instructions?.map(instruction => {
        <img src={instruction.imageUrl}/>
      })}
    </div>
  </>
  )
}

export default SingleRecipePage
