const fs = require('fs');
const html = fs.readFileSync('eventbeds_raw.html', 'utf8');
const links = html.match(/href="([^"]+css[^"]*)"/gi);
console.log(links);
