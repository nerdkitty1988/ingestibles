import React from 'react';

const AddTag = ({count}) => {

    return (
       
        <div>
            <label>Tag #{count+2}</label>
            <input
                className='listingInput'
                type="text"
                        // value={tagName}
                        // onChange={(e) => setTagName(e.target.value)}
                placeholder='Tag'
                    // required
            />
        </div>
    
    );
}

export default AddTag;