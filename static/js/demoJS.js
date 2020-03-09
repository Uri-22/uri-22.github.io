//GET https://api.yelp.com/v3/businesses/search'
npm install yelp-api --save


const yelp = require('yelp-fusion');
const client = yelp.client('QN_uM4CAc1AbjmqtBpQBA_2ZR2J46EGpHSznTbPsWzljGUPuOZV1XjAHwrzrhru4sHHWi4u14PJ-vEF1UcG3QFKD232RiW7HsNMIzqMYe-wSlnONbJWZ-92EQKxdXnYx');

client.search({
  term: 'Four Barrel Coffee',
  location: 'san francisco, ca',
}).then(response => {
  console.log(response.jsonBody.businesses[0].name);
}).catch(e => {
  console.log(e);
});


