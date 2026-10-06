const https = require('https');
const fs = require('fs');

const urls = [
  'https://cdn.prod.website-files.com/64d9d44b74f7cd98eec10d8d/js/webflow.schunk.36b8fb49256177c8.js',
  'https://cdn.prod.website-files.com/64d9d44b74f7cd98eec10d8d/js/webflow.schunk.3e07cc2213a3ca1f.js'
];

urls.forEach((url, i) => {
  https.get(url, (res) => {
    let data = '';
    res.on('data', chunk => data += chunk);
    res.on('end', () => {
      console.log(`URL ${i} size:`, data.length);
      const pos = data.indexOf('14f42098-623f-4752-7933-18a5630eb7b7');
      console.log(`URL ${i} pos of 14f42098:`, pos);
      if (pos !== -1) {
        fs.writeFileSync(`chunk_${i}.js`, data);
        console.log(`Saved chunk_${i}.js`);
      }
      const discPos = data.indexOf('discovery-mobile');
      console.log(`URL ${i} pos of discovery-mobile:`, discPos);
      if (discPos !== -1) {
        console.log(data.substring(discPos - 200, discPos + 600));
      }
    });
  });
});
