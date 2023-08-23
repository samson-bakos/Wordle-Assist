# Wordle-Assist

## [Try it here!](https://wordle-cheater.streamlit.app)

A project created because my fiance is better at Wordle than I am. 

This project predicts the most statistically probable solution to a Wordle puzzle, taking user input at each step.

It can be used in one of two ways:

* If a user is stuck, they can enter their guesses and recieve the best word recommendation
* A user can use the recommended words for each guess, resulting in the lowest possible average score (3.44 guesses on average, compared to the global user average of 4.02)

## Using the App

Load it up using the link above! If the app has not been opened by a user in some time, it may be necessary to wait a few moments for it to be redeployed by Streamlit.

You can load up the [official daily wordle](https://www.nytimes.com/games/wordle/index.html) or play an [unlimited puzzle](https://wordlegame.org).

The app sidebar provides an explanation of how to use the app to solve your wordle puzzle.

## How It Works:

This implementation uses a higher variance approach to solving the puzzle because I wanted to optimize the probability of 2 and 3 step solves. For reference, this implementation has an observed 2 step solve rate of 5% and a mean solve rate of 3.44 and the theoretically optimal information theory based approach has a two step solve rate of 3.45%, and a mean solve rate of 3.42. This approach has a slightly higher expected value, but is more likely to solve the puzzle quickly. 

Generally, this solution focuses on achieving the optimal number of 'greens' -- correct letter in the correct place -- as it finds probabilities for each word in each column seperately.

The algorithm initializes by loading a list of all possible wordle solutions. 

A word's score is calculated as a product of probabilities -- akin to a likelihood. Each letter's probability in a column is computed as the number of remaining words that have that letter in that position, divided by the total number of remaining words. Each word's overall score is then determined as the product of these probabilities. This is the theoretical probability of the solution being that word in an independent, unbounded solution space (all combinations of letters are valid possibilities, and each column's outcome is indepedent). However, because the actual probabilities used are derived from the limited solution space only (valid words), this should correspond to the most "likely" solution in the limited space as well. The word that is recommended by the algorithm is one with the highest likelihood score.

As discussed above, it is possible to take an information theory approach that treats the columns as non independent -- focusing on guessing letters that provide information on the puzzle as a whole, rather than just that column. This is also somewhat accomplished by this algorithm, as it is reasonable to say that a letter being common in a given column means it is likely common in other columns as well, meaning it has a provides a high probability of being yellow, or else yields more information when it is found to be grey. However, this puzzle does not necessarily provide the optimal solution under this approach, though the empirical difference is extremely minor. 

Letters with duplicate letters are handled in a way that respects this information based approach. Because recommending words with duplicate letters is likely under the independent column approach (i.e. 'e' is probability high probability in many columns), but does not yield as much information when guessed multiple times, letters with repeat letters are penalized and are generally only recommended when solutions with all unique letters are exhausted. 




