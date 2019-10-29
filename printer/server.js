const express = require("express");
const ejs = require('ejs');
const path = require('path');
const logger = require('morgan');
const request = require('request');
const cors = require('cors');
const fs = require("fs");
const printer = require("pdf-to-printer");
const fetch = require("node-fetch");

// const print = require("./src/print");
const list = require("./src/list");
//put your printer here
const options = {
  printer: "HP-LaserJet-M1522nf-MFP-2"
};

const app = express();
app.use(cors());
app.use(logger('dev'));
app.set('view engine', 'ejs');
app.use(express.static(path.join(__dirname, 'public')))
app.set('views', path.join(__dirname, 'views'))
app.use(express.json());

app.get('/', (req,res,next) => res.render('home'));

app.post('/request', (req, res, next) => {
    console.log('body',req.body)
    const pdfPath = path.join(__dirname, "./" + randomString() + ".pdf");
    request({
        url: 'http://127.0.0.1:5000/api/v1/generate-pdf-receipt',
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(req.body)
    }).pipe(fs.createWriteStream(pdfPath)).on('finish', function(){
      console.log('end writing')
        printer
          .print(pdfPath, options)
          .then(onSuccess)
          .catch(onError)
          .finally(() => remove(pdfPath));
    })

    function onSuccess() {
      res.send({ status: "completed" });
    }
    
    
    function onError(error) {
      res.send({ status: "error", error });
    }
})

app.get("/print", print);

app.get("/list", list);

const port = 8080;

app.listen(port, () => console.log(`http://localhost:${port}.`));

function onSuccess() {
  response.send({ status: "completed" });
}


function onError(error) {
  response.send({ status: "error", error });
}

function print(request, response) {
    function onSuccess() {
      response.send({ status: "completed" });
    }
  
    function onError(error) {
      response.send({ status: "error", error });
    }
  
    fetch(request.query.url)
      .then(res => res.buffer())
      .then(buffer => {
        const pdf = save(buffer);
  
        printer
          .print(pdf)
          .then(onSuccess)
          .catch(onError)
          .finally(() => remove(pdf));
      });
  }
  
  function save(buffer) {
    const pdfPath = path.join(__dirname, "./" + randomString() + ".pdf");
    fs.writeFileSync(pdfPath, buffer, "binary");
    return pdfPath;
  }
  
  function remove(pdf) {
    fs.unlinkSync(pdf);
  }
  
  function randomString() {
    return Math.random()
      .toString(36)
      .substring(7);
  }