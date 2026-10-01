const fs = require('fs');
const js = fs.readFileSync('chunk_1.js', 'utf8');

// Find event with 14f42098-623f-4752-7933-18a5630eb7b7
const pos = js.indexOf('14f42098-623f-4752-7933-18a5630eb7b7');
console.log('Context around 14f42098:');
console.log(js.substring(pos - 300, pos + 1200));

// Find actionListId for this event
const eventSnippet = js.substring(pos - 300, pos + 500);
const actionListMatch = eventSnippet.match(/actionListId:"([^"]+)"/);
if (actionListMatch) {
  const actionListId = actionListMatch[1];
  console.log('\nFound Action List ID:', actionListId);
  
  // Find actionList definition
  const alPos = js.indexOf(`"${actionListId}":`);
  if (alPos !== -1) {
    console.log('\nAction List definition:');
    console.log(js.substring(alPos, alPos + 3500));
  }
}
