const https = require('https');
const fs = require('fs');

https.get('https://www.eventbeds.com/', (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    fs.writeFileSync('eventbeds_raw.html', data);
    console.log('Saved raw HTML, size:', data.length);
    
    // search for discover section
    const idx = data.indexOf('discover');
    console.log('first discover idx:', idx);
    
    // let's find all sections
    const sections = data.match(/<section[\s\S]*?<\/section>/gi) || [];
    console.log('Total sections:', sections.length);
    sections.forEach((s, i) => {
      const classMatch = s.match(/class="([^"]*)"/i);
      console.log(`Section ${i}:`, classMatch ? classMatch[1] : 'no class', 'length:', s.length);
    });
  });
});
