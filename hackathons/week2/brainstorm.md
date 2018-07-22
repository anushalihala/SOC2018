## Boggle Solver

#### Challenge
> Write a boggle solver that finds all possible words on a given board.
You should pick a fixed vocabulary (dictionary): Hasbro standard English dictionary.


#### Tasks
1. **How do we pick a fixed vocabulary?**
  - Do we load a local dictionary (from a file for example) into memory?
  By either implementing our own using a [trie][1], or using an existing python module to handle this task for us?
  - Do we use an external online service (API)? If so, how do we handle service non availability (or errors)?

2. **Dice distribution?**
  - randomly generated? Any ideas on how to do this efficiently enough, and still generate evenly distributed 16 letters?

3. **Main algorithm: given 16 letters, how do we find all possible words on a given board?**
  - Do we try out all possible combinations and check them against the dictionary? This implies all possible combinations of length 2, of length 3, of length 4... of length 16.
  - Is there a way to do this more efficiently?

4. **[What is the MOST number of points possible in boggle?][2]**
  - What does this question mean?



[1]: https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014
[2]: https://github.com/1millionwomentotech/toolkitten/blob/master/summer-of-code/week-02/wk2-hackathon-submissions/hackathon-challenge-boggle-solver.md
