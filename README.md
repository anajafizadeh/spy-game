
# 🕵️ Spy Game

I developed a Spy Party-style game using **Django** as a personal project to strengthen my backend development skills and experiment with session-based gameplay. The app allows multiple players to join a session and get assigned roles—one or more players become the **Spies**, while the others are **Citizens**. The Spies must figure out the secret location, while the Citizens try to identify the Spies before time runs out.  

The project was built with Django’s **MTV architecture** (Models, Templates, Views) and leverages Django sessions to manage user states across different rounds. It also includes a round timer, dynamic role assignments, and a clean UI for game instructions and interaction.  

The game is hosted online and can be played here: 👉 [Spy Game on Render](https://spy-game-qz5d.onrender.com/)

---

## 🎮 How to Play
1. **Start a game session**: One player creates a new session and shares the session code with friends.  
2. **Join the game**: Other players enter the session code to join the game.  
3. **Role assignment**: Each player is randomly assigned a role:  
   - 🕵️ **Spy (or Spies)**: Do not know the location. Your goal is to blend in and avoid detection while trying to guess the location.  
   - 👥 **Citizens**: Know the location. Your goal is to identify the Spy/Spies without giving away too much information.  
4. **Discussion round**: Players ask each other questions about the location to try and identify who the Spies are.  
5. **Voting**: At the end of the round, everyone votes on who they think the Spy/Spies are.  
6. **Win conditions**:  
   - Citizens win if they correctly identify all Spies.  
   - The Spies win if at least one Spy guesses the location or if the Citizens fail to identify all of them.  

---

## ⚙️ Features
- Multiplayer game sessions with unique codes  
- Random role assignment (supports multiple Spies per round)  
- Round timer to keep the game fast-paced  
- Voting system to identify Spies  
- Session-based tracking of players and roles  
- Simple, responsive UI built with Django templates  

---

## 🛠️ Tech Stack
- **Backend**: Django (Python)  
- **Frontend**: HTML, CSS (Django Templates)  
- **Hosting**: Render  

---

## 📂 Installation & Setup
If you’d like to run the project locally:

```bash
# Clone the repository
git clone https://github.com/your-username/spy-game.git
cd spy-game

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
