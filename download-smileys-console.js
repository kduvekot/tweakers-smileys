// Tweakers Smiley Downloader - Browser Console Script
// Copy and paste this entire script into Chrome DevTools Console while logged into Tweakers.net
// The script will download all smileys as a zip file

(async function() {
    console.log('🎨 Tweakers Smiley Downloader Starting...');

    // Load JSZip library dynamically
    if (typeof JSZip === 'undefined') {
        console.log('📦 Loading JSZip library...');
        const script = document.createElement('script');
        script.src = 'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js';
        document.head.appendChild(script);

        await new Promise((resolve, reject) => {
            script.onload = resolve;
            script.onerror = reject;
        });
        console.log('✅ JSZip loaded successfully');
    }

    // All Tweakers smileys with their filenames and URLs
    const smileys = [
        { filename: 'smile.svg', url: 'https://tweakers.net/g/s/smile.svg' },
        { filename: 'frown.svg', url: 'https://tweakers.net/g/s/frown.svg' },
        { filename: 'unhappy.svg', url: 'https://tweakers.net/g/s/unhappy.svg' },
        { filename: 'wink.svg', url: 'https://tweakers.net/g/s/wink.svg' },
        { filename: 'devil.svg', url: 'https://tweakers.net/g/s/devil.svg' },
        { filename: 'puh.svg', url: 'https://tweakers.net/g/s/puh.svg' },
        { filename: 'puh2.svg', url: 'https://tweakers.net/g/s/puh2.svg' },
        { filename: 'yummie.svg', url: 'https://tweakers.net/g/s/yummie.svg' },
        { filename: 'redface.svg', url: 'https://tweakers.net/g/s/redface.svg' },
        { filename: 'shiny.svg', url: 'https://tweakers.net/g/s/shiny.svg' },
        { filename: 'cry.svg', url: 'https://tweakers.net/g/s/cry.svg' },
        { filename: 'coool.svg', url: 'https://tweakers.net/g/s/coool.svg' },
        { filename: 'clown.svg', url: 'https://tweakers.net/g/s/clown.svg' },
        { filename: 'biggrin.svg', url: 'https://tweakers.net/g/s/biggrin.svg' },
        { filename: 'worshippy.svg', url: 'https://tweakers.net/g/s/worshippy.svg' },
        { filename: 'kwijl.svg', url: 'https://tweakers.net/g/s/kwijl.svg' },
        { filename: 'heart.svg', url: 'https://tweakers.net/g/s/heart.svg' },
        { filename: 'yawnee.gif', url: 'https://tweakers.net/g/s/yawnee.gif' },
        { filename: 'rc5.svg', url: 'https://tweakers.net/g/s/rc5.svg' },
        { filename: 'nosmile2.svg', url: 'https://tweakers.net/g/s/nosmile2.svg' },
        { filename: 'shutup.gif', url: 'https://tweakers.net/g/s/shutup.gif' },
        { filename: 'confused.svg', url: 'https://tweakers.net/g/s/confused.svg' },
        { filename: 'bonk.gif', url: 'https://tweakers.net/g/s/bonk.gif' },
        { filename: 'frusty.gif', url: 'https://tweakers.net/g/s/frusty.gif' },
        { filename: 'hypocrite.gif', url: 'https://tweakers.net/g/s/hypocrite.gif' },
        { filename: 'sleephappy.gif', url: 'https://tweakers.net/g/s/sleephappy.gif' },
        { filename: 'sadley.svg', url: 'https://tweakers.net/g/s/sadley.svg' },
        { filename: 'facepalm.gif', url: 'https://tweakers.net/g/s/facepalm.gif' },
        { filename: 'tweakers.svg', url: 'https://tweakers.net/g/s/tweakers.svg' },
        { filename: 'henk.svg', url: 'https://tweakers.net/g/s/henk.svg' },
        { filename: 'nosmile.gif', url: 'https://tweakers.net/g/s/nosmile.gif' },
        { filename: 'farewell.gif', url: 'https://tweakers.net/g/s/farewell.gif' },
        { filename: 'pukey.gif', url: 'https://tweakers.net/g/s/pukey.gif' },
        { filename: 'nerd.svg', url: 'https://tweakers.net/g/s/nerd.svg' },
        { filename: 'vork.svg', url: 'https://tweakers.net/g/s/vork.svg' },
        { filename: 'michel.svg', url: 'https://tweakers.net/g/s/michel.svg' },
        { filename: 'loveit.svg', url: 'https://tweakers.net/g/s/loveit.svg' },
        { filename: 'sleepey.gif', url: 'https://tweakers.net/g/s/sleepey.gif' },
        { filename: 'devilish.svg', url: 'https://tweakers.net/g/s/devilish.svg' },
        { filename: 'shadey.gif', url: 'https://tweakers.net/g/s/shadey.gif' },
        { filename: 'bye.gif', url: 'https://tweakers.net/g/s/bye.gif' },
        { filename: 'thumbsup.svg', url: 'https://tweakers.net/g/s/thumbsup.svg' },
        { filename: 'ok.svg', url: 'https://tweakers.net/g/s/ok.svg' },
        { filename: 'bonk3.gif', url: 'https://tweakers.net/g/s/bonk3.gif' },
        { filename: 'loveys.gif', url: 'https://tweakers.net/g/s/loveys.gif' },
        { filename: 'sintsmiley.gif', url: 'https://tweakers.net/g/g/s/sintsmiley.gif' },
        { filename: 'xmas.svg', url: 'https://tweakers.net/g/s/xmas.svg' },
        { filename: 'marrysmile.svg', url: 'https://tweakers.net/g/s/marrysmile.svg' },
        { filename: 'bloos.svg', url: 'https://tweakers.net/g/s/bloos.svg' },
        { filename: 'eerie.svg', url: 'https://tweakers.net/g/s/eerie.svg' },
        { filename: 'emo.svg', url: 'https://tweakers.net/g/s/emo.svg' },
        { filename: 'huh.svg', url: 'https://tweakers.net/g/s/huh.svg' },
        { filename: 'yes.gif', url: 'https://tweakers.net/g/s/yes.gif' },
        { filename: 'no.gif', url: 'https://tweakers.net/g/s/no.gif' },
        { filename: 'pompom.gif', url: 'https://tweakers.net/g/s/pompom.gif' },
        { filename: 'nopompom.gif', url: 'https://tweakers.net/g/s/nopompom.gif' },
        { filename: 'lol.gif', url: 'https://tweakers.net/g/s/lol.gif' },
        { filename: 'hup.gif', url: 'https://tweakers.net/g/s/hup.gif' },
        { filename: 'oranje.gif', url: 'https://tweakers.net/g/s/oranje.gif' },
        { filename: 'belgie.gif', url: 'https://tweakers.net/g/s/belgie.gif' },
        { filename: 'paard.svg', url: 'https://tweakers.net/g/s/paard.svg' },
        { filename: 'rozewolk.gif', url: 'https://tweakers.net/g/s/rozewolk.gif' },
        { filename: 'knuf.gif', url: 'https://tweakers.net/g/s/knuf.gif' },
        { filename: 'yummie-beer.svg', url: 'https://tweakers.net/g/s/yummie-beer.svg' }
    ];

    console.log(`📥 Downloading ${smileys.length} smileys...`);

    const zip = new JSZip();
    let successCount = 0;
    let failCount = 0;

    // Download all smileys
    for (let i = 0; i < smileys.length; i++) {
        const smiley = smileys[i];
        try {
            console.log(`[${i + 1}/${smileys.length}] Fetching ${smiley.filename}...`);

            const response = await fetch(smiley.url);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const blob = await response.blob();
            zip.file(smiley.filename, blob);
            successCount++;

        } catch (error) {
            console.error(`❌ Failed to download ${smiley.filename}: ${error.message}`);
            failCount++;
        }
    }

    console.log(`\n📊 Download Summary:`);
    console.log(`   ✅ Success: ${successCount}`);
    console.log(`   ❌ Failed: ${failCount}`);

    if (successCount > 0) {
        console.log('\n📦 Creating zip file...');
        const zipBlob = await zip.generateAsync({ type: 'blob' });

        // Trigger download
        const link = document.createElement('a');
        link.href = URL.createObjectURL(zipBlob);
        link.download = 'tweakers-smileys.zip';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);

        console.log('✅ Download started! Check your downloads folder for tweakers-smileys.zip');
    } else {
        console.error('❌ No smileys were downloaded successfully.');
    }

})().catch(error => {
    console.error('❌ Script error:', error);
});
