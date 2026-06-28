# 🏎️ NEED FOR SPEED: COPPERBELT DRIFT

A thrilling street racing game with police chases! Race against opponents, escape from cops, and rise to the top.

## Features

✨ **Gameplay Features:**
- 🏁 Race against AI opponents
- 🚨 Dynamic police chases (60% chance after winning)
- 🎯 Multiple difficulty levels (Easy, Normal, Hard, Insane)
- 🚗 Three car choices (Supra, Skyline, Mustang)
- 📊 Real-time race progress visualization
- 📈 Career statistics tracking

⚡ **Race Mechanics:**
- **Gas**: Consistent speed boost (15-25m)
- **Drift**: High risk/reward (30m on success, 5m on failure)

🚔 **Police Chase Mechanics:**
- **Speed Boost**: Accelerate quickly (25-35m)
- **Evasive Maneuver**: 50/50 chance to gain distance (20-30m)
- **Hide in Alley**: 50/50 chance to fully escape

## Installation

### Option 1: Direct Run
```bash
# Clone the repository
git clone https://github.com/kapapala577-ux/CAR-RACING-ZED-TOP-SPEED.git
cd CAR-RACING-ZED-TOP-SPEED

# Run CLI version
python racing_game.py

# Run GUI version
python gui_app.py
```

### Option 2: Install as Package
```bash
pip install -e .

# Run from command line
racing-game          # CLI version
racing-game-gui      # GUI version
```

## Usage

### CLI Version (Text-based)
```bash
python racing_game.py
```
- Choose difficulty level
- Select your car
- Use 'G' for gas, 'D' for drift
- During police chase, choose 'S' (speed), 'E' (evasion), or 'H' (hide)

### GUI Version (Graphical Interface)
```bash
python gui_app.py
```
- Click to select difficulty and car
- Use GUI buttons for race actions
- View real-time stats

## Game Mechanics

### Difficulty Levels

| Level | Opponent Speed | Police Speed | Description |
|-------|---|---|---|
| Easy | 8-18 m/s | 18-35 m/s | Great for beginners |
| Normal | 12-26 m/s | 18-42 m/s | Balanced challenge |
| Hard | 15-30 m/s | 18-48 m/s | Intense races |
| Insane | 18-35 m/s | 18-55 m/s | Nearly impossible |

### Police Chase
- **60% chance** to trigger after winning a race
- Police speed increases when close to you
- Choose escape tactics strategically
- Get caught = lose the race bonus

## Statistics Tracked
- Races won/lost
- Win rate percentage
- Police encounters
- Successful escapes vs captures
- Escape rate percentage

## Requirements

- Python 3.7+
- No external dependencies for CLI version
- tkinter (included with Python) for GUI version

## File Structure

```
CAR-RACING-ZED-TOP-SPEED/
├── racing_game.py      # Core game logic (CLI)
├── gui_app.py          # GUI version
├── requirements.txt    # Dependencies
├── setup.py           # Package setup
└── README.md          # This file
```

## Game Flow

1. **Menu Screen**
   - Select difficulty
   - Choose car

2. **Race Phase**
   - Choose action each turn (Gas/Drift)
   - Opponent moves randomly
   - Race ends when either reaches 100m

3. **Police Chase** (if triggered)
   - Evade police using three tactics
   - Police pursues with increasing speed
   - Escape = keep winnings, Caught = lose everything

4. **Stats Display**
   - View career statistics
   - Play again or return to menu

## Tips & Tricks

💡 **Racing Tips:**
- Gas is safer but slower
- Drift is risky but can give you leads
- Mix both strategies for best results

🚔 **Police Chase Tips:**
- Use speed boost when police are far away
- Save "Hide in Alley" for emergencies
- Evasive maneuvers work best in the middle
- Keep distance if you can

## Future Features

- 🎵 Sound effects and music
- 🏆 Leaderboard system
- 🎨 More car customization
- 🗺️ Different race tracks
- 👥 Multiplayer support
- 🎮 Joystick support

## Contributing

Feel free to fork and submit pull requests!

## License

MIT License - feel free to use this code for any purpose!

## Author

Created with ❤️ for racing game enthusiasts

---

**🏁 Ready to race? Start your engines! 🏁**
