const fs = require('fs');
const js = fs.readFileSync('chunk_1.js', 'utf8');

const alPos = js.indexOf('"a-3":');
const endPos = js.indexOf('"a-4":', alPos);
fs.writeFileSync('a3_full.json', js.substring(alPos, endPos));
console.log('Saved a3_full.json, length:', (endPos - alPos));
