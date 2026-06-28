import random
import time

class RaceGame:
    def __init__(self, difficulty="normal"):
        self.difficulty = difficulty
        self.race_length = 100
        self.opponent_speed_range = self._get_opponent_speed_range()
        self.rounds_won = 0
        self.rounds_lost = 0
        self.police_caught = 0
        self.police_escaped = 0
        
    def _get_opponent_speed_range(self):
        """Adjust opponent difficulty based on selected level."""
        ranges = {
            "easy": (8, 18),
            "normal": (12, 26),
            "hard": (15, 30),
            "insane": (18, 35)
        }
        return ranges.get(self.difficulty, (12, 26))
    
    def get_valid_car(self):
        """Get user's car choice with validation."""
        valid_cars = ["Supra", "Skyline", "Mustang"]
        while True:
            car = input("Choose your ride (Supra, Skyline, or Mustang): ").strip().capitalize()
            if car in valid_cars:
                return car
            print("❌ Invalid choice! Pick from: Supra, Skyline, or Mustang")
    
    def get_valid_action(self):
        """Get validated player action."""
        while True:
            action = input("\n[G]as or [D]rift? ").lower().strip()
            if action in ['g', 'd']:
                return action
            print("❌ Invalid input! Press 'g' for gas or 'd' for drift.")
    
    def execute_gas_action(self):
        """Player chooses to gas."""
        speed = random.randint(15, 25)
        print(f"🏁 You floor the gas and surge forward by {speed} meters!")
        return speed
    
    def execute_drift_action(self):
        """Player chooses to drift with risk/reward."""
        drift_success = random.choice([True, False])
        if drift_success:
            print("✨ Perfect drift! You hit the nitro and rocket forward by 30 meters!")
            return 30
        else:
            print("💥 You spun out! You only gained 5 meters.")
            return 5
    
    def simulate_opponent_turn(self):
        """Simulate opponent's movement."""
        min_speed, max_speed = self.opponent_speed_range
        speed = random.randint(min_speed, max_speed)
        return speed
    
    def simulate_police_movement(self, police_distance, player_distance):
        """Simulate police car movement - they accelerate when close."""
        distance_gap = player_distance - police_distance
        
        if distance_gap < 10:  # Police very close - aggressive pursuit
            police_speed = random.randint(28, 38)
            print("🚨 🚨 POLICE ARE RIGHT ON YOUR TAIL! 🚨 🚨")
        elif distance_gap < 25:  # Police getting close
            police_speed = random.randint(22, 32)
            print("⚠️  Police are gaining on you!")
        else:  # Police far behind
            police_speed = random.randint(18, 28)
            print("🚔 Police in pursuit...")
        
        return police_speed
    
    def display_race_status(self, player_dist, opponent_dist, police_dist=None):
        """Show visual race progress."""
        player_progress = int((player_dist / self.race_length) * 20)
        opponent_progress = int((opponent_dist / self.race_length) * 20)
        
        print(f"\n📊 Race Progress:")
        print(f"   You:      [{'█' * player_progress}{'░' * (20 - player_progress)}] {player_dist}m")
        print(f"   Opponent: [{'█' * opponent_progress}{'░' * (20 - opponent_progress)}] {opponent_dist}m")
        
        if police_dist is not None:
            police_progress = int((police_dist / self.race_length) * 20)
            print(f"   Police:   [{'🚔' * police_progress}{'░' * (20 - police_progress)}] {police_dist}m")
    
    def police_chase_phase(self, player_distance, opponent_distance):
        """Handle police chase after race ends."""
        print("\n" + "="*50)
        print("🚨 ILLEGAL STREET RACE DETECTED! 🚨")
        print("="*50)
        time.sleep(1.5)
        
        police_distance = 0
        chase_turn = 0
        max_police_speed = 35 if self.difficulty == "easy" else 42 if self.difficulty == "normal" else 48 if self.difficulty == "hard" else 55
        
        while police_distance < self.race_length and player_distance < self.race_length * 1.5:
            chase_turn += 1
            print(f"\n--- Chase Turn {chase_turn} ---")
            
            # Player must escape
            print("\n🏃 ESCAPE OPTIONS:")
            print("   [S]peed boost (risky, uses fuel)")
            print("   [E]vasive maneuver (chance to lose them)")
            print("   [H]ide in alley (50/50 chance)")
            
            while True:
                escape_action = input("\nChoose action (S/E/H): ").lower().strip()
                if escape_action in ['s', 'e', 'h']:
                    break
                print("❌ Invalid input!")
            
            if escape_action == 's':
                # Speed boost
                boost_speed = random.randint(25, 35)
                print(f"⚡ SPEED BOOST! You accelerate by {boost_speed} meters!")
                player_distance += boost_speed
            
            elif escape_action == 'e':
                # Evasive maneuver
                if random.choice([True, False]):
                    evasion_distance = random.randint(20, 30)
                    print(f"🎯 Excellent evasive maneuver! You gain {evasion_distance} meters!")
                    player_distance += evasion_distance
                else:
                    print("❌ Failed evasion! Police narrowed the gap!")
                    player_distance += random.randint(5, 10)
            
            elif escape_action == 'h':
                # Hide in alley
                if random.choice([True, False]):
                    print("✅ You hid successfully! Police drove past...")
                    return True  # Escaped!
                else:
                    print("❌ They spotted you in the alley!")
                    player_distance += random.randint(3, 8)
            
            # Police pursuit
            police_speed = self.simulate_police_movement(police_distance, player_distance)
            police_distance += police_speed
            
            self.display_race_status(player_distance, 0, police_distance)
            
            # Check if caught
            if police_distance >= player_distance:
                print("\n" + "="*50)
                print("🚨 BUSTED! POLICE CAUGHT YOU! 🚨")
                print("="*50)
                print("💔 You got arrested and lost the pink slips!")
                self.police_caught += 1
                return False
            
            time.sleep(0.5)
        
        # Player escaped!
        print("\n" + "="*50)
        print("✅ YOU ESCAPED! POLICE LOST YOU! ✅")
        print("="*50)
        print("🎉 You made it safely away with the pink slips!")
        self.police_escaped += 1
        return True
    
    def start_race(self):
        """Main race loop."""
        print("\n" + "="*50)
        print("   🏎️  NEED FOR SPEED: COPPERBELT DRIFT 🏎️")
        print("="*50)
        
        car = self.get_valid_car()
        print(f"\n🚗 You line up in your {car}.")
        print("The lights flash: 🔴 🔴 🔴 🟢\n")
        time.sleep(2)
        
        player_distance = 0
        opponent_distance = 0
        turn = 0
        
        while player_distance < self.race_length and opponent_distance < self.race_length:
            turn += 1
            print(f"\n--- Turn {turn} ---")
            
            # Player action
            action = self.get_valid_action()
            if action == 'g':
                player_distance += self.execute_gas_action()
            else:  # drift
                player_distance += self.execute_drift_action()
            
            # Opponent action
            opponent_speed = self.simulate_opponent_turn()
            opponent_distance += opponent_speed
            print(f"🤖 Opponent advances by {opponent_speed} meters!")
            
            # Display race status
            self.display_race_status(player_distance, opponent_distance)
            time.sleep(0.5)
        
        # Determine race winner
        print("\n" + "="*50)
        race_won = False
        if player_distance >= self.race_length and player_distance > opponent_distance:
            print("🏆 YOU WIN THE RACE!")
            race_won = True
            self.rounds_won += 1
        else:
            print("💔 OPPONENT WINS THE RACE!")
            self.rounds_lost += 1
        
        # Police might show up!
        print("\n" + "-"*50)
        police_chance = random.randint(1, 100)
        
        if police_chance > 40:  # 60% chance police show up
            print("👮 Police spotted the illegal race!")
            time.sleep(1)
            escaped = self.police_chase_phase(player_distance, opponent_distance)
            return race_won and escaped
        else:
            print("✅ You got away clean! No police!")
            return race_won
    
    def show_stats(self):
        """Display career statistics."""
        total_races = self.rounds_won + self.rounds_lost
        total_chases = self.police_escaped + self.police_caught
        
        print(f"\n📈 CAREER STATS:")
        print(f"   Races Won: {self.rounds_won} | Races Lost: {self.rounds_lost}")
        
        if total_races > 0:
            win_rate = (self.rounds_won / total_races * 100)
            print(f"   Win Rate: {win_rate:.1f}%")
        
        if total_chases > 0:
            escape_rate = (self.police_escaped / total_chases * 100)
            print(f"\n   Police Chases: {total_chases}")
            print(f"   Escaped: {self.police_escaped} | Caught: {self.police_caught}")
            print(f"   Escape Rate: {escape_rate:.1f}%")
        
        print(f"   Total Successful Races: {self.rounds_won - self.police_caught}")
    
    def play_again(self):
        """Ask if player wants another race."""
        while True:
            choice = input("\n🔄 Race again? (Y/N): ").lower().strip()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            print("❌ Please enter Y or N")

def main():
    """Main game loop."""
    print("\n🎮 SELECT DIFFICULTY:")
    print("   1. Easy    (Slow opponent, slow police)")
    print("   2. Normal  (Balanced)")
    print("   3. Hard    (Fast opponent, fast police)")
    print("   4. Insane  (Nearly impossible)")
    
    difficulty_choice = input("\nEnter difficulty (1-4): ").strip()
    difficulties = {"1": "easy", "2": "normal", "3": "hard", "4": "insane"}
    difficulty = difficulties.get(difficulty_choice, "normal")
    
    game = RaceGame(difficulty=difficulty)
    print(f"\n✅ Difficulty set to: {difficulty.upper()}")
    
    while True:
        game.start_race()
        game.show_stats()
        
        if not game.play_again():
            print("\n👋 Thanks for playing! FINAL STATS:")
            game.show_stats()
            print("\n🏁 See you on the track!\n")
            break

if __name__ == "__main__":
    main()
