const fs = require('fs');
const html = fs.readFileSync('eventbeds_raw.html', 'utf8');

const pos = html.indexOf('14f42098-623f-4752-7933-18a5630eb7b7');
while (pos !== -1) {
  console.log('Found at pos:', pos);
  console.log(html.substring(Math.max(0, pos - 100), Math.min(html.length, pos + 300)));
  break;
}

// Let's search for "discovery-mobile" or "mobiles-block" or "Easy search" in html
const ixMatches = html.match(/"events":\s*\{[\s\S]*?\}\s*,\s*"actionLists"/);
if (ixMatches) {
  console.log('Found IX events!');
}

const actionListsMatch = html.match(/"actionLists":\s*\{[\s\S]*?\}\s*,\s*"site"/);
if (actionListsMatch) {
  console.log('Found actionLists!');
  fs.writeFileSync('actionLists.json', actionListsMatch[0]);
}
