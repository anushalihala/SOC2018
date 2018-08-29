## Boggle Solver Challenge - NodeJS Version

[![NodeJS Runtime](https://img.shields.io/badge/JavaScript%20Runtime-NodeJS-43853D.svg)][1]
[![ExpressJS Framework](https://img.shields.io/badge/Framework-ExpressJS-85929E.svg)][2]
[![Pug Template Engine](https://img.shields.io/badge/Template%20Engine-PugJS-A86454.svg)][3]


### Context

> Write a [boggle solver][4] that finds all possible words on a given board.


### Frameworks - Libraries - Resources

- [NodeJS][1]
- [ExpressJS][2]
- [PugJS][3]
- [Boggle dictionary][5]

### Content

This NodeJS version of the Boggle solver contains the following folders and files:

- the **`server.js` file** contains our NodeJS server application definition

- the **`images` folder** contains the application `favicon` image

- the **`views` folder** contains template files and their `HTML` compiled versions:
    - `index.pug`: the index (default) application template
    - `pending.pug`: a temporary page displayed while benchmarking the application
    - `benchmark.pug`: a template to display the application benchmark results

- the **`routes` folder** contains:
    - `index.js`: module that handles default `GET` requests to the server
    - `benchmark.js`: module that handles `GET` requests to the *benchmark resources*

- in the **`solver` folder**:
    - `Main.js`: the main application class to get the boggle solver started
    - `Solver.js`: class that implements a boggle game solver
    - `Board.js`: class that randomly generates a boggle board
    - `Dictionary.js`: class to implement the boggle dictionary using a trie
    - `Trienode.js`: a javascript class that represents a trie node
    - `dictionary.txt`: the dictionary text file used for this project

### Setup and Run Instructions

**Prerequisites:**
- Download and install the latest [Long Term Support version of NodeJS][6] for your platform.
- This will automatically install the [`npm`][7] JavaScript package manager as well.

**To run the program:**
- Download this `boggle-solver-node` folder (unzip it if necessary), and navigate into it via a command line window.
- Run the `npm install` command, then start the NodeJS server with the `npm start` command.
- The application will be available at the `http:localhost:8484` address.
- To display benchmark results, go to `http:localhost:8484/benchmark` in your favorite web browser.


[1]: https://nodejs.org/en/
[2]: https://expressjs.com/
[3]: https://pugjs.org/api/getting-started.html
[4]: https://github.com/1millionwomentotech/toolkitten/blob/master/summer-of-code/week-02/wk2-hackathon-submissions/hackathon-challenge-boggle-solver.md
[5]: https://raw.githubusercontent.com/jonbcard/scrabble-bot/master/src/dictionary.txt
[6]: https://nodejs.org/en/download/
[7]: https://www.npmjs.com/