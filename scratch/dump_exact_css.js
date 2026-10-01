const fs = require('fs');
const css = fs.readFileSync('eventbeds_shared.css', 'utf8');

const classNames = [
  'discover-sc', 'discover-subhead', 'discover-height', 'discover-sticky',
  'discover-s', 'discovery-content', 'discover-header-block',
  'mobiles-block', 'discovery-mobile', 'down-position-block', 'down-text-block'
];

classNames.forEach(cls => {
  const regex = new RegExp(`\\.${cls}[^{]*\\{[^}]*\\}`, 'g');
  const matches = css.match(regex) || [];
  console.log(`\n=== .${cls} (${matches.length} rules) ===`);
  matches.forEach(m => console.log(m));
});
