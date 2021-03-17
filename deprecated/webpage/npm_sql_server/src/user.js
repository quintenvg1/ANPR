const express = require('express');

function createRouter(db) {
  const router = express.Router();
  //const owner = '';

  // the routes are defined here
  router.post('/user', (req, res, next) => {
    db.query(
      'INSERT INTO user (naam, paswoord, nummerplaat) VALUES (?,?,?)',
      [(req.body.naam, req.body.paswoord, req.body.nummerplaat)],
      (error) => {
        if (error) {
          console.error(error);
          res.status(500).json({status: 'error'});
        } else {
          res.status(200).json({status: 'ok'});
        }
      }
    );
  });

  router.get('/user', function (req, res, next) {
    db.query(
      'SELECT ID, naam, nummerplaat WHERE nummerplaat=? ',
      [(req.body.nummerplaat)],
      (error, results) => {
        if (error) {
          console.log(error);
          res.status(500).json({status: 'error'});
        } else {
          res.status(200).json(results);
        }
      }
    );
  });

  router.put('/user/:ID', function (req, res, next) {
  db.query(
    'UPDATE user SET naam=?, paswoord=?, nummerplaat=? WHERE ID=? AND naam=?',
    [req.body.naam, req.body.paswoord, req.params.id, user],
    (error) => {
      if (error) {
        res.status(500).json({status: 'error'});
      } else {
        res.status(200).json({status: 'ok'});
      }
    }
  );
});

router.delete('/user/:ID', function (req, res, next) {
  db.query(
    'DELETE FROM user WHERE naam=? AND paswoord=?',
    [req.params.naam, req.body.paswoord],
    (error) => {
      if (error) {
        res.status(500).json({status: 'error'});
      } else {
        res.status(200).json({status: 'ok'});
      }
    }
  );
});

  return router;
}

module.exports = createRouter;