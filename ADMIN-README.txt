SKY GRAPHICS — CERTIFICATE PORTAL — ADMIN NOTES
=================================================
Keep this file for yourself. Do not upload it to the live site or share it in the group.

WHAT CHANGED
------------
The leaderboard (data.js, script.js, leaderboard.html) has been removed. Points and
rankings are no longer shown anywhere. In its place is certificates.html — a single
page where each graduate enters a private key to view and download their certificate.
Nothing is visible until the correct key is entered.

FILES IN THIS ZIP
------------------
index.html            - the countdown page (button now links to certificates.html)
certificates.html      - the certificate portal (key entry + admin/test mode)
Assets/certificate-christine.png   - Christine Choundong's certificate
Assets/certificate-opal.png        - Abongnwi Chrioni-Opal Forba's certificate

Upload all of this to the same place your current site is hosted, keeping the
Assets folder intact. You can delete the old leaderboard.html, script.js, and
data.js from your host — they're no longer used.

THE KEYS
--------
Christine Choundong  -> SKY-CHR-2026-X7Q9
Abongnwi Chrioni-Opal Forba -> SKY-OPL-2026-M4T2

Each key only unlocks that person's own certificate. Keys are not case sensitive
and ignore spaces, so typos are forgiving.

DIRECT LINKS (no typing required)
----------------------------------
You can skip the key entirely by sending each person a direct link. Replace
YOURSITE.com with your actual domain:

Christine: https://YOURSITE.com/certificates.html?key=SKY-CHR-2026-X7Q9
Opal:      https://YOURSITE.com/certificates.html?key=SKY-OPL-2026-M4T2

Opening that link auto-unlocks their certificate immediately.

ADMIN / TEST MODE
------------------
To test the whole flow yourself (and preview both certificates without using
either person's real key), visit:

https://YOURSITE.com/certificates.html?admin=SKY-ADMIN-2026

This shows an "Admin / Test Mode" panel listing both names and keys with a
"Preview" button for each, so you can confirm images load and download
correctly before sending anything out. This admin link is only visible to
whoever has the URL — it's not shown or hinted at anywhere on the public page.

SENDING TO THE WHATSAPP GROUP
------------------------------
Do NOT post the individual keys or direct links in the shared group — that
would let anyone open someone else's certificate link if they intercepted it,
and it looks messier. Instead:

1. Post one message in the group announcing the portal is live, e.g.:

   "🎓 Certificates are live! Head to [YOURSITE.com/certificates.html],
   enter the unique key sent to you directly, and download your Sky
   Graphics Figma Edition 1 certificate. Keys are private — please
   don't share yours."

2. Then DM (private message) each graduate their own direct link or key
   individually:

   To Christine: "Here's your certificate — https://YOURSITE.com/certificates.html?key=SKY-CHR-2026-X7Q9"
   To Opal:      "Here's your certificate — https://YOURSITE.com/certificates.html?key=SKY-OPL-2026-M4T2"

This keeps the portal link public but each person's unlock private.

ADDING MORE PEOPLE LATER
--------------------------
Open certificates.html, find the CERTIFICATES object near the top of the
<script> block, and add a new entry following the same pattern (name, cert
number, certificate image filename, download filename), then drop that
person's certificate image into the Assets folder.
