// constants
const CREATE_RECIPE = 'recipe/CREATE_RECIPE';

//actions
const createRecipeAction = (newRecipe) => ({
    type: CREATE_RECIPE,
    payload: newRecipe
});




//thunks
export const createRecipeThunk = (newRecipe) => async (dispatch) => {
    const responseRecipe = await fetch('/api/recipes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newRecipe.recipe),
    });

    if (responseRecipe.ok) {
        const data = await responseRecipe.json();
        dispatch(setUser(data))
        return null;
    } else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) {
            return data.errors;
        }
    } else {
        return ['An error occurred. Please try again.']
    }
}



const initialState = { newRecipe: null };
export default function reducer(state = initialState, action) {
    switch (action.type) {
        case SET_USER:
            return { user: action.payload }
        case REMOVE_USER:
            return { user: null }
        default:
            return state;
    }
}