import React, { useState } from 'react';
import { useSelector } from 'react-redux'

const CommentForm = ({currentRecipe}) => {
  const user = useSelector(state => state.session.user);
  const [commentBody, setCommentBody] = useState('');
  const createComment = async(e) => {
    e.preventDefault()
    const newComment = {
      "commentBody": commentBody,
      "userId": user.id,
      "recipeId": currentRecipe.id
    }
    currentRecipe?.comments?.push(newComment)
    console.log("createComment recipe passed in =====>>", currentRecipe)
    console.log("createComment recipe.comments passed in =====>>",currentRecipe['comments'])
    console.log("createComment newComment passed in =====>>", newComment)

    //createNewComment(newComment)
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
    return data
  }


  return (
    <form onSubmit={createComment}>
      <div>
        <label>What do you think?</label>
        <textarea
          name='commentBody'
          onChange={(e) => setCommentBody(e.target.value)}
          value={commentBody}
        ></textarea>
      </div>
      <button type='submit'>Post Comment</button>
    </form>
  );
};

export default CommentForm;
