import React, { useState, useEffect } from 'react';
import './PlayerSearch.css';

const PlayerSearch = () => {
  const [searchInput, setSearchInput] = useState('');
  const [players, setPlayers] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleInputChange = (e) => {
    setSearchInput(e.target.value);
  };

  const searchPlayers = () => {
    if (searchInput.trim() === '') {
      alert('Please enter a player name.');
      return;
    }

    setLoading(true);

    // Replace this URL with your API endpoint
    fetch(`/api/player/search/${searchInput}`)
      .then((response) => response.json())
      .then((data) => {
        setPlayers(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error:', error);
        setLoading(false);
      });
  };

  return (
    <div className="PlayerSearch">
      <h1>NBA Player Search</h1>
      <div className="search-container">
        <input
          type="text"
          placeholder="Search for players by name"
          value={searchInput}
          onChange={handleInputChange}
        />
        <button onClick={searchPlayers} disabled={loading}>
          {loading ? 'Searching...' : 'Search'}
        </button>
      </div>
      <ul>
        {players.map((player) => (
          <li key={player.id} className="player-item">
            {player.full_name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PlayerSearch;
