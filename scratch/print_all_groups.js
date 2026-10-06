const fs = require('fs');
const js = fs.readFileSync('full_a3.js', 'utf8');
const obj = eval(js)['a-3'];
const groups = obj.continuousParameterGroups[0].continuousActionGroups;
console.log('All keyframe percentages:', groups.map(g => g.keyframe));

groups.forEach(g => {
  console.log(`\n================ Keyframe ${g.keyframe}% ================`);
  g.actionItems.forEach(item => {
    console.log(item);
  });
});
