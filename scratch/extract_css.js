const https = require('https');
const fs = require('fs');

const cssUrl = 'https://cdn.prod.website-files.com/64d9d44b74f7cd98eec10d8d/css/eventbeds.webflow.33fdf399c.min.css';

https.get(cssUrl, (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    fs.writeFileSync('eventbeds.css', data);
    console.log('Saved CSS, size:', data.length);
    
    // search for discover rules
    const matches = data.match(/[^{}]*discover[^{}]*\{[^}]*\}/gi) || [];
    console.log('Discover CSS rules count:', matches.length);
    matches.forEach(m => console.log(m));
  });
});
