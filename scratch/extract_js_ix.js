const https = require('https');
const fs = require('fs');

const jsUrl = 'https://cdn.prod.website-files.com/64d9d44b74f7cd98eec10d8d/js/webflow.006fd696.c496db9787624813.js';

https.get(jsUrl, (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    fs.writeFileSync('webflow_main.js', data);
    console.log('Saved JS, size:', data.length);
    
    const pos = data.indexOf('14f42098-623f-4752-7933-18a5630eb7b7');
    console.log('Found 14f42098 in JS at:', pos);
    
    // search for discovery-mobile or discover
    const regex = /"actionTypeId"[^}]*"discovery-mobile[^}]*/gi;
    const matches = data.match(regex) || [];
    console.log('Matches:', matches.length);
    
    // Find action list that animates discovery-mobile
    const ixIdx = data.indexOf('discovery-mobile');
    console.log('first discovery-mobile in JS at:', ixIdx);
    if (ixIdx !== -1) {
      console.log(data.substring(ixIdx - 200, ixIdx + 800));
    }
  });
});
