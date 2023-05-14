![Banner for Paco Panda Drawing Stats](https://user-images.githubusercontent.com/94678583/220274497-18b6a944-a759-469e-a10e-1d9b1ec6a95b.png)

<h1 align="center">Paco Panda Drawing Stats</h1>

<p align="center">
	<a href="https://opensource.org/licenses/MIT">
		<img src="https://img.shields.io/github/license/kuroji-fusky/pacopanda-drawing-stats?style=flat-square" />
	</a>
</p>
	
**Paco Panda Drawing Stats** is a data analysis and data visualization project
that collects and parses drawing data from a furry artist and illustrator Paco
Panda.

Initially made simply out of curiosity - it has expanded to provide its own REST
and GraphQL APIs, and utilizes Supabase as the database.

## Project structure

This project is structured as a
[**monorepo**](https://monorepo.tools/#what-is-a-monorepo), it uses Yarn
workspaces and Turborepo to install and manage dependencies in each subdirectory
and remotely cache builds on the cloud via Turborepo.

Written in TypeScript, Python, and Rust - it utilizes the ES Module syntax, with
some files utilize the `.cjs` file type for Prettier, Tailwind CSS configs.

- `.github` - CI/CD Workflow stuff
- `.husky` - Pre-commit hooks for lint-staging
- `apps`
  - `admin` - A desktop dashboard app written in Tauri
  - `website` - The website written in Nuxt 3 + Tailwind CSS
- `packages`
  - `types` - Shared TypeScript declarations
  - `ui` - Shared design system
- `python`
  - `parinton` - Local scraper and parser library for manipulating public
    drawing data with Python

## Setup and Installation

### Prerequisites

- **Required**
  - Node.js 18 or higher (LTS recommended)
  - Python 3.10 or higher
  - Yarn Package Manager
- **Optional**
  - Rust (rustc 1.6.x or higher)
  - VS 2017 Pre-requisites
  - WSL/Git Bash

### Installation

Install Node dependencies with Yarn:

```console
yarn install
```

Then, clone the `.env` files:

```console
cp apps/website/.env.example apps/website/.env
cp apps/admin/.env.example apps/admin/.env
```

## API

![API banner](https://user-images.githubusercontent.com/94678583/203912229-9b6c2479-e999-4b36-9d54-205037691d18.png)

> **Note** Section WIP

### Planned Endpoints

- `/character/:character?={query}`
- `/characters/?={query}`
- `/artwork/:year/:title?={query}`

## About this project

![](https://user-images.githubusercontent.com/94678583/208869784-c68b5483-8e18-4d01-9163-d502b4cb40c5.png)

The project began on October 31, 2021, and the possible inspiration from this
project is through McBroken (basically a McDonald's broken ice cream machine
site) and it'd be interesting to see in all of his drawings to see said data,
and its various datasets.

This project collects the following:

- The title and date of the piece
- Number of character(s) species and names
- Media type (either drawn digital or traditional)
- Programs/mediums used (i.e. Photoshop, Procreate, etc.)
- The source where I got the data from (i.e. FurAffinity, DeviantArt, InkBunny,
  Weasyl, etc.)

Previously, I have to manually source it through FurAffinity and DeviantArt for
his draft drawings (including his _Art & Biro_ comics). Unfortunately, drawings
from Twitter won't be counted in order to ease the load on my end and the
dataset as well since all the data gathered will be hardcoded to the site.

### Why did you create this project?

Believe it or not, it's not my intention to impress him in general.

I'm just a huge fan of his artwork and his unique and adorable art style that
I'd want to see how many characters he's drawn since the early to mid-2000s, but
he'd for sure find it interesting as it's more of a fun project to a new hobby
of mine, learning not only JavaScript but also learning a bit of back-end and
basic data management in the process of other projects I do.

During the early stages of this project - I have limited backend knowledge and I
needed a help with [@thatITfox][it] for setting up a Flask web server, and now
currently working with Redis stuff!

### Isn't this taking it too far?

As someone who admires his art, yes... to some extent. Well, sure - it may feel
like I watch him on every step, but I only use them for analytical and
informational purposes; parsing drawing data on his Twitter profile would be
difficult and will require more work.

It's more of a serious yet passion side-project of mine to show various kinds of
drawing data from his.

### Are the images/drawings stored in the database?

No, most image requests are coming from FurAffinity since they use Cloudflare as
their CDN under the hood to cache media types.

## License

Paco Panda Drawing Stats' source code is open source and is licensed under
[MIT](https://opensource.org/licenses/MIT).

[it]: https://github.com/thatITfox
