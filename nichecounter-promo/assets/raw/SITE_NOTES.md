# nichecounter.fr — discovery notes (captured 2026-11-15)

## What the site is (verified on the live site)
- `<title>`: "Niche Counter · Le meilleur prix du marché gris de la parfumerie de niche"
- Meta description: "Comparez tous les vendeurs du marché gris de la parfumerie de niche et achetez au prix plancher, paiement sécurisé. France."
- Hero: "Tous les parfums. / Tous les vendeurs. / Le meilleur prix." + "La marketplace des parfums de niche. Dénichez les meilleurs deals, achetez et vendez en toute sécurité."
- It is a **marketplace**: sellers (particuliers + pros) list bottles on Niche Counter; buyers compare the sellers **on the platform** (search → results sortable by "Prix croissant", "Réduction max"…). It does not compare external shops.
- FAQ "meilleur prix": "Chaque parfum n'a qu'une seule fiche produit, sur laquelle tous les vendeurs qui le proposent affichent leur prix. Le prix « dès » affiché est toujours celui du vendeur le moins cher."
- Payment: Stripe Connect. "Paiement débité à la commande" / "Fonds bloqués jusqu'à votre confirmation de réception" / "Un problème ? Ouvrez un litige, l'argent reste bloqué".
- Footer trust row: "Paiement sécurisé · Vendeurs vérifiés · Protection en cas de litige". Sellers: pseudonymous, "vérification d'identité en privé".
- Alerts: "M'alerter sur ce parfum" button on product pages + newsletter "Les nouveautés et les baisses de prix, directement dans votre boîte mail."
- Extra features: "Faire une offre" (offre encadrée, 3 offers per listing, floor price), chat masks phone/e-mail/links.
- Sell page: "Vendez votre parfum sur Niche Counter — Créez votre annonce en quelques minutes." Particulier = gratuit; Pro = "Gratuit au lancement".
- Catalogue today: 16 listings, "104 maisons, de Amouage à Xerjoff" (most brands marked "Bientôt").
- CAUTION: product page says authenticity info is "déclarés par le vendeur. Niche Counter ne les vérifie pas", while footer says "catalogue vérifié, 100 % authentique". → Do NOT make authenticity claims in the ad.

## Spine data (real listings)
- Search "Renaissance" → 4 annonces, XERJOFF Renaissance EDP 100 ml, Neuf sous blister:
  157 € (−40 %), 164 € (−37 %), 171 € (−34 %), 178 € (−32 %); reference 260 €.
- Best one (/annonce/ac95cac8-…): "157 € 260 € −40 %", "Soit 103 € de moins qu'en boutique", seller "Flacon Club 4.6 (53 avis) · 88 ventes · Vendeur professionnel", "Acheter · 157 €".
- Backup: KILIAN Rolling in Love 50 ml: 145/150/155 € vs 250 € (−42 %, "105 € de moins").
- No listing photos for these (site shows initials "XR"/"KR" placeholder tiles). Only Guerlain Rose Nacrée du Désert (site catalogue image /products/guerlain-rose-nacree-du-desert.png) and a Kilian refill have pictures.

## Brand identity (from CSS, `.dark` theme = default)
| token | value |
|---|---|
| page (bg) | rgb(20 18 15) `#14120F` (= theme-color) |
| card | `#1D1A16` |
| imgbg | `#262219` |
| line | `#3A342B` |
| ink | `#F5F1E8` |
| ink2 | `#C9C2B4` |
| muted | `#9A9389` |
| brand (rose, dark) | `#D4636F` |
| brand-fill (dark) | `#AE3A47` |
| gold | `#D3A551` |
| success | `#6FCB9F` |
| light theme page | `#FAF6EF`, brand `#9B2D3A`, gold `#A5762B` |
- Fonts: **Cormorant Garamond** (display, 500–700, headings & product names) + **Hanken Grotesk** (UI/body, 400–700). Both OFL (Google Fonts), latin variable woff2 saved in `fonts/`.
- Logo: line-drawn perfume bottle crossed by diagonals (`logo-mark.png` rose `#9B2D3A` for light bg, `logo-mark-dark.png` rose `#D4636F` for dark bg) + wordmark "Niche Counter" in Cormorant bold.
- Tone: sober, premium, French, "vous", short declaratives ("Dénichez les meilleurs deals").
- No cookie banner on mobile. Fixed bottom nav (Accueil / Découvrir / Vendre / Messages / Connexion) must be cropped/hidden in processed assets.
