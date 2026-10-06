import os

file_path = r"C:\Users\Admin\.gemini\antigravity\scratch\connect-india\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Brand Identity - meta tags
    ('<meta content="Find the best rates on event accommodation with EventBeds™. Partnering with top global organisers, we offer 1m+ rooms near key venues for a seamless event experience and real-time booking data." name="description">',
     '<meta content="Connect India™ — India\'s leading omni-channel communication platform. Send SMS, RCS & WhatsApp messages at scale with our powerful Omni Panel. Real-time analytics, campaign management & API integration." name="description">'),
    ('<meta content="EventBeds™ by NuBreed Hotels" property="og:title">',
     '<meta content="Connect India™ — Omni-Channel Communication Platform" property="og:title">'),
    ('<meta content="Find the best rates on event accommodation with EventBeds™. Partnering with top global organisers, we offer 1m+ rooms near key venues for a seamless event experience and real-time booking data." property="og:description">',
     '<meta content="Connect India™ — India\'s leading omni-channel communication platform. Send SMS, RCS & WhatsApp messages at scale with our powerful Omni Panel. Real-time analytics, campaign management & API integration." property="og:description">'),
    ('<meta content="EventBeds™ by NuBreed Hotels" name="twitter:title">',
     '<meta content="Connect India™ — Omni-Channel Communication Platform" name="twitter:title">'),
    ('<meta content="Find the best rates on event accommodation with EventBeds™. Partnering with top global organisers, we offer 1m+ rooms near key venues for a seamless event experience and real-time booking data." name="twitter:description">',
     '<meta content="Connect India™ — India\'s leading omni-channel communication platform. Send SMS, RCS & WhatsApp messages at scale with our powerful Omni Panel. Real-time analytics, campaign management & API integration." name="twitter:description">'),

    # Brand Identity - Logo
    ('<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="auto" viewBox="0 0 755 144" fill="none">\n<g clip-path="url(#clip0_744_1444)">\n<path d="M734.07 29.5585H737.119V38.095H739.383V29.5585H742.447V27.6299H734.07V29.5585Z" fill="currentColor"></path>\n<path d="M743.348 38.095H745.507V31.0834L748.254 38.095H750.095L752.842 31.0834V38.095H755V27.6299H752.087L749.25 35.3143L746.322 27.6299H743.348V38.095Z" fill="currentColor"></path>\n<path d="M227.917 106.118C244.13 106.118 254.663 96.6618 256.556 84.8413H240.107C238.686 90.5152 233.953 93.4703 227.207 93.4703C218.805 93.4703 213.243 88.2693 212.888 79.6403V78.8129H257.029C257.384 76.9216 257.503 74.9121 257.503 73.1391C257.266 55.2901 244.959 43.9424 226.734 43.9424C207.918 43.9424 195.492 56.2357 195.492 75.1485C195.492 93.9431 207.681 106.118 227.917 106.118ZM213.243 67.938C214.19 60.7275 219.633 56.3539 226.852 56.3539C234.426 56.3539 239.515 60.4911 240.698 67.938H213.243Z" fill="currentColor"></path>\n<path d="M273.791 105.409H294.501L316.394 44.6514H298.88L284.442 88.3872L269.768 44.6514H251.898L273.791 105.409Z" fill="currentColor"></path>\n<path d="M343.207 106.118C359.42 106.118 369.952 96.6618 371.846 84.8413H355.396C353.976 90.5152 349.242 93.4703 342.497 93.4703C334.095 93.4703 328.533 88.2693 328.178 79.6403V78.8129H372.319C372.674 76.9216 372.792 74.9121 372.792 73.1391C372.556 55.2901 360.248 43.9424 342.024 43.9424C323.207 43.9424 310.781 56.2357 310.781 75.1485C310.781 93.9431 322.971 106.118 343.207 106.118ZM328.533 67.938C329.479 60.7275 334.923 56.3539 342.142 56.3539C349.716 56.3539 354.804 60.4911 355.988 67.938H328.533Z" fill="currentColor"></path>\n<path d="M410.905 43.9424C401.556 43.9424 395.994 47.4886 392.089 52.2168L390.55 44.6517H375.994V105.409H392.68V74.3211C392.68 63.8009 397.651 57.6542 406.289 57.6542C414.692 57.6542 418.597 63.0916 418.597 73.3755V105.409H435.283V71.7206C435.283 50.9165 424.041 43.9424 410.905 43.9424Z" fill="currentColor"></path>\n<path d="M444.26 88.0327C444.26 99.6168 450.058 105.409 461.656 105.409H475.265V91.3424H466.981C462.603 91.3424 460.946 89.5694 460.946 85.314V58.7178H474.91V44.6515H460.946V27.6299H444.26V44.6515H434.201V58.7178H444.26V88.0327Z" fill="currentColor"></path>\n<path d="M512.099 43.9423C503.697 43.9423 497.78 47.4885 493.756 52.3349V27.8369H477.07V105.409H491.626L493.283 97.1346C497.188 102.335 503.223 106.118 511.98 106.118C528.43 106.118 540.264 93.7066 540.264 74.912C540.264 55.6446 528.43 43.9423 512.099 43.9423ZM508.312 92.5246C499.2 92.5246 493.519 85.3141 493.519 74.912C493.519 64.6282 499.2 57.5359 508.312 57.5359C517.424 57.5359 523.341 64.6282 523.341 75.0302C523.341 85.4323 517.424 92.5246 508.312 92.5246Z" fill="currentColor"></path>\n<path d="M573.674 106.118C589.886 106.118 600.419 96.6618 602.312 84.8413H585.863C584.443 90.5152 579.709 93.4703 572.963 93.4703C564.561 93.4703 558.999 88.2693 558.644 79.6403V78.8129H602.786C603.141 76.9216 603.259 74.9121 603.259 73.1391C603.022 55.2901 590.715 43.9424 572.49 43.9424C553.674 43.9424 541.248 56.2357 541.248 75.1485C541.248 93.9431 553.437 106.118 573.674 106.118ZM558.999 67.938C559.946 60.7275 565.39 56.3539 572.608 56.3539C580.182 56.3539 585.271 60.4911 586.454 67.938H558.999Z" fill="currentColor"></path>\n<path d="M650.602 52.2167C646.697 47.2521 640.661 43.9423 632.259 43.9423C616.046 43.9423 604.094 56.1174 604.094 74.912C604.094 94.1794 616.046 106.118 632.377 106.118C641.135 106.118 647.052 102.217 651.075 97.0164L652.732 105.409H667.288V27.8369H650.602V52.2167ZM636.046 92.5246C626.934 92.5246 621.135 85.4323 621.135 75.0302C621.135 64.6282 626.934 57.5359 636.046 57.5359C645.158 57.5359 650.839 64.7464 650.839 75.1484C650.839 85.4323 645.158 92.5246 636.046 92.5246Z" fill="currentColor"></path>\n<path d="M670.164 85.1954C670.874 98.1979 682.354 106.118 699.276 106.118C715.608 106.118 726.968 98.4343 726.968 86.3774C726.968 72.6656 715.371 69.4741 701.407 68.0556C692.649 66.9918 687.442 66.519 687.442 61.909C687.442 58.0082 691.703 55.6441 698.211 55.6441C704.957 55.6441 709.572 58.5992 710.046 63.4456H726.022C725.193 51.0341 713.951 43.8236 697.62 43.8236C681.999 43.7054 671.466 51.6252 671.466 63.6821C671.466 76.2118 682.472 79.4033 696.673 81.0582C706.495 82.3584 710.637 82.7131 710.637 87.6777C710.637 91.933 706.377 94.1789 699.395 94.1789C691.229 94.1789 686.614 90.5146 686.022 85.1954H670.164Z" fill="currentColor"></path>\n<path d="M71.6847 0.157227C32.098 0.157227 0 32.2552 0 71.8419V143.515H71.6847C91.4837 143.515 109.402 135.491 122.362 122.519C135.333 109.559 143.358 91.641 143.358 71.8419C143.358 32.2552 111.271 0.157227 71.6847 0.157227ZM110.417 109.696L109.242 116.695C99.1549 125.016 86.1492 130.054 71.9582 130.019C48.1013 129.974 25.2817 115.692 16.4707 89.7602L64.2985 83.4683L107.852 104.533C109.733 105.547 110.77 107.61 110.417 109.696ZM119.638 105.49C119.638 105.49 119.832 103.245 119.934 102.116C120.094 100.27 119.056 98.5256 117.335 97.7391L73.2576 78.0427L88.1326 66.2795C89.5574 64.6951 91.7801 64.0568 93.8432 64.6381C104.66 67.6929 115.466 70.7477 126.272 73.8024C128.472 74.4179 130.022 76.6863 129.794 78.9203C128.745 88.3582 125.428 97.1122 119.638 105.49Z" fill="currentColor"></path>\n</g>\n<defs>\n<clipPath id="clip0_744_1444">\n<rect width="755" height="144" fill="white"></rect>\n</clipPath>\n</defs>\n</svg>',
     '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="40" viewBox="0 0 200 40"><text x="0" y="30" font-family="system-ui, -apple-system, sans-serif" font-size="24" font-weight="700" fill="currentColor">Connect India</text></svg>'),

    # Hero Section - All devices (Subheader)
    ('<div class="subheader hero">Discover your next</div>', '<div class="subheader hero">Start Your Campaign With</div>'),

    # Hero Section - Desktop Headings
    ('<h1 class="heading-mega">perfect <span class="opacity-span">s</span>tay</h1>',
     '<h1 class="heading-mega">Connect <span class="opacity-span">I</span>ndia</h1>'),
    ('<div class="heading-mega mask top">perfect stay</div>', '<div class="heading-mega mask top">Connect India</div>'),
    ('<div class="heading-mega mask"><span class="opacity-span">perfect</span> s<span class="opacity-span">tay</span></div>',
     '<div class="heading-mega mask"><span class="opacity-span">Connect</span> I<span class="opacity-span">ndia</span></div>'),
    ('<div class="heading-mega mask"><span class="opacity-span">perfect s</span>tay</div>',
     '<div class="heading-mega mask"><span class="opacity-span">Connect I</span>ndia</div>'),
    
    # Hero Section - Tablet Headings (if they differ, otherwise handled by string replace above globally if match)
    
    # Price pins -> Stats
    ('<div class="pin-price three">£349</div>', '<div class="pin-price three">98% Open</div>'),
    ('<div class="pin-price three">£335</div>', '<div class="pin-price three">45% CTR</div>'),
    ('<div class="pin-price">£285</div>', '<div class="pin-price">10x ROI</div>'),
    
    ('<div class="pin-price two">£349</div>', '<div class="pin-price two">98% Open</div>'),
    ('<div class="pin-price two">£335</div>', '<div class="pin-price two">45% CTR</div>'),
    ('<div class="pin-price one">£285</div>', '<div class="pin-price one">10x ROI</div>'),
    
    ('<div class="pin-price tab-2">£335</div>', '<div class="pin-price tab-2">45% CTR</div>'),
    ('<div class="pin-price tab">£285</div>', '<div class="pin-price tab">10x ROI</div>'),
    
    ('<div class="pin-price tab-3">£349</div>', '<div class="pin-price tab-3">98% Open</div>'),

    # Also catch other occurrences just in case class names vary slightly:
    ('>£349<', '>98% Open<'),
    ('>£335<', '>45% CTR<'),
    ('>£285<', '>10x ROI<'),

    # Deals Section
    ('The webs best hotel', 'The best omni-channel'),
    ('deals for events', 'messaging platform'),
    ('The webs best<', 'The best omni<'),
    ('hotel deals for<', 'channel messaging<'),
    ('events<', 'platform<'),
    ('Search event-exclusive deals &amp; unlock secret prices', 'Send SMS, RCS &amp; WhatsApp messages from one powerful dashboard'),
    ('from your favourite hotel brands and apartments.', 'with real-time analytics and campaign management.'),
    ('Search event-exclusive deals & unlock secret prices', 'Send SMS, RCS & WhatsApp messages from one powerful dashboard'),
    ('Flexible rates, massive savings and a choice of', 'Powerful APIs, smart routing and reach'),
    ('<div class="stat-h1">1M</div>', '<div class="stat-h1">10B</div>'),
    ('<div class="stat-text">properties</div>', '<div class="stat-text">messages sent</div>'),

    # Discover Section
    ('Easy search', 'Easy setup'),
    ('<h3 class="h3-white">Preference</h3>', '<h3 class="h3-white">Configure</h3>'),
    ('Nearest hotels to your event are shown on an easy-to-use map.', 'Set up SMS, RCS &amp; WhatsApp channels from one intuitive dashboard.'),
    ('<h3 class="h3-white">Save</h3>', '<h3 class="h3-white">Send</h3>'),
    ('Your exclusive discount code and secret prices with savings up to 50%.', 'Launch campaigns with smart routing for maximum delivery and engagement.'),
    ('<h3 class="h3-white">Book</h3>', '<h3 class="h3-white">Analyze</h3>'),
    ('Compare and book your perfect hotel or apartment in seconds.', 'Track delivery, opens and conversions with real-time analytics.'),
    
    # Discover section mobile/tablet variations
    ('Nearest hotels to your event are shown on an easy-to-use map.', 'Set up SMS, RCS & WhatsApp channels from one intuitive dashboard.'),
    ('Your exclusive discount code and secret prices with savings up to 50%.', 'Launch campaigns with smart routing for maximum delivery and engagement.'),
    ('Compare and book your perfect hotel or apartment in seconds.', 'Track delivery, opens and conversions with real-time analytics.'),

    # Hotel Section
    ('Book and relax', 'Send and relax'),
    ('Flexible options give you more time...', 'Automated workflows handle your messages while you focus on growing your business.'),
    ('Fully flexible rates.', 'Multi-channel routing.'),
    ('Semi-flexible options.', 'Smart scheduling.'),
    ('Amend or cancel your booking online.', 'Real-time delivery tracking.'),
    ('On demand customer service.', '24/7 support &amp; monitoring.'),

    # Benefits Section
    ('Deals to make', 'Features to make'),
    ('your eyes water', 'your campaigns soar'),
    ('Event', 'Channel'),
    ('exclusives', 'integration'),
    ('VIP benefits only available with EventBeds™', 'Seamless SMS, RCS &amp; WhatsApp from one platform'),
    ('Brand', 'Smart'),
    ('discounts', 'analytics'),
    ('Unlock secret prices at your favourite brands with powerful discounts', 'Real-time insights into message delivery, engagement and conversion rates'),
    ('Referral', 'API'),
    ('scheme', 'access'),
    ('Send your exclusive discounts to other event attendees. Share the love', 'Integrate our powerful messaging API into your existing systems in minutes'),

    # Partners Section
    ('Safe &amp; secure', 'Safe &amp; secure'),
    ('payments', 'messaging'),
    ("We partner with Stripe for safe and secure payments so you don't need to worry about anything but enjoying your stay.", "We're powered by enterprise-grade infrastructure with end-to-end encryption, ensuring your messages are delivered securely every time."),
    ('Members get', 'Businesses get'),
    ('much more', 'much more'),
    ('Join our members waiting list to get exclusive access to our newest deals, bigger discounts &amp; VIP perks.', 'Join our early adopter program to get exclusive access to new features, premium rates and dedicated support.'),
    ('Sign up to our newsletter', 'Join early access program'),
    ('Join VIP waiting list', 'Get started free'),
    ('Join VIP waiting list', 'Join Connect India'),
    ('Join the waitlist and be the first one to get an invite.', 'Join our early access program and be among the first to experience Connect India.'),

    # Partners Logo Slider
    ('Partners', 'Trusted By'),
    ('Our high-level', 'Our technology'),
    ('partners', 'partners'),
    ('We cooperate with top partners and provide access to over 1m properties in 180 countries.', 'We integrate with leading platforms and serve businesses across 50+ countries.'),

    # Reviews Section
    ('Trusted by people', 'Trusted by businesses'),
    ('Within minutes the friendly sales assistant had arranged my preferred hotel. Brilliant service!', 'Within minutes of setting up Connect India, we launched our first WhatsApp campaign and saw a 45% response rate. The dashboard is incredibly intuitive!'),
    ('Stephen A.', 'Rajesh K.'),
    ('Super professional, organised, helpful, and very competitive on price. I\'ll 100% use them again.', 'The API integration was seamless. We connected our CRM in under an hour and now send automated SMS notifications to 50K+ customers daily.'),
    
    # Founders Section
    ('EventBeds™', 'Connect India™'),
    ('NuBreed Hotels', 'Connect India Technologies'),

    # Footer & CTA
    ('Get the latest from EventBeds™', 'Get the latest from Connect India™'),
    ('Book Demo', 'Get Started'),
    
    # Nav Menu
    ('For business', 'SMS Platform'),
    ('For Venues', 'RCS Solutions'),
    ('Partner API', 'WhatsApp Business'),
    ('Knowledge Base', 'Documentation'),

    # Cleanups
    ('<div data-nce-attribution-bar></div>', ''),
    ('<script src="./nce-runtime.js"></script>', ''),
]

# We need to explicitly match FinSweet and GTM to remove them.
# There are 2 GTM tags, Finsweet consent, Zendesk references
for r_from, r_to in replacements:
    content = content.replace(r_from, r_to)

# Custom Cleanup regex or specific strings
cleanup_strings = [
    '<script async src=\'https://www.googletagmanager.com/gtag/js?id=G-LHC68YEMVW\'></script>',
    "<script> window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'G-LHC68YEMVW');\n</script>",
    '<script async="" src="https://cdn.jsdelivr.net/npm/@finsweet/cookie-consent@1/fs-cc.js" fs-cc-mode="opt-in"></script>',
    "<script type=\"fs-cc\" fs-cc-categories=\"personalization, analytics, marketing\">(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':\nnew Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],\nj=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=\n'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);\n})(window,document,'script','dataLayer','G-LHC68YEMVW');</script>",
    '<script defer="" src="https://cdn.jsdelivr.net/npm/@finsweet/attributes-scrolldisable@1/scrolldisable.js"></script>',
    # NCE runtime might look different, let's remove everything that says <script>window.__NCE_PAGE__
]

for s in cleanup_strings:
    content = content.replace(s, '')
    
# Advanced NCE attribution removal:
import re
content = re.sub(r'<script>window\.__NCE_PAGE__=.*?</script>', '', content, flags=re.DOTALL)
content = re.sub(r'<div data-nce-attribution-bar(?:.*?)>.*?</div>', '', content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Edits complete.")
