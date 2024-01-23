import React, {useState, useEffect} from 'react'
import Book from './Book';
import axios from 'axios';

export default function Booklist() {
    const [books, setBooks] = useState([]);

    useEffect(() => {
      try{
        const response = axios.get('http://127.0.0.1:8000/api/get/');
        console.log(response)
        setBooks(response.data);
      }catch(error){
        console.log(error.response)
      }
    }, []); // Run only once on component mount

  return (


      <div>
        <h2>Book List</h2>
        {books.map(book => (
          <Book key={book.id} book={book} />
        ))}
      </div>

  );
}
