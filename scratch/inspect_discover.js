const fs = require('fs');
const html = fs.readFileSync('eventbeds_raw.html', 'utf8');

// Find all CSS links
const cssMatches = [...html.matchAll(/<link[^>]+href="([^"]+\.css[^"]*)"/gi)];
console.log('CSS Links:');
cssMatches.forEach(m => console.log(m[1]));

// Find all JS links
const jsMatches = [...html.matchAll(/<script[^>]+src="([^"]+\.js[^"]*)"/gi)];
console.log('\nJS Links:');
jsMatches.forEach(m => console.log(m[1]));

// Print section 4 & 5
const sections = html.match(/<section[\s\S]*?<\/section>/gi) || [];
console.log('\n--- Section 4 (static-discover-sc) ---');
console.log(sections[4]);
console.log('\n--- Section 5 (discover-sc) ---');
console.log(sections[5]);
