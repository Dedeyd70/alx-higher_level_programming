document.addEventListener('DOMContentLoaded', function() {
    // Wait for the DOM to be fully loaded before manipulating it
    const headerElement = document.querySelector('header');

    // Check if the header element is found
    if (headerElement) {
      // Update the text color of the header element to red
      headerElement.style.color = '#FF0000';
    } else {
      console.error('Header element not found');
    }
  });
