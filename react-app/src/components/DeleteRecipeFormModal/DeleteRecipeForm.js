import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux"; 

function DeleteRecipeForm({ id, userId, setCreatedRecipes, setLikedRecipes, setShowDelete, open, setOpen }) {
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        const deleteResponse = await fetch(`/api/recipes/delete/${id}`, {
            method: 'DELETE'
        })
        // re-set all created_recipes to dynamically shown on page when recipe is deleted
        const response = await fetch(`/api/recipes/my_plate/${userId}`);
        const responseData = await response.json();
        setCreatedRecipes(responseData.created);
        setLikedRecipes(responseData.liked);
    };

    const cancelSubmit = async (e) => {
        e.preventDefault();
        setOpen(false)
        setShowDelete(true)
        // re-set all created_recipes to dynamically shown on page when recipe is deleted
        // const response = await fetch(`/api/recipes/my_plate/${userId}`);
        // const responseData = await response.json();
        // setCreatedRecipes(responseData.created);
    };

    return (
        open && (<div style={{ color:'#F27D21', fontWeight:'bold'}}>
            {/* <ul className='error'>
                {errors.map((error, idx) => (
                    <li key={idx}>{error}</li>
                ))}
            </ul> */}

            Are you sure to delete this recipe?

            <div >
                <button
                    className='btn-category-header'
                    onClick={handleSubmit}
                >Confirm</button>
                <button
                    className='btn-category-header'
                    onClick={cancelSubmit}
                >Cancel</button>

            </div>
        </div>)


    );
}

export default DeleteRecipeForm;