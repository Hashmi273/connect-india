const fs = require('fs');
const js = fs.readFileSync('chunk_1.js', 'utf8');

const alPos = js.indexOf('"a-3":');
// Let's find the next action list
const nextAl = js.indexOf('"a-', alPos + 6);
const a3str = js.substring(alPos, nextAl !== -1 ? nextAl : alPos + 15000);
fs.writeFileSync('a3_full.txt', a3str);

// Let's format and print the action items
const data = eval('({' + a3str + '})');
console.log('Action List Title:', data['a-3'].title);
const groups = data['a-3'].continuousParameterGroups[0].continuousActionGroups;
groups.forEach(g => {
  console.log(`\n=== Keyframe ${g.keyframe}% ===`);
  g.actionItems.forEach(item => {
    console.log(`  - Type: ${item.actionTypeId}, Target: ${item.config.target ? item.config.target.selector : 'none'}, Values:`, {
      xValue: item.config.xValue,
      yValue: item.config.yValue,
      xUnit: item.config.xUnit,
      yUnit: item.config.yUnit,
      heightValue: item.config.heightValue,
      heightUnit: item.config.heightUnit,
      value: item.config.value
    });
  });
});
