const fs = require('fs');
const js = fs.readFileSync('chunk_1.js', 'utf8');

const alPos = js.indexOf('"a-3":');
// Let's parse until "a-4" or end of action list
const endPos = js.indexOf('"a-4":', alPos);
const actionListStr = js.substring(alPos, endPos !== -1 ? endPos : alPos + 10000);

// Print all continuousActionGroups
const kfRegex = /keyframe:(\d+),actionItems:\[([\s\S]*?)\]\}/g;
let match;
while ((match = kfRegex.exec(actionListStr)) !== null) {
  const kf = match[1];
  console.log(`\n================ KEYFRAME ${kf}% ================`);
  const items = match[2];
  const itemRegex = /actionTypeId:"([^"]+)",config:\{([^}]+target:\{[^}]+\}[^}]*)\}/g;
  let itemMatch;
  while ((itemMatch = itemRegex.exec(items)) !== null) {
    console.log(`  Action: ${itemMatch[1]}`);
    console.log(`  Config: ${itemMatch[2]}`);
  }
}
