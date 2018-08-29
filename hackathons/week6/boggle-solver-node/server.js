'use strict';

let path = require('path');
let express = require('express');

// create express application
const app = express();

// define port
const port = process.env.PORT || 8484;
app.listen(port, () => {
    console.log(`http://localhost:${port}`)
});

// define template engine for our application
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

// define routing for our application
let index = require('./routes/index');
let benchmark = require('./routes/benchmark');
app.use('/', index);
app.use('/benchmark', benchmark);

// add favicon
app.use('/favicon.ico', express.static('images/favicon.ico'));