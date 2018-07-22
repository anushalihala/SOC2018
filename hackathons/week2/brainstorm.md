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

2. **Dice distribution?**
  - randomly generated? Any ideas on how to do this efficiently enough, and still generate evenly distributed 16 letters?

Anusha: Honestly I'm rather confused here. A couple of points to address;
  - When creating a die how do we assign it alphabets? Do we randomly choose 6 numbers from 1 to 26?
  - how many different types dice would be there? Would they be assigned to board positions randomly?
About the board;
  - Do we have to differentiate between a board creation and a board shuffle?
    => Like I guess the different types of die would remain the same during a shuffle but not on different board creations. 
    Also for a shuffle do the dices change position on the board? (I dont know much about Boggle haha)

3. **Main algorithm: given 16 letters, how do we find all possible words on a given board?**
  - Do we try out all possible combinations and check them against the dictionary? This implies all possible combinations of length 2, of length 3, of length 4... of length 16.
  - Is there a way to do this more efficiently?
  
Anusha: I dont think it would be a case of all combinations of letters.. So once we have our dictionary in a trie structure, 
we'll just traverse down paths which are valid words. We would have to start at each of the 16 positions though, and find a way to
get all the neighbours that aren't part of the word yet

4. **[What is the MOST number of points possible in boggle?][2]**
  - What does this question mean?
  
Anusha: I've no idea

### Possible components

- Dictionary resource into trie
..- Parse dictionary
..- Add words to Trie
- Generate board
..- Create die
..- Populate board
- Given board, find all valid words
- Calculate points

#### References
[1]: https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014
[2]: https://github.com/1millionwomentotech/toolkitten/blob/master/summer-of-code/week-02/wk2-hackathon-submissions/hackathon-challenge-boggle-solver.md