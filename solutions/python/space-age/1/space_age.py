class SpaceAge:
    EARTH_SECONDS = 31557600  # 365.25 days * 24 hours * 3600 seconds
    
    ORBITAL_PERIODS = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
    }
    
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds/self.EARTH_SECONDS, 2)
        
    def on_mercury(self):
        years = self.seconds/(self.EARTH_SECONDS*self.ORBITAL_PERIODS['mercury'])
        return round(years, 2)

    def on_venus(self):
        years = self.seconds/(self.EARTH_SECONDS*self.ORBITAL_PERIODS['venus'])
        return round(years, 2)

    def on_mars(self):
        years = self.seconds/(self.EARTH_SECONDS*self.ORBITAL_PERIODS['mars'])
        return round(years, 2)
        
    def on_jupiter(self):
        years = self.seconds/(self.EARTH_SECONDS*self.ORBITAL_PERIODS['jupiter'])
        return round(years, 2)

    def on_saturn(self):
        years = self.seconds/(self.EARTH_SECONDS*self.ORBITAL_PERIODS['saturn'])
        return round(years, 2)
        
    def on_uranus(self):
        years = self.seconds/(self.EARTH_SECONDS*self.ORBITAL_PERIODS['uranus'])
        return round(years, 2)
        
    def on_neptune(self):
        years = self.seconds/(self.EARTH_SECONDS*self.ORBITAL_PERIODS['neptune'])
        return round(years, 2)
        