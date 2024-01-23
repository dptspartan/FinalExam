import React, {useState} from 'react'
import axios from 'axios';

export default function Book({book}) {
    const [editedGenre, setEditedGenre] = useState(book.genre);
    const [editedAuthor, setEditedAuthor] = useState(book.author);
    const handleEdit = () => {
    try{
      const response = axios.post({'id': book.id,
                             'newgenre': editedGenre,
                            'newauthor': editedAuthor}, 'http://127.0.0.1:8000/api/update/');
    }catch(error){

    }
    };
    const handleDelete = () => {
      // Make API call to delete the book
      // Example: deleteBookInAPI(book.id)
      // Then, you can update the local state or fetch the updated data from the API
    };
    return (
      <div>
        <h3>{book.title}</h3>
        <p>Author: {book.author}</p>
        <p>Genre: {book.genre}</p>
        <button onClick={handleEdit}>Edit</button>
        <button onClick={handleDelete}>Delete</button>
      </div>
    );
}
