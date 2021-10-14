import React, { useState } from 'react';
import { useSelector } from 'react-redux'
import { useParams } from 'react-router';

const CommentForm = (recipe) => {
  const user = useSelector(state => state.session.user);
  const [commentBody, setCommentBody] = useState('');


  const createComment = (e) => {
    e.preventDefault()
    const newComment = {
      comment: commentBody,
      userId: user.id,
      recipeId: recipe.id
    }
    console.log("createComment recipe passed in =====>>", recipe)
    console.log("createComment recipe.comments passed in =====>>", recipe.comments)
    console.log("createComment newComment passed in =====>>", newComment)

    recipe.comments.push(newComment)
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
