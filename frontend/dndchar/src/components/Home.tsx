import React from 'react';
import { Link } from 'react-router-dom';

function Home() {

    return (
    <div>
        <h1>Home Page</h1>
        <Link to="/spell-picker">
            <button>Go to Spell Picker</button>
        </Link>
        <Link to="/about">
            <button>Go to About Page</button>
        </Link>
    </div>
    );
}

export default Home;
