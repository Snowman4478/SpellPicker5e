import React, { useEffect, useState } from 'react';

const About: React.FC = () => {
  const [content, setContent] = useState<string>('');
  
  
  useEffect(() => {
    // Fetch the HTML content from the Flask backend
    fetch('http://localhost:5000/about') // Assuming this endpoint serves the HTML
      .then(response => response.text())
      .then(data => setContent(data))
      .catch(error => console.error('Error fetching the About page:', error));
  }, []);

  return (
    <div dangerouslySetInnerHTML={{ __html: content }} />
  );
};

export default About;
