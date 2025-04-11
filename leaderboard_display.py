from observer import Observer

class LeaderboardDisplay(Observer):
    def update(self, race_state: dict):
        sorted_racers = sorted(race_state.items(), key=lambda x: x[1], reverse=True)
        print("\n Leaderboard:")
        for position, (racer, distance) in enumerate(sorted_racers, start=1):
            print(f"{position}. {racer} - {distance}m")
