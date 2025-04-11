# PROJECT 3 LANGSTON PEARSON

import time
from subject import RaceEvent
from observers.leaderboard_display import LeaderboardDisplay
from observers.commenetaryDisplay import CommentaryDisplay

def main():
    race = RaceEvent()

    leaderboard = LeaderboardDisplay()
    commentary = CommentaryDisplay()

    race.attach(leaderboard)
    race.attach(commentary)

    # Simulate race updates
    race_data = [
        {"Jake": 50, "Jamal": 45, "Emma": 40},
        {"Jake": 70, "Jamal": 68, "Emma": 60},
        {"Jake": 90, "Jamal": 85, "Emma": 80},
        {"Jake": 100, "Jamal": 105, "Emma": 98}
    ]

    for update in race_data:
        race.update_positions(update)
        time.sleep(1)  # Simulate time between race updates

if __name__ == "__main__":
    main()
