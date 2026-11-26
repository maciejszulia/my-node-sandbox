# my-node-sandbox

My first steps with Node.js: a module, an HTTP server, an Express server with a Handlebars view, and a Python generator of sample blog posts in JSON.

A small project of my own from my Computer Science studies at UWM (2020–2024). I wrote the code by hand; the commit history is unchanged. This README was added in November 2026.

Years of work: 2022 (first commit on 2 June 2022, last commit on 7 June 2022).

## Contents

- `my-first-app.js`, `utils.js`: a module with a greeting and an addition.
- `server.js`: an HTTP server on the `http` module.
- `server-express.js`, `setFunctions.js`, `views/`: an Express server that renders `views/index.hbs`.
- `json_generator/`: Python scripts that use Faker to write sample blog posts to `blog_posts.json`.

## Running

```
node my-first-app.js
```

Result on 26 November 2026 (Node.js 22): `Loaded.`, `hello node!` and `9`. `server-express.js` needs the `express` package and `json_generator/` needs Faker; neither is installed on this machine, so I did not run them.

## Po polsku

Repozytorium zawiera moje pierwsze programy w Node.js: moduł, serwer HTTP, serwer Express i generator przykładowych wpisów w Pythonie. Kod napisałem ręcznie w 2022 roku.
