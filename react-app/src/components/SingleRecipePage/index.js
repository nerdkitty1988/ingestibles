import { React, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router";
import * as recipeActions from "../../store/recipe"

const SingleRecipePage = () => {
  const dispatch = useDispatch()
  const { recipeId } = useParams();
  const currentRecipe = useSelector(state => state.recipe)
  console.log(currentRecipe)
  useEffect(() => {
    dispatch(recipeActions.retrieveRecipe(recipeId))
  }, [dispatch, recipeId])
  return (
    <div id="recipe-info">
    <h1></h1>
  </div>
  )
}

export default SingleRecipePage
