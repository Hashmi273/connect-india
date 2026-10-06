const fs = require('fs');
const html = fs.readFileSync('eventbeds_raw.html', 'utf8');

// Find the data-ix2 object
const ix2Match = html.match(/<html[^>]*data-wf-page="([^"]*)"/i);
console.log('Page ID:', ix2Match ? ix2Match[1] : 'none');

// Find JSON script containing webflow interaction definitions
const scripts = html.match(/<script[^>]*>([\s\S]*?)<\/script>/gi) || [];
scripts.forEach((s, idx) => {
  if (s.includes('14f42098-623f-4752-7933-18a5630eb7b7') || s.includes('discover-sc') || s.includes('mobiles-block')) {
    console.log(`Script ${idx} contains discover interaction:`);
    fs.writeFileSync('discover_interaction.json', s);
    console.log('Saved interaction script');
  }
});

// Let's also search in the entire html for the animation data
const matchAllIX = [...html.matchAll(/"actionTypeId":"[^"]*"[\s\S]*?"id":"14f42098-623f-4752-7933-18a5630eb7b7"/gi)];
console.log('IX matches count:', matchAllIX.length);
