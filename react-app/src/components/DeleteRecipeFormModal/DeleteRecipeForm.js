import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";


function DeleteRecipeForm({ id }) {
  
    const handleSubmit = async (e) => {
        e.preventDefault();

        const deleteResponse = await fetch(`/api/recipes/delete/${id}`, {
            method: 'DELETE'
        })

    };


    return (

        <form onSubmit={handleSubmit}>
            {/* <ul className='error'>
                {errors.map((error, idx) => (
                    <li key={idx}>{error}</li>
                ))}
            </ul> */}
            <div>
                Are you sure to delete this recipe?
            </div>

            <div >
                <button  type="submit">Delete</button>
            </div>

        </form>


    );
}

export default DeleteRecipeForm;