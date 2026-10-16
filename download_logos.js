const fs = require('fs');
const https = require('https');

const urls = {
  'tvs': 'https://upload.wikimedia.org/wikipedia/commons/4/4b/TVS_Motor_Company_Logo.svg',
  'hero': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Hero_MotoCorp_Logo.svg',
  'bajaj': 'https://upload.wikimedia.org/wikipedia/commons/7/77/Bajaj_Auto_logo.svg',
  'royalenfield': 'https://upload.wikimedia.org/wikipedia/commons/1/14/Royal_Enfield_logo.svg',
  'yamaha': 'https://upload.wikimedia.org/wikipedia/commons/0/0b/Yamaha_Motor_Logo.svg',
  'honda': 'https://upload.wikimedia.org/wikipedia/commons/a/af/Honda_logo_text.svg',
  'ktm': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/KTM_logo.svg',
  'suzuki': 'https://upload.wikimedia.org/wikipedia/commons/1/12/Suzuki_logo_2.svg',
  'kawasaki': 'https://upload.wikimedia.org/wikipedia/commons/a/ab/Kawasaki_logo_2021.svg',
  'bmw': 'https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg',
  'triumph': 'https://upload.wikimedia.org/wikipedia/commons/8/87/Triumph_Motorcycles_logo.svg',
  'jawa': 'https://upload.wikimedia.org/wikipedia/commons/3/30/Jawa_Motors_Logo.svg'
};

const options = {
  headers: {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
  }
};

async function download() {
  for (const brand of Object.keys(urls)) {
    const url = urls[brand];
    console.log(`Downloading ${brand}...`);
    await new Promise((resolve) => {
      https.get(url, options, (res) => {
        if (res.statusCode === 301 || res.statusCode === 302) {
            https.get(res.headers.location, options, (res2) => {
                let data = '';
                res2.on('data', chunk => data += chunk);
                res2.on('end', () => {
                  fs.writeFileSync(`assets/brands/${brand}.svg`, data);
                  console.log(`Saved ${brand}`);
                  setTimeout(resolve, 500);
                });
            });
        } else {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => {
              fs.writeFileSync(`assets/brands/${brand}.svg`, data);
              console.log(`Saved ${brand}`);
              setTimeout(resolve, 500);
            });
        }
      });
    });
  }
}
download();
