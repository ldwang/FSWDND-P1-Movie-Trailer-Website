import fresh_tomatoes
import media

# Movie class instances
the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "Two imprisoned men bond over a number of years, finding solace and eventual"
                                       " redemption through acts of common decency.",
                                       "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # NOQA
                                       "https://www.youtube.com/watch?v=6hB3S9bIaco")

the_dark_knight = media.Movie("The Dark Knight",
                              "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham,"
                              " the caped crusader must come to terms with one of the greatest psychological tests of "
                              "his ability to fight injustice",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                              "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

interstella = media.Movie("Interstella",
                          "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's "
                          "survival.",
                          "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                          "https://www.youtube.com/watch?v=0vxOhd4qlnA")

gone_with_the_wind = media.Movie("Gone With the Wind",
                                 "A manipulative Southern belle carries on a turbulent affair with a blockade runner "
                                 "during the American Civil War.",
                                 "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Poster_-_Gone_With_the_Wind_01.jpg/330px-Poster_-_Gone_With_the_Wind_01.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=8mM8iNarcRc")

inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use of dream-sharing technology, is given the "
                        "inverse task of planting an idea into the mind of a CEO.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# the list of movie objects
movies = [gone_with_the_wind, toy_story, the_dark_knight, interstella, inception, the_shawshank_redemption]

# execute the function to generate HTML file and open it in browser
fresh_tomatoes.open_movies_page(movies)
