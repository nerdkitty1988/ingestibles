import React, { useState } from 'react';
import { Modal } from '../../context/Modal';
import DeleteRecipeForm from './DeleteRecipeForm';
import { useSelector } from 'react-redux';




function DeleteRecipeFormModal({ id}) {

    const [showModal, setShowModal] = useState(false);

    return (
        <div style={{ display: 'inline' }}>
            <button  onClick={() => setShowModal(true)}>Delete</button>

            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <DeleteRecipeForm id={id} />
                </Modal>
            )}

        </div>
    );
}

export default DeleteRecipeFormModal;