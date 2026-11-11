# What upakenigma.ru is

**ODO «ENIGMA» (ОДО «ЭНИГМА») is a Belarusian manufacturer of plastic packaging, based in Mogilev.** It makes bottles and jars (флаконы) from PET, PET-G, PVC, PE and PP, plus caps and closures. Its customers are cosmetics, household-chemicals and medical brands. It also decorates bottles with silk-screen printing, heat-transfer printing and hot-foil stamping.

The website is a **B2B lead-generation catalog**. There are no prices and no cart: every product leads to a "leave a request" form (name and phone), and a sales manager follows up.

`upakenigma.ru` permanently redirects (301) to **upakenigma.com**. A news post on the site announces the move to the .com zone and asks partners to switch to `@upakenigma.com` e-mail addresses. "Upak" is short for *упаковка* (packaging), so the domain reads "Enigma packaging".

Everything below was read from the live site on 11 November 2026.

## Company facts

| | |
|---|---|
| Legal name | ОДО «ЭНИГМА». ODO is a Belarusian legal form, an "additional liability company" |
| Registration number (УНП) | 700008381 |
| Address | 212036, Mogilev, ul. Simonova 11/1, Belarus |
| Founded | 1992. The site celebrated "33 years" in 2025 |
| Own production since | 2000 |
| Claimed markets | Belarus, Russia, CIS, Europe |
| Quality | ISO 9001:2015 (GOST R ISO 9001-2015) certificates from two Russian voluntary certification bodies, TQC and BQC. **Both certificates shown on the site have expired** (see [audit](audit.md)) |
| Trade shows | RosUpack, Moscow (2015, 2016, 2024, 2025); Pharmtech & Ingredients, Moscow (2017) |
| Channels | Phone (multichannel +375 222 705-222), Viber, WhatsApp, Telegram, Instagram `@enigma_company_`, e-mail upakenigma@mail.ru. The contacts page also lists separate addresses for the director, sales, accounting, customs and the technical department |
| Website built by | Ultraweb.by, a Belarusian web studio (credited in the footer) |

## History (from the "О нас" / About page)

- **1992.** Founded as a private foreign-trade company. For its first five years it imported and exported almost anything, from vegetables and fruit to agricultural fertilizers.
- **1998.** Specialized in importing plastic containers from Europe.
- **2000.** Started its own packaging production.
- **Today.** Makes PE, PVC and PET products on equipment from Germany, Japan, Italy, the USA, Korea and China.

The Production page highlights a **Jomar injection-blow-molding machine** (New Jersey). It makes PVC bottles in a single automatic step. PVC suits aggressive liquids, and unlike extrusion blow molding the process leaves no flash to regrind. The machine currently runs a 5-cavity mold for 50 ml cylindrical bottles.

## What they sell

The catalog is organized in **10 categories**:

| Category (Russian) | Meaning |
|---|---|
| Медицинские флаконы | Medical bottles |
| Флаконы для косметики | Cosmetic bottles |
| Флаконы для бытовой химии | Household-chemical bottles |
| Крышки и колпачки | Caps and closures |
| Импортная продукция | Imported products |
| Декорирование | Decoration services |
| Эксклюзивные флаконы | Exclusive (custom) bottles |
| Пластиковые флаконы 10 / 50 / 100 мл | Plastic bottles by volume (3 categories) |

`/products` lists **46 items**, grouped into named families: Basis, Bella, Beta, Bond, Fum, Grenada, Jomar 50, Naturae, Particula, Prima, Ray, Ring, Ruby, Sanit, Sitis, Spatium, Square, Uno and Vika (5–60 ml). The list also includes a Flip-top 24 cap and the three decoration services as items. The newest product is **Tear 360 ml** (June 2025): a PE bottle that comes with a tamper-evident cap and a dropper insert.

The site's copy also mentions flip-top, disc-top and plain screw caps, pumps and trigger sprayers, custom colors, logo printing, and design and prototyping of custom packaging.

### Product data model

Each product page has a **"Характеристики" (specifications)** table with the same six fields:

| Field | Example (Uno 100 ml) |
|---|---|
| Neck diameter, mm (Диаметр горла) | 24 |
| Volume, ml (Объем) | 100 |
| Weight, g (Вес) | 22 |
| Height, mm (Высота) | 150 |
| Diameter, mm (Диаметр) | 35.3 |
| Material (Материал) | PET |

Product pages also show four badges ("own production", "30+ years", "bottle decoration", "fast delivery across the CIS"), a "Мы рекомендуем" (we recommend) carousel, and a request button. There is no price field on the page, though the template's edit attributes include unused price and sale-price fields.

## How the site sells

Visitors have several ways to contact sales, and none of them involves buying online:

1. **"Оставить заявку"** (leave a request) on every product card opens a modal with name and phone fields. The product name is sent in a hidden field.
2. **"Заказать звонок"** (request a call) in the header.
3. **"Заявка на консультацию"** (consultation request), a form at the bottom of every page.
4. Phone numbers, messenger links, and a third-party callback widget (Venyoo).

The homepage also explains the process in six steps: send a request, a manager processes it, price and delivery dates are agreed, packaging is developed and prototyped, the order is produced, and it is shipped.

## Site map

| URL | Page |
|---|---|
| `/` | Home |
| `/products` | All products |
| `/catalog/<category>` | Category listing: chips and a 3-column card grid, then SEO text |
| `/products/<slug>` | Product page: photo, specifications, request button, recommendations |
| `/o-nas` | About |
| `/proizvodstvo` | Production |
| `/sertifikaty` | Certificates |
| `/blog`, `/blog/<slug>` | News, including the ecology page `/blog/ecology` ("С природой, а не против неё", "With nature, not against it") |
| `/kontakty` | Contacts, with an embedded Google map |

## Technology (as observed)

- **Server:** nginx 1.30.6 and PHP 5.3.29 (from the `X-Powered-By` header; PHP 5.3 has been end-of-life since 2014).
- **CMS:** very likely Simpla, a Russian PHP e-commerce CMS. The `design/default/` theme folder, `files/products/<name>.470x470.jpg?<token>` image URLs and a `/simpla/` path all match it. The front-end template carries WordPress markup (`menu-item-type-custom` classes, WordPress 5.2.1 block-library CSS, `data-live-edit` attributes with `post_title`), so the studio appears to have ported one of its WordPress themes onto it.
- **Front end:** jQuery 1.7.1 (2011) from Google's CDN, Owl Carousel, fancybox (lightbox), arcticmodal (modals), animate.css with scroll-triggered reveals, and a jQuery autocomplete plugin for search.
- **Analytics:** two Yandex.Metrica counters, plus Google and Yandex site-verification tags.

## Things to know before reusing content

- The page source contains a commented-out "clients" block with 14 logos: LG, a Volgograd university, medical centers, a gas supplier, a sports bar and a beauty salon. They look like leftovers from the studio's template rather than Enigma's customer list, so verify before using any of them.
- The certificate scans on the site are out of date. Ask the company for current ones.
