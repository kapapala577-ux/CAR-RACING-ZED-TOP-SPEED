import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import threading
from racing_game import RaceGame

class RaceGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🏎️ NEED FOR SPEED: COPPERBELT DRIFT 🏎️")
        self.root.geometry("900x700")
        self.root.configure(bg="#1a1a1a")
        
        self.game = None
        self.difficulty = tk.StringVar(value="normal")
        self.car_choice = tk.StringVar(value="Supra")
        
        self.setup_styles()
        self.create_menu_screen()
        
    def setup_styles(self):
        """Configure tkinter styles."""
        style = ttk.Style()
        style.theme_use('darkly')
        
    def clear_window(self):
        """Clear all widgets from window."""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def create_menu_screen(self):
        """Create the main menu screen."""
        self.clear_window()
        
        frame = tk.Frame(self.root, bg="#1a1a1a")
        frame.pack(expand=True)
        
        # Title
        title_label = tk.Label(
            frame,
            text="🏎️ NEED FOR SPEED\nCOPPERBELT DRIFT 🏎️",
            font=("Arial", 28, "bold"),
            fg="#ff6b6b",
            bg="#1a1a1a"
        )
        title_label.pack(pady=20)
        
        # Subtitle
        subtitle_label = tk.Label(
            frame,
            text="Race for Glory, Escape from Cops!",
            font=("Arial", 14),
            fg="#ffd93d",
            bg="#1a1a1a"
        )
        subtitle_label.pack(pady=10)
        
        # Difficulty selection
        difficulty_frame = tk.LabelFrame(
            frame,
            text="SELECT DIFFICULTY",
            font=("Arial", 12, "bold"),
            fg="#4ecdc4",
            bg="#2a2a2a",
            padx=20,
            pady=20
        )
        difficulty_frame.pack(pady=20)
        
        difficulties = [("1️⃣  Easy", "easy"), ("2️⃣  Normal", "normal"), ("3️⃣  Hard", "hard"), ("4️⃣  Insane", "insane")]
        
        for label, value in difficulties:
            rb = tk.Radiobutton(
                difficulty_frame,
                text=label,
                variable=self.difficulty,
                value=value,
                font=("Arial", 11),
                fg="#4ecdc4",
                bg="#2a2a2a",
                selectcolor="#1a1a1a",
                activeforeground="#ff6b6b",
                activebackground="#2a2a2a"
            )
            rb.pack(anchor=tk.W, pady=5)
        
        # Car selection
        car_frame = tk.LabelFrame(
            frame,
            text="SELECT YOUR RIDE",
            font=("Arial", 12, "bold"),
            fg="#4ecdc4",
            bg="#2a2a2a",
            padx=20,
            pady=20
        )
        car_frame.pack(pady=20)
        
        cars = [("🏎️ Supra", "Supra"), ("🏎️ Skyline", "Skyline"), ("🏎️ Mustang", "Mustang")]
        
        for label, value in cars:
            rb = tk.Radiobutton(
                car_frame,
                text=label,
                variable=self.car_choice,
                value=value,
                font=("Arial", 11),
                fg="#4ecdc4",
                bg="#2a2a2a",
                selectcolor="#1a1a1a",
                activeforeground="#ff6b6b",
                activebackground="#2a2a2a"
            )
            rb.pack(anchor=tk.W, pady=5)
        
        # Start button
        start_button = tk.Button(
            frame,
            text="🏁 START RACE",
            font=("Arial", 14, "bold"),
            bg="#ff6b6b",
            fg="white",
            padx=30,
            pady=10,
            command=self.start_game,
            cursor="hand2"
        )
        start_button.pack(pady=20)
    
    def start_game(self):
        """Start the game."""
        self.game = RaceGame(difficulty=self.difficulty.get())
        self.show_race_screen()
    
    def show_race_screen(self):
        """Show the race screen."""
        self.clear_window()
        
        # Title
        title_label = tk.Label(
            self.root,
            text=f"🏎️ Racing in your {self.car_choice.get()}",
            font=("Arial", 16, "bold"),
            fg="#ff6b6b",
            bg="#1a1a1a"
        )
        title_label.pack(pady=10)
        
        # Race display
        display_frame = tk.Frame(self.root, bg="#2a2a2a", height=300)
        display_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        self.race_text = scrolledtext.ScrolledText(
            display_frame,
            height=15,
            width=90,
            bg="#1a1a1a",
            fg="#4ecdc4",
            font=("Courier", 10)
        )
        self.race_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Controls
        controls_frame = tk.Frame(self.root, bg="#1a1a1a")
        controls_frame.pack(pady=10)
        
        gas_button = tk.Button(
            controls_frame,
            text="⚡ GAS IT",
            font=("Arial", 12, "bold"),
            bg="#ffd93d",
            fg="black",
            padx=20,
            pady=10,
            command=lambda: self.player_action('g'),
            cursor="hand2"
        )
        gas_button.pack(side=tk.LEFT, padx=10)
        
        drift_button = tk.Button(
            controls_frame,
            text="🎯 DRIFT",
            font=("Arial", 12, "bold"),
            bg="#4ecdc4",
            fg="black",
            padx=20,
            pady=10,
            command=lambda: self.player_action('d'),
            cursor="hand2"
        )
        drift_button.pack(side=tk.LEFT, padx=10)
        
        # Start race in separate thread
        threading.Thread(target=self.run_gui_race, daemon=True).start()
    
    def run_gui_race(self):
        """Run the race in GUI mode."""
        self.race_text.insert(tk.END, "🚗 You line up at the starting grid...\n")
        self.race_text.insert(tk.END, "The lights flash: 🔴 🔴 🔴 🟢\n\n")
        self.race_text.see(tk.END)
        self.root.update()
        
        player_distance = 0
        opponent_distance = 0
        turn = 0
        
        while player_distance < self.game.race_length and opponent_distance < self.game.race_length:
            turn += 1
            self.race_text.insert(tk.END, f"--- Turn {turn} ---\n")
            self.race_text.see(tk.END)
            self.root.update()
            
            # Wait for player input (simplified for GUI)
            import time
            time.sleep(1)
            
            # Simulate player action
            action = random.choice(['g', 'd'])
            if action == 'g':
                speed = random.randint(15, 25)
                self.race_text.insert(tk.END, f"🏁 You floor the gas and surge forward by {speed} meters!\n")
                player_distance += speed
            else:
                drift_success = random.choice([True, False])
                if drift_success:
                    self.race_text.insert(tk.END, f"✨ Perfect drift! You advance 30 meters!\n")
                    player_distance += 30
                else:
                    self.race_text.insert(tk.END, f"💥 You spun out! Only 5 meters.\n")
                    player_distance += 5
            
            # Opponent
            opponent_speed = self.game.simulate_opponent_turn()
            opponent_distance += opponent_speed
            self.race_text.insert(tk.END, f"🤖 Opponent: {opponent_distance}m\n")
            
            self.race_text.insert(tk.END, f"\n📊 You: {player_distance}m | Opponent: {opponent_distance}m\n\n")
            self.race_text.see(tk.END)
            self.root.update()
        
        # Race result
        if player_distance > opponent_distance:
            self.race_text.insert(tk.END, "🏆 YOU WON! 🏆\n")
            self.game.rounds_won += 1
        else:
            self.race_text.insert(tk.END, "💔 OPPONENT WINS!\n")
            self.game.rounds_lost += 1
        
        self.race_text.see(tk.END)
        self.root.update()
        
        # Show stats after delay
        import time
        time.sleep(2)
        self.show_stats_screen()
    
    def player_action(self, action):
        """Handle player action (placeholder)."""
        pass
    
    def show_stats_screen(self):
        """Show final statistics."""
        self.clear_window()
        
        stats_frame = tk.Frame(self.root, bg="#1a1a1a")
        stats_frame.pack(expand=True)
        
        title = tk.Label(
            stats_frame,
            text="📈 CAREER STATS",
            font=("Arial", 20, "bold"),
            fg="#4ecdc4",
            bg="#1a1a1a"
        )
        title.pack(pady=20)
        
        stats_text = f"""
🏎️  RACES WON: {self.game.rounds_won}
💔 RACES LOST: {self.game.rounds_lost}
👮 POLICE CAUGHT: {self.game.police_caught}
✅ ESCAPES: {self.game.police_escaped}
        """
        
        stats_label = tk.Label(
            stats_frame,
            text=stats_text,
            font=("Arial", 14),
            fg="#ffd93d",
            bg="#1a1a1a",
            justify=tk.LEFT
        )
        stats_label.pack(pady=20)
        
        # Buttons
        button_frame = tk.Frame(stats_frame, bg="#1a1a1a")
        button_frame.pack(pady=20)
        
        next_button = tk.Button(
            button_frame,
            text="🔄 NEXT RACE",
            font=("Arial", 12, "bold"),
            bg="#ff6b6b",
            fg="white",
            padx=20,
            pady=10,
            command=self.show_race_screen,
            cursor="hand2"
        )
        next_button.pack(side=tk.LEFT, padx=10)
        
        menu_button = tk.Button(
            button_frame,
            text="🏠 MAIN MENU",
            font=("Arial", 12, "bold"),
            bg="#4ecdc4",
            fg="black",
            padx=20,
            pady=10,
            command=self.create_menu_screen,
            cursor="hand2"
        )
        menu_button.pack(side=tk.LEFT, padx=10)
        
        exit_button = tk.Button(
            button_frame,
            text="❌ EXIT",
            font=("Arial", 12, "bold"),
            bg="#888888",
            fg="white",
            padx=20,
            pady=10,
            command=self.root.quit,
            cursor="hand2"
        )
        exit_button.pack(side=tk.LEFT, padx=10)

def main():
    root = tk.Tk()
    app = RaceGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()