import React, { useState } from 'react';
import { useSelector } from 'react-redux'
import "./EditComment.css"
const EditComment = ({currentRecipe, setCanEdit, setComments, commentId}) => {
  const user = useSelector(state => state.session.user);
  const [comment, setComment] = useState('');
  const [errors , setErrors] = useState([])

  const updateComment = async(e) => {
    e.preventDefault()
    const newComment = {
      comment,
      userId: user.id,
      recipeId: currentRecipe.id
    }
    currentRecipe?.comments?.push(newComment)

    const commentData = await fetch(`/api/recipes/comments/${commentId}`, {
      method: 'PATCH',
      body: JSON.stringify({
        ...newComment
          }),
          headers: {
            "Content-Type": "application/json"
          }
      })
      const data = await commentData.json()
      //console.log("DATA HERE EDIT COMMENT =========>>>>>", data)
      if(data.errors){
        setErrors(data.errors)
        setCanEdit(true)
      }else {
        setCanEdit(false)
        const newComments = await (await fetch('/api/recipes/comments')).json()
        //console.log("NEW COMMENTS .JSON ======>>>>", newComments)
        setComments(newComments.comments)
      }

    return data
  }


  return (
    <>
    <div id="outer-most-div">
      <div style={{ color:'#F27D21'}}>
                  {errors.map((error, ind) => (
                  <li style={{ marginLeft:'15%', textAlign:'start'}}
                          key={ind}>{error}</li>
                  ))}
      </div>
      <form id="edit-comment-form" onSubmit={updateComment}>
        <div>
          <textarea id="edit-comment-textarea"
            name='comment'
            onChange={(e) => setComment(e.target.value)}
            value={comment}
          ></textarea>
        </div>
      </form>
    </div>
    <div id="bottom-of-the-white-box">
      <p id="comment-note">If you ain't got nothin' nice to say, don't say nothin' at all.</p>
      <div id="post-comment-button-div">
        <button id="cancel-button" className="commentButtons" onClick={() => setCanEdit(false)}>Cancel</button>
        <button id="little-post-comment-button" type='submit' form="edit-comment-form">Save</button>
      </div>
    </div>
    </>
  );
};

export default EditComment;
