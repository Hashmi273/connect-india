const https = require('https');
const fs = require('fs');

const cssUrl = 'https://cdn.prod.website-files.com/64d9d44b74f7cd98eec10d8d/css/eventbeds-dev.webflow.shared.f56536f20.min.css';

https.get(cssUrl, (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    fs.writeFileSync('eventbeds_shared.css', data);
    console.log('Saved CSS, size:', data.length);
    
    // search for discover rules
    const matches = data.match(/[^\{\}]*discover[^\{\}]*\{[^}]*\}/gi) || [];
    console.log('Discover CSS rules count:', matches.length);
    matches.forEach(m => console.log(m));
  });
});

// Also search for discover interactions in HTML
const html = fs.readFileSync('eventbeds_raw.html', 'utf8');
const wId = '14f42098-623f-4752-7933-18a5630eb7b7'; // discover-sc id
console.log('\nSearching for interaction with id:', wId);
const ix2Match = html.match(new RegExp(`"${wId}"[\\s\\S]*?\\}`, 'g'));
console.log('ix2 match in html:', ix2Match ? ix2Match.length : 'none');
