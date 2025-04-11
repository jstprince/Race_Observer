from observer import Observer

class CommentaryDisplay(Observer):
    def __init__(self):
        self._previous_state = {}

    def update(self, race_state: dict):
        print("\n️ Race Commentary:")
        for racer, distance in race_state.items():
            prev_distance = self._previous_state.get(racer, 0)
            if distance > prev_distance:
                print(f"{racer} advanced to {distance}m.")
            elif distance == prev_distance:
                print(f"{racer} is holding position at {distance}m.")
            else:
                print(f"{racer} dropped back to {distance}m!")
        self._previous_state = race_state.copy()