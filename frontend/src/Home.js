import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const Home = () => {
    const [searchInput, setSearchInput] = useState('');
    const [players, setPlayers] = useState([]);
    const [timeoutFlag, setTimeoutFlag] = useState(null);
    const [inputValue, setInputValue] = useState('');
    let timerId; // Store the timer ID
    const navigate = useNavigate();
    const playersStatic = [
        {"first_name":"Curtis","full_name":"Curtis Borchardt","id":2414,"is_active":false,"last_name":"Borchardt"},
        {"first_name":"Curtis","full_name":"Curtis Jerrells","id":201998,"is_active":false,"last_name":"Jerrells"},
        {"first_name":"Curtis","full_name":"Curtis Kitchen","id":77280,"is_active":false,"last_name":"Kitchen"},
        {"first_name":"Curtis","full_name":"Curtis Perry","id":77835,"is_active":false,"last_name":"Perry"},
        {"first_name":"Curtis","full_name":"Curtis Rowe","id":78028,"is_active":false,"last_name":"Rowe"},
        {"first_name":"Radisav","full_name":"Radisav Curcic","id":76488,"is_active":false,"last_name":"Curcic"},
        {"first_name":"Armand","full_name":"Armand Cure","id":76489,"is_active":false,"last_name":"Cure"},
        {"first_name":"Earl","full_name":"Earl Cureton","id":940,"is_active":false,"last_name":"Cureton"},
        {"first_name":"Bill","full_name":"Bill Curley","id":223,"is_active":false,"last_name":"Curley"},
        {"first_name":"Fran","full_name":"Fran Curran","id":76492,"is_active":false,"last_name":"Curran"},
        {"first_name":"Dell","full_name":"Dell Curry","id":209,"is_active":false,"last_name":"Curry"},
        {"first_name":"Eddy","full_name":"Eddy Curry","id":2201,"is_active":false,"last_name":"Curry"},
        {"first_name":"JamesOn","full_name":"JamesOn Curry","id":201191,"is_active":false,"last_name":"Curry"},
        {"first_name":"Michael","full_name":"Michael Curry","id":688,"is_active":false,"last_name":"Curry"},
        {"first_name":"Seth","full_name":"Seth Curry","id":203552,"is_active":true,"last_name":"Curry"},
        {"first_name":"Stephen","full_name":"Stephen Curry","id":201939,"is_active":true,"last_name":"Curry"},
        {"first_name":"J.P.","full_name":"J.P. Macura","id":1629122,"is_active":false,"last_name":"Macura"},
        {"first_name":"Carey","full_name":"Carey Scurry","id":78102,"is_active":false,"last_name":"Scurry"}
      ];      
    // if (searchInput.trim() === '') {
    //   //     setPlayers([]);
    //   //     return;
    //   //     }

        
        const fetchPlayers = (inputValue) => {
          console.log('fetching data for: ', inputValue)
          // Grab the current value of the input

          // WORK IN PROGRESS!!!
          // const searchInput = document.querySelector('.searchBar').value;
        
          // // Perform the API request based on the search input
          // fetch(`/api/player/search/${searchInput}`)
          //   .then((response) => response.json())
          //   .then((data) => {
          //     setPlayers(data);
          //   })
          //   .catch((error) => {
          //     console.error('Error:', error);
          //   });
        };

        const checkForTwoChars = (inputValue) => {
          if (inputValue.length >= 2) {
            console.log(`Search for players with at least 2 characters: ${inputValue}`);
            // Clear any previous timers to prevent multiple updates
            clearTimeout(timerId);
            timerId = setTimeout(() => {
              setSearchInput(inputValue);
              if(timeoutFlag == false){
                setTimeoutFlag(true);
              }
              else if(timeoutFlag == true){
                setTimeoutFlag(false);
              }
              else if(timeoutFlag == null){
                setTimeoutFlag(true);
              }
            }, 1000);
          }
        };
      
        const handleInputChange = (event) => {
          setInputValue(event.target.value);
          setSearchInput(inputValue);
          checkForTwoChars(inputValue);
        };

        useEffect(() => {
          console.log('timer just ended! The input was:', inputValue);
          if(timeoutFlag != null){
            fetchPlayers(inputValue);
          }
        }, [timeoutFlag])
      
        return (
          <div className="homePageDiv">
            <div className="homePageLogoDiv">
              <img
                src={process.env.PUBLIC_URL + '/hoopLogicLogo1.png'}
                alt="Hoop Logic Logo"
                className="homePageLogo"
              />
            </div>
            <div className="searchBarDiv">
            <input
              type="text"
              placeholder="Search for players by name"
              className="searchBar"
              style={{ fontFamily: 'Norwester' }}
              onChange={handleInputChange}
            />
              <div className="suggestedPlayersDiv">
                {players.map((player) => (
                  <div key={player.id}>{player.full_name}</div>
                ))}
              </div>
            </div>
          </div>
        );
};

export default Home;