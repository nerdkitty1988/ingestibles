import React, { useState } from 'react';
import { useSelector } from 'react-redux'
import "./NewComment.css"

const NewComment = ({currentRecipe, setCanComment, setComments, setCommenting}) => {
  const user = useSelector(state => state.session.user);
  const [comment, setComment] = useState('');
  const [errors , setErrors] = useState([])


  const createComment = async(e) => {
    e.preventDefault()
    const newComment = {
      comment,
      userId: user.id,
      recipeId: currentRecipe.id
    }
    currentRecipe?.comments?.push(newComment)

    const commentData = await fetch(`/api/recipes/comments`, {
      method: 'POST',
      body: JSON.stringify({
        ...newComment
          }),
          headers: {
            "Content-Type": "application/json"
          }
      })
      const data = await commentData.json()
      //console.log("DATA =======>>>>", data)
      if(data.errors){
        setErrors(data.errors)
        setCanComment(true)
      }else {
        setCanComment(false)
      }

      const newComments = await (await fetch('/api/recipes/comments')).json()
      //console.log("NEW COMMENTS .JSON ======>>>>", newComments)
      setComments(newComments.comments)
      setCommenting(false)

    return data
  }


  return (
    <>
      <div style={{ color:'#F27D21'}}>
                    {errors.map((error, ind) => (
                    <li style={{ marginLeft:'15%', textAlign:'start'}}
                            key={'newCommentErr'+ind}>{error}</li>
                    ))}
                </div>
    <form id="comment-form" onSubmit={createComment}>
      <textarea id="comment-textarea"
        name='comment'
        onChange={(e) => setComment(e.target.value)}
        value={comment}
      ></textarea>
    </form>
  </>
  );
};

export default NewComment;
