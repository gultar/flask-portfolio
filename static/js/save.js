function saveArticle(slug, content) {
    const url = `/edit/${slug}`;
    const data = {
      content: content
    };
  
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: new URLSearchParams(data)
    })
      .then(response => {
        if (response.ok) {
          console.log('Article saved successfully.');
          location.reload(); // Optional: Reload the page after saving
        } else {
          console.log('Failed to save the article.');
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
}
  