# Xinyu (Ray) Chen — academic website

A personal academic website for **raysuan.github.io**, using the same Jekyll / al-folio theme and layout as the reference site. Includes About, News, Publications, CV, search, and light/dark mode.

## Publish on GitHub Pages

1. Create an **empty** repository named `raysuan.github.io` in the `raysuan` account. Do not initialize it with a README or license.
2. Extract this project's ZIP. In a terminal opened inside the extracted project folder, run:

   ```sh
   git init -b main
   git add .
   git commit -m "Create academic website"
   git remote add origin https://github.com/raysuan/raysuan.github.io.git
   git push -u origin main
   ```

   If Git asks for your name and email, set your own Git identity. Authenticate through GitHub's normal sign-in flow; do not put access tokens into project files.
3. Open repository **Settings → Pages**. Under **Build and deployment → Source**, choose **GitHub Actions**.
4. In **Actions**, open **Deploy academic website**. The initial push may fail if Pages was not enabled yet; choose **Run workflow → main** after changing the Pages setting.
5. When deployment succeeds, your site will be at **https://raysuan.github.io/**.

Future pushes to `main` rebuild and redeploy the site. Pull requests build and check the site without publishing.

## Edit your content

| Change | File |
| --- | --- |
| Biography and profile image | `_pages/about.md` |
| Name, site description and URL | `_config.yml` |
| Publications and their links | `_bibliography/papers.bib` |
| News entries | `_news/` |
| CV contents | `_data/cv.yml` |
| GitHub, LinkedIn, and optional email/Scholar | `_data/socials.yml` |
| Publication images | `assets/img/publication_preview/` |

The profile uses an initials image until you provide a portrait. Add `assets/img/profile.jpg` and set `profile.image: profile.jpg` in `_pages/about.md` to replace it.

To add a CV PDF, put it in `assets/pdf/` and set `cv_pdf: filename.pdf` in `_pages/cv.md`. The current CV is rendered directly from your academic background.

To add news, create `_news/announcement.md`:

```yaml
---
layout: post
date: 2026-11-24
inline: true
---
Your announcement here.
```

Publication descriptions are concise summaries. Replace them with your preferred wording or the full abstracts if desired. `selected={true}` controls which papers appear on the home page.

## Preview locally

Install Ruby 3.3+ and Bundler, then run:

```sh
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000`. To build and check without serving:

```sh
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py
```

## Credits

Based on [al-folio](https://github.com/alshedivat/al-folio), adapted from [Yifan Yu's site](https://github.com/yifan1130/yifan1130.github.io). The MIT license is retained. See `SOURCE_NOTES.md` for publication sources and the customization notes.
