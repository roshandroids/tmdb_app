# Flask Movie App Documentation

## TMDb API

**The Movie Database (TMDb) API:**
The Movie Database (TMDb) API is a comprehensive movie and TV database that provides access to a vast collection of movie-related information. It offers endpoints to retrieve details about movies, TV shows, actors, and more. In this project, we utilized the TMDb API to fetch information about movies, including popular movies and search results.

## Functionality of the Web App

**Overview:**
The web app is built using Flask, a Python web framework, and it leverages the TMDb API to fetch and display movie data. This web app is deployed using https://render.com and can be access live at https://tmdb-app.onrender.com. The primary functionalities include:

1. **Display Popular Movies:**
   - The homepage displays a list of popular movies retrieved from the TMDb API.
2. **Search Movies:**
   - Users can use the search bar to look for specific movies. The search functionality queries the TMDb API and displays the search results.

## Challenges Faced

**1. API Key Management:**

- One challenge was securely managing the TMDb API key. It's essential to keep API keys secure, especially in a public repository. A solution involved using environment variables to store sensitive information.

**2. Responsive Design:**

- Ensuring the web application's responsiveness across different devices was a challenge. Testing and refining the CSS styles and layout were crucial to creating a user-friendly experience on various screen sizes.

**3. Deployment on Render:**

- Deploying the Flask application on Render posed some challenges, especially in configuring environment variables and ensuring that the deployment environment matched the local development environment.

## Future Development

**1. User Authentication:**

- Implement user authentication to allow users to save favorite movies, rate movies, or create personalized watchlists.

**2. Movie Details:**

- Extend the application to display detailed information about each movie, including cast and crew details, release dates, and user reviews.

**3. Pagination:**

- Implement pagination for both popular movies and search results to improve performance and user experience, especially when dealing with a large number of movies.

**4. Testing and Refinement:**

- Ongoing testing and refinement of the application, including unit tests, usability testing, and performance optimization.

## Conclusion

The Flask Movie App project successfully demonstrates the integration of the Flask web framework with an external API (TMDb). Challenges encountered during

## How to Run Locally

To run this project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/roshandroids/tmdb_app.git
   cd your-repository
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set TMDb API Key:**
   ```bash
   Replace the placeholder in the TMDB_API_KEY variable in the app.py file with your TMDb API key.
   ```
4. **Run the Application:**
   ```bash
   python app.py
   ```
   The application will be accessible at http://127.0.0.1:5000/ in your web browser.

## Usage

- Open your web browser and navigate to http://127.0.0.1:5000/.
- You will see a list of popular movies by default.
- Use the search bar to search for specific movies.

## Additional Notes

The project uses Flask as the web framework and requests to interact with the TMDb API.
Make sure to keep your TMDb API key secure and do not share it publicly.
