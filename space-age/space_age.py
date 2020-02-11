class SpaceAge:
    def __init__(self, seconds):
        self.time = seconds / 31557600

    def on_earth(self):
        return round(self.time, 2)

    def on_mercury(self):
        return round(self.time / 0.2408467, 2)

    def on_venus(self):
        return round(self.time / 0.61519726, 2)

    def on_mars(self):
        return round(self.time / 1.8808158, 2)

    def on_jupiter(self):
        return round(self.time / 11.862615, 2)

    def on_saturn(self):
        return round(self.time / 29.447498, 2)

    def on_uranus(self):
        return round(self.time / 84.016846, 2)

    def on_neptune(self):
        return round(self.time / 164.79132, 2)



"""
Earth: orbital period 365.25 Earth days, or 31557600 seconds
Mercury: orbital period 0.2408467 Earth years
Venus: orbital period 0.61519726 Earth years
Mars: orbital period 1.8808158 Earth years
Jupiter: orbital period 11.862615 Earth years
Saturn: orbital period 29.447498 Earth years
Uranus: orbital period 84.016846 Earth years
Neptune: orbital period 164.79132 Earth years
"""