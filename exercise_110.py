# Movie Ratings!

#  As a user I should be able to ask the user for the a rating, and receive back the appropriate response:

# check for rating for this movie:
  ## universal -> everyone can watch
  ## pg --> General viewing, but some scenes may be unsuitable for young children
  ## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
  ## 15 --> No one younger than 15 may see a 15 film in a cinema.
  ## 18 --> No one younger than 18 may see an 18 film in a cinema.

while True:
    print('Hint: If you want to exit at all then type exit')
    print("What rating are you curious about?")
    movie_rating = str(input('please input your movie rating (Universal, pg, 12, 15 or 18): '.lower()))
    if movie_rating == 'universal':
        print('UNIVERSAL: Everyone can watch.')
    elif movie_rating == 'pg':
        print('PG: General viewing, but some scenes may be unsuitable for young children.')
    elif movie_rating == '12':
        print('''12: Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12.
         No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.''')
    elif movie_rating == '15':
        print('15: No one younger than 15 may see a 15 film in a cinema.')
    elif movie_rating == '18':
        print('18: No one younger than 18 may see an 18 film in a cinema.')
    elif movie_rating == 'exit':
        break
