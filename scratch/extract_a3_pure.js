const fs = require('fs');
const js = fs.readFileSync('chunk_1.js', 'utf8');

const alPos = js.indexOf('"a-3":{');
console.log('alPos:', alPos);

// Count braces to find matching close brace
let depth = 0;
let endPos = alPos;
for (let i = alPos + 6; i < js.length; i++) {
  if (js[i] === '{') depth++;
  else if (js[i] === '}') {
    if (depth === 0) {
      endPos = i + 1;
      break;
    }
    depth--;
  }
}

console.log('endPos:', endPos, 'length:', endPos - alPos);
const jsonStr = js.substring(alPos + 6, endPos);
fs.writeFileSync('a3_pure.json', jsonStr);

const obj = eval('(' + jsonStr + ')');
console.log('Title:', obj.title);
obj.continuousParameterGroups[0].continuousActionGroups.forEach(g => {
  console.log(`\n=== Keyframe ${g.keyframe}% ===`);
  g.actionItems.forEach(item => {
    console.log(`  - Type: ${item.actionTypeId}, Selector: ${item.config.target ? item.config.target.selector : 'none'}, Conf:`, {
      x: item.config.xValue,
      y: item.config.yValue,
      xUnit: item.config.xUnit,
      yUnit: item.config.yUnit,
      h: item.config.heightValue,
      hUnit: item.config.heightUnit,
      val: item.config.value
    });
  });
});
