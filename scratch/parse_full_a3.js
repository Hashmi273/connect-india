const fs = require('fs');
const js = fs.readFileSync('chunk_1.js', 'utf8');

const alPos = js.indexOf('"a-3":{');
let depth = 0;
let endPos = alPos;
for (let i = alPos + 5; i < js.length; i++) {
  if (js[i] === '{') depth++;
  else if (js[i] === '}') {
    depth--;
    if (depth === 0) {
      endPos = i + 1;
      break;
    }
  }
}

const fullObjStr = '({' + js.substring(alPos, endPos) + '})';
fs.writeFileSync('full_a3.js', fullObjStr);
const obj = eval(fullObjStr)['a-3'];

console.log('Animation Title:', obj.title);
obj.continuousParameterGroups[0].continuousActionGroups.forEach(g => {
  console.log(`\n================ Keyframe ${g.keyframe}% ================`);
  g.actionItems.forEach(item => {
    const sel = item.config.target ? item.config.target.selector : 'unknown';
    console.log(`  [${item.actionTypeId}] ${sel}:`, {
      x: item.config.xValue,
      y: item.config.yValue,
      xUnit: item.config.xUnit,
      yUnit: item.config.yUnit,
      h: item.config.heightValue,
      hUnit: item.config.heightUnit,
      scaleX: item.config.xValue,
      scaleY: item.config.yValue,
      opacity: item.config.value
    });
  });
});
