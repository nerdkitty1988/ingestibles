const GET_RECIPE = 'recipe/GET_RECIPE'
const REMOVE_RECIPE = 'recipe/REMOVE_RECIPE'

const getRecipe = (recipe) => ({
  type: GET_RECIPE,
  recipe
})

export const retrieveRecipe = (recipe) => {
  return async dispatch => {
    const response = await fetch(`/api/recipes/${recipe}`);
    const data = await response.json();
    dispatch(getRecipe(...data.recipe));
    return response;
  }
}

const initialState = { recipe: null }

export default function recipeReducer(state = initialState, action) {
  switch (action.type) {
    case GET_RECIPE:
      return action.recipe
    case REMOVE_RECIPE:
      return { recipe: null }
    default:
      return state;
  }
}
