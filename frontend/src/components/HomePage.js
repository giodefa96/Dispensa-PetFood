// HomePage.js  
import React from 'react';  
import { Container, Button } from 'react-bootstrap';  
  
function HomePage() {  
  return (  
    <Container className="p-3">  
      <h1>Welcome to the Home Page!</h1>  
      <p>  
        This is a simple hero unit, a simple jumbotron-style component for calling  
        extra attention to featured content or information.  
      </p>  
      <p>  
        <Button variant="primary">Learn more</Button>  
      </p>  
    </Container>  
  );  
}  
  
export default HomePage;  
