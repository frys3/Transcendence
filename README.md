# Transcendence
A web application designed for the mighty Pong contest ! The goal is to allow users to play real-time multiplayer Pong with other participants.

### Mandatory Implementations

- Single Page Application: The website is designed as a single-page application, ensuring seamless user interaction with minimal page reloads.
- Vanilla JavaScript Frontend: The frontend is developed in vanilla JavaScript, guaranteeing compatibility with the latest version of Google Chrome.
- Real-Time Multiplayer Pong: Users can participate in live Pong games directly on the website, playing against other users.
- Tournament System: Users can join tournaments, with the system organizing matches and determining winners.
- Registration & Matchmaking: Players register with an alias for each tournament, and matchmaking ensures a fair and competitive environment.
- Dockerized Deployment: The entire website runs in a containerized environment, using Docker to ensure smooth deployment and security.
- Password Hashing: All user passwords are hashed before storage.
- Protection Against SQL Injection/XSS: The website is safeguarded against common web vulnerabilities such as SQL injection and cross-site scripting.
- HTTPS and WSS: The entire site, including websockets, operates over secure HTTPS and WSS protocols.
- Form Validation: All user inputs are validated either on the frontend or backend to ensure data integrity and prevent malicious inputs.
- Environment Variables: Sensitive information such as API keys and credentials are securely stored in environment variables, which are not included in version control.

### Additional Implementations

- Backend as Microservices: we have divided functionality into independent services, each with its own database.
- Backend Framework: Instead of using pure Ruby, we are leveraging a backend framework to handle server-side logic more efficiently.
- Database Integration: A robust database is used to store essential information such as user data, tournament progress, and game statistics.
- Frontend Framework: We opted to use a frontend framework/toolkit to streamline the development of the user interface and improve scalability.
- Standard User Management: We have implemented a full-fledged user management system, allowing for user registration, authentication, and tournament participation tracking.
- Two-Factor Authentication: We have implemented a Two-Factor Authentication (2FA) with JWT token.
- Remote Players: Players can compete against each other remotely, adding an online multiplayer dimension to the Pong experience.
- Server-Side Pong: Instead of relying on client-side game logic, the game mechanics are processed on the server, improving fairness and synchronizing game state across players.
- API Implementation: We’ve implemented a comprehensive API that facilitates communication between the server and clients, allowing for real-time game updates and remote gameplay.
- Extended Browser Compatibility: While we focus on Chrome compatibility, we’ve extended support to other modern browsers to ensure a broader reach.
- Server-Side Rendering (SSR): We’ve integrated server-side rendering to improve performance and SEO, ensuring that the website is fast and responsive across devices.

## Installation
Clone the repository.

Make sure you have an .env file with all the necessary API keys (42, Django). You can use the file .envsample for reference.

Your machine should have docker installed with sudo privileges.

To perform the initial setup of the project, you can run the following commands:

```bash
make
```

## Technologies
- Docker
- Nginx
- PostreSQL
- Django / Python
- Javascript
- html / CSS / bootstrap
