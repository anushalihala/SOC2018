## Boggle Solver

#### Challenge
> Write a boggle solver that finds all possible words on a given board.
You should pick a fixed vocabulary (dictionary): Hasbro standard English dictionary.


#### Tasks
1. **How do we pick a fixed vocabulary?**
  - Do we load a local dictionary (from a file for example) into memory?
  By either implementing our own using a [trie][1], or using an existing python module to handle this task for us?

Anusha: Implementing it on our own might be more thorough and fun :) If we get short on time though, we could use a module. I dont know of any though..

  - Do we use an external online service (API)? If so, how do we handle service non availability (or errors)?

Anusha: I dont think its required for the exercise. After we're done with it perhaps we could extend it with the service (like beyond this week)

Lisa: Make our own dictionary?

*Dictionary to be used - https://raw.githubusercontent.com/jonbcard/scrabble-bot/master/src/dictionary.txt* 

2. **Dice distribution?**
  - randomly generated? Any ideas on how to do this efficiently enough, and still generate evenly distributed 16 letters?

Anusha: Honestly I'm rather confused here. A couple of points to address;
  - When creating a die how do we assign it alphabets? Do we randomly choose 6 numbers from 1 to 26?
  - how many different types dice would be there? Would they be assigned to board positions randomly?
  
About the board;
  - Do we have to differentiate between a board creation and a board shuffle?
    => Like I guess the different types of die would remain the same during a shuffle but not on different board creations. 
    Also for a shuffle do the dices change position on the board? (I dont know much about Boggle haha)
    
LISA: I FOUND THIS for THE DICE LETTERS. 
https://boardgames.stackexchange.com/questions/29264/boggle-what-is-the-dice-configuration-for-boggle-in-various-languages

*Dice Distribution - Use the New Version: https://www.boardgamegeek.com/thread/300565/review-boggle-veteran-and-beware-different-version*

3. **Main algorithm: given 16 letters, how do we find all possible words on a given board?**
  - Do we try out all possible combinations and check them against the dictionary? This implies all possible combinations of length 2, of length 3, of length 4... of length 16.
  - Is there a way to do this more efficiently?
  
Anusha: I dont think it would be a case of all combinations of letters.. So once we have our dictionary in a trie structure, 
we'll just traverse down paths which are valid words. We would have to start at each of the 16 positions though, and find a way to
get all the neighbours that aren't part of the word yet

4. **[What is the MOST number of points possible in boggle?][2]**
  - What does this question mean?
  
  Lisa: depending on how long the word is, it's worth a certain amount of points.
  
1 and 2 letter words = 0 points 3 letter words = 1 point 4 letter words = 2 points 5 letter words = 3 points
The longest possible word 16 letter word = 14 points

Anusha: I've no idea

#### Possible components

- Dictionary resource into trie
  * Parse dictionary
  * Add words to Trie
- Generate board
  * Create die
  * Populate board
- Given board, find all valid words
- Calculate points
-timer (3 min)

#### Submission guidlines
Your code should return an object in the following format:

```
result = {
    "score": 143,
    "words": [ "" , "", "", "", ... , ""]
}
```

Where there are two key-value pairs. The first pair has key = "score", and the value should be an integer. The second par has key = "words", and the value should be an alphabetically SORTED list of words.

#### References

[1]: https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014
[2]: https://github.com/1millionwomentotech/toolkitten/blob/master/summer-of-code/week-02/wk2-hackathon-submissions/hackathon-challenge-boggle-solver.md
