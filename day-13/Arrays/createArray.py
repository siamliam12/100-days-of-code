dvd_collections = [None] * 15

class DVD:
    def __init__(self,name,release_year,director):
        self.name = name
        self.release_year = release_year
        self.director = director

    def __str__(self):
        return f"{self.name} ,directed by {self.director}, released in {self.release_year}"
    
dvd_collections[7] = DVD("The Avengers", 2012, "Joss Whedon")
dvd_collections[3] = DVD("The Incredibles", 2004, "Brad Bird")
dvd_collections[9] = DVD("Finding Dory", 2016, "Andrew Stanton")
dvd_collections[2] = DVD("The Lion King", 2019, "Jon Favreau")

print(dvd_collections[2])