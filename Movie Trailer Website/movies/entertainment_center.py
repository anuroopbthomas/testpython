import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
inception = media.Movie("Inception", "Dream layers", "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", "https://www.youtube.com/watch?v=YoHD9XEInc0")

movies = [toy_story, avatar, inception]
#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__module__)
print(media.Movie.VALID_RATINGS)
#print(avatar.storyline)
#inception.show_trailer()
#avatar.show_trailer()
#print(toy_story.storyline)
