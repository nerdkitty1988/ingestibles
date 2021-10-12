// constants
// const CREATE_RECIPE = 'recipe/CREATE_RECIPE';

//actions
// const createRecipeAction = (newRecipe) => ({
//     type: CREATE_RECIPE,
//     payload: newRecipe
// });




//thunks
export const createRecipeThunk = (newRecipe) => async (dispatch) => {
    const responseRecipe = await fetch('/api/recipes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ...newRecipe.recipe,        
                                tags:newRecipe.tags,
                                media: newRecipe.media,
                                ingredients: newRecipe.ingredients,
                                steps: newRecipe.steps,

        }),
    });


    if (responseRecipe.ok) {
        const data = await responseRecipe.json();
        // dispatch()
        return data;
    } else if (responseRecipe.status < 500) {
        const data = await responseRecipe.json();
        if (data.errors) {
            return data;
        }
    } else {
        return ['An error occurred. Please try again.']
    }
}


// No need to store redux for newly create recipe

// const initialState = { newRecipe: null };
// export default function reducer(state = initialState, action) {
//     switch (action.type) {
//         case CREATE_RECIPE:
//             return { user: action.payload }
//         default:
//             return state;
//     }
// }