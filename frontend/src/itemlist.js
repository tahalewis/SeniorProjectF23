// src/components/ItemList.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ItemList() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    axios.get('/api/items')
      .then((response) => setItems(response.data))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h1>Items</h1>
      <ul>
        {items.map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default ItemList;
