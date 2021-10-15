import React, { useState } from 'react';
import { Modal, ModalContext } from '../../context/Modal';
import DeleteRecipeForm from './DeleteRecipeForm';
// import { useSelector } from 'react-redux';

function DeleteRecipeFormModal({ id, userId, setCreatedRecipes, setLikedRecipes}) {

    const [showModal, setShowModal] = useState(false);
    const [showDelete, setShowDelete] = useState(true);
    const [open, setOpen] = useState(true)

    return (
        <div style={{ display: 'inline' }}>
            {showDelete && <button className='btn-category-header'
            onClick={() => {
                setShowModal(true)
                setShowDelete(false)
                setOpen(true)
                }}>Delete</button>}
           
            {showModal && (
                
                <ModalContext.Provider value={{ setShowModal }} onClose={() => {setShowModal(false)}}>
                    <DeleteRecipeForm 
                    id={id} 
                    userId={userId} 
                    setCreatedRecipes={setCreatedRecipes}
                    setLikedRecipes={setLikedRecipes}
                    setShowDelete={setShowDelete} setOpen={setOpen} open={open}/>
                </ModalContext.Provider>
                
            )}

        </div>
    );
}

export default DeleteRecipeFormModal;