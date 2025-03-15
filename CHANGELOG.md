# Changelog

All notable changes to this project will be documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project attempts to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v1.1.0](https://github.com/engineervix/ten-lists/compare/v1.0.1...v1.1.0) (2025-03-15)


### 🚀 Features

* upgrade to flask v2 and update several outdated dependencies ([f7a7aff](https://github.com/engineervix/ten-lists/commit/f7a7aff0a2e4f61205b1932333b802b4ebdd1820))


### ♻️ Code Refactoring

* `datetime.utcnow()` is deprecated ([0d6d498](https://github.com/engineervix/ten-lists/commit/0d6d4988d7f0f928b794c8c359ccb49bd7021ccf))
* fix port number ([b306b9f](https://github.com/engineervix/ten-lists/commit/b306b9f0b0e6ee24d0e8ccb42bf825dd903b8f89))
* fix some broken things ([f2eda19](https://github.com/engineervix/ten-lists/commit/f2eda1936bcc510a4ee375c5baad883f8b494cb7))
* make things work with Flask v2 ([18eddc3](https://github.com/engineervix/ten-lists/commit/18eddc38c978f719ab1decceec2d994e042844ec))


### 👷 CI/CD

* fix config ([cf564c6](https://github.com/engineervix/ten-lists/commit/cf564c6745a5c777b795670129c9c4ff58a7c174))
* make test job depend on lint job ([8104407](https://github.com/engineervix/ten-lists/commit/810440742ea0585a4ddabf85a3194c5825c19b71))
* more fixes ([8c9de05](https://github.com/engineervix/ten-lists/commit/8c9de05951e45f64ba35b92e9719848cdfa21ef8))
* no need to install grunt-cli ([e71644b](https://github.com/engineervix/ten-lists/commit/e71644b7d501f2bcb11875e3669c2a423eb9f7f0))
* npm install -g grunt-cli ([c7ac2d3](https://github.com/engineervix/ten-lists/commit/c7ac2d3df4bf391e64e8bb9556246f8613244de2))
* run tests in a container ([202e2d4](https://github.com/engineervix/ten-lists/commit/202e2d49d373472267a2c212927c58747d1d4eb8))
* switch to Github Actions ([8917dec](https://github.com/engineervix/ten-lists/commit/8917dec987ceac678b333e64dc099c98d69ed4a0))
* update how environment variables are set ([2e3847e](https://github.com/engineervix/ten-lists/commit/2e3847e9820c5a54833685e5b3391ce0927e5194))


### 🐛 Bug Fixes

* issue with python 3.12 and distutils ([08bc941](https://github.com/engineervix/ten-lists/commit/08bc941462abff39a6506fae042657c26fda8a5b))


### ⚙️ Build System

* add honcho & bump isort and flake8 ([dddce6f](https://github.com/engineervix/ten-lists/commit/dddce6f8650cf011d46b1c07d6109155bba721eb))
* **deps-dev:** update dependency black to v24.10.0 ([#401](https://github.com/engineervix/ten-lists/issues/401)) ([8949ff1](https://github.com/engineervix/ten-lists/commit/8949ff1b2d302b599a606f1fb0f0beb1eb6f69f9))
* **deps-dev:** update dependency bpython to v0.24 ([6f2fdc8](https://github.com/engineervix/ten-lists/commit/6f2fdc81e75a77387c56a2c3d67c7e89afe7291c))
* **deps-dev:** update dependency commitizen to v3.29.1 ([6ff9481](https://github.com/engineervix/ten-lists/commit/6ff948171f263b4199d111085a8527aef56215af))
* **deps-dev:** update dependency commitizen to v3.31.0 ([#402](https://github.com/engineervix/ten-lists/issues/402)) ([d129873](https://github.com/engineervix/ten-lists/commit/d12987379bbe0d424761406c725c5a1b285eddfb))
* **deps-dev:** update dependency faker to v8.16.0 ([174a045](https://github.com/engineervix/ten-lists/commit/174a045f478f4f54dd1ade2ee74dca039dc0d157))
* **deps-dev:** update dependency gtts to v2.5.3 ([2d27fba](https://github.com/engineervix/ten-lists/commit/2d27fba608762ced758939a007806544fc6e1b4c))
* **deps-dev:** update dependency gtts to v2.5.4 ([#399](https://github.com/engineervix/ten-lists/issues/399)) ([3fb7543](https://github.com/engineervix/ten-lists/commit/3fb754387aa67a144ee0eea232092fe7ff72993e))
* **deps-dev:** update dependency pre-commit to v2.21.0 ([c15e451](https://github.com/engineervix/ten-lists/commit/c15e451b818f8c99e79dcb455bf9ff139949e4ad))
* **deps-dev:** update dependency pyupgrade to v3.19.0 ([#403](https://github.com/engineervix/ten-lists/issues/403)) ([414c794](https://github.com/engineervix/ten-lists/commit/414c79443fc89971909a90b552862df7f152fc9c))
* **deps-dev:** update dependency ruff to v0.6.4 ([87d5efa](https://github.com/engineervix/ten-lists/commit/87d5efa4fb81876a7e7d031c6bf0cb6e7e34d31b))
* **deps-dev:** update dependency ruff to v0.6.6 ([28d7512](https://github.com/engineervix/ten-lists/commit/28d75120d069a26bb957d2e54ee81d26e1495409))
* **deps-dev:** update dependency ruff to v0.6.8 ([871c879](https://github.com/engineervix/ten-lists/commit/871c8797dbe548643b06296f4931dd2909448b71))
* **deps-dev:** update dependency ruff to v0.7.4 ([#404](https://github.com/engineervix/ten-lists/issues/404)) ([30e7cd7](https://github.com/engineervix/ten-lists/commit/30e7cd7caf9d39033cf05c2d8b8ca8540c2cd498))
* **deps-dev:** update dependency ruff to v0.8.2 ([#410](https://github.com/engineervix/ten-lists/issues/410)) ([5db7cec](https://github.com/engineervix/ten-lists/commit/5db7cece5f4f09e06aedacbb586c2c6dfc0baf31))
* **deps-dev:** update dependency ruff to v0.8.3 ([#412](https://github.com/engineervix/ten-lists/issues/412)) ([19e4945](https://github.com/engineervix/ten-lists/commit/19e494588aa14cbd5c23c1cc786e3bc10337695e))
* **deps-dev:** update dependency sentry-sdk to v2.14.0 ([873f276](https://github.com/engineervix/ten-lists/commit/873f27645ebb75c5d6b2107cc04cefe83aa07837))
* **deps-dev:** update dependency sentry-sdk to v2.18.0 ([#405](https://github.com/engineervix/ten-lists/issues/405)) ([40c4de2](https://github.com/engineervix/ten-lists/commit/40c4de257a62cd47f46c3722137e219aa964f7e5))
* **deps-dev:** update dependency sentry-sdk to v2.19.2 ([#411](https://github.com/engineervix/ten-lists/issues/411)) ([26f8f65](https://github.com/engineervix/ten-lists/commit/26f8f650ccdc9e22c07b674cdc3950bcd36ffb01))
* **deps-dev:** update dependency setuptools to v74.1.2 ([8edaeca](https://github.com/engineervix/ten-lists/commit/8edaecad06d6304e208be5361dee591f139c14c6))
* **deps-dev:** update dependency setuptools to v74.1.3 ([6499b5d](https://github.com/engineervix/ten-lists/commit/6499b5d50dd9bd3c7e43da6b91bd119b8ebef607))
* **deps-dev:** update dependency tomli to v2.1.0 ([#406](https://github.com/engineervix/ten-lists/issues/406)) ([af9ccc3](https://github.com/engineervix/ten-lists/commit/af9ccc3fed921c6e074f1da29dae500fed62a9bf))
* **deps-dev:** update dependency tomli to v2.2.1 ([#413](https://github.com/engineervix/ten-lists/issues/413)) ([d697873](https://github.com/engineervix/ten-lists/commit/d697873603e79d9d9c4b35561887b7eddf97b986))
* **deps-dev:** update dependency tqdm to v4.67.0 ([#407](https://github.com/engineervix/ten-lists/issues/407)) ([4f95a6e](https://github.com/engineervix/ten-lists/commit/4f95a6eb4009ce331ad954684b794e9b581af54c))
* **deps-dev:** update dependency tqdm to v4.67.1 ([#409](https://github.com/engineervix/ten-lists/issues/409)) ([589f9e1](https://github.com/engineervix/ten-lists/commit/589f9e1cd69fb215bb91295706d8153a1609e6ce))
* **deps:** update dependency colorama to v0.4.6 ([656198d](https://github.com/engineervix/ten-lists/commit/656198d190aed46532ed5c4d7191e541a224ef40))
* **deps:** update dependency eyed3 to v0.9.7 ([b299353](https://github.com/engineervix/ten-lists/commit/b29935392edd731dcf9f0899b731d2572b1af1c7))
* **deps:** update dependency flask-debugtoolbar to v0.16.0 ([#400](https://github.com/engineervix/ten-lists/issues/400)) ([084e21e](https://github.com/engineervix/ten-lists/commit/084e21ee40b53d08ae0440d4fd58d3fae17c3440))
* **deps:** update dependency flask-httpauth to v4.8.0 ([778d284](https://github.com/engineervix/ten-lists/commit/778d2843e92ae0625481a138a6a7376d72f1e0a9))
* **deps:** update dependency flask-mail to v0.10.0 ([fdf1b5c](https://github.com/engineervix/ten-lists/commit/fdf1b5cb2f1a661bb7e34668651eca7311d2ee6b))
* **deps:** update dependency flask-moment to v1.0.6 ([8c5ea96](https://github.com/engineervix/ten-lists/commit/8c5ea961097cd1b087f90867f919ec137b070365))
* **deps:** update dependency flask-restful to v0.3.10 ([1dfe973](https://github.com/engineervix/ten-lists/commit/1dfe973a349b6928406f3ac767d05bb0f9e5e84c))
* **deps:** update dependency flask-talisman to v1.1.0 ([4f3bf9a](https://github.com/engineervix/ten-lists/commit/4f3bf9aa4518d19af76453b4d60a01925dec79e7))
* **deps:** update dependency pytest-flask to v1.3.0 ([de83cdb](https://github.com/engineervix/ten-lists/commit/de83cdb4e070b5ef714738f9fef3deacb79c3ff6))
* **deps:** update dependency python-dotenv to v0.21.1 ([84c566d](https://github.com/engineervix/ten-lists/commit/84c566d8c73e6ecaf081712f3826b04c0481fd75))
* flask-script isn't used ([54d7b1d](https://github.com/engineervix/ten-lists/commit/54d7b1dcfb347f050429f87cd31f9b01e5a17add))
* improve docker setup ([7c10ce1](https://github.com/engineervix/ten-lists/commit/7c10ce167e78e8080ac9857117d1b55891b92b0f))
* specify Node version ([c68a1b6](https://github.com/engineervix/ten-lists/commit/c68a1b6d4e1a93ae5c942a5683a1bf59c7d5ca30))
* switch to Node.js 16 ([cb1e892](https://github.com/engineervix/ten-lists/commit/cb1e892ee94be7925182d6f1b90f4de2aae5dbc3))
* switch to poetry ([88ab13f](https://github.com/engineervix/ten-lists/commit/88ab13fb678b659b807a5147ef7b706e1f748023))
* we don't need libpq-dev ([29fd5df](https://github.com/engineervix/ten-lists/commit/29fd5df844c7d03778de3b7abafa5c3024f86f45))

## [v1.0.1](https://github.com/engineervix/ten-lists/compare/v1.0.0...v1.0.1) (2022-09-30)


### 🚀 Features

* set up HTTP security headers ([2652a91](https://github.com/engineervix/ten-lists/commit/2652a911a7780c62b3579eb32f7ea15b80c0704b))


### 🐛 Bug Fixes

* add missing kwarg `content_security_policy` in Talisman init_app ([432cbdf](https://github.com/engineervix/ten-lists/commit/432cbdf289a986a5d9693c4d468346c8913e9025))
* broken HTTP security headers configuration ([be42945](https://github.com/engineervix/ten-lists/commit/be429453fd34565f5a43b89d8a9a615d7681d80c))
* change `permission_policy` to `permissions_policy` in flask-talisman config ([f6d363b](https://github.com/engineervix/ten-lists/commit/f6d363bfb73c159b9ae05debd6951027b6af4150))
* cleanup Content Security Policy config ([18ef459](https://github.com/engineervix/ten-lists/commit/18ef459131655a16497d4cac29365ea8cbdc1972))
* rewrite `autoplay` permissions_policy ([82bea8b](https://github.com/engineervix/ten-lists/commit/82bea8b8328000f5ed59ba50e749b8db98f4dfee))


### 📝 Docs

* add TODO item concerning CDN setup for mp3 files ([5fa653e](https://github.com/engineervix/ten-lists/commit/5fa653eb8e284a1c58111f1aec9045881b6255b8))

## [v1.0.0](https://github.com/engineervix/ten-lists/compare/v0.6.3...v1.0.0) (2022-09-30)


### ⚠ BREAKING CHANGES

* For the web app, it is now recommended to have files in the cloud, instead of
locally

### 🚀 Features

* install gunicorn & add production deployment config for Dokku ([6287f8f](https://github.com/engineervix/ten-lists/commit/6287f8f2e6433db28cd44bb8a08ccf723f0d1511))
* remove metadata fetching using ffprobe ([85016e6](https://github.com/engineervix/ten-lists/commit/85016e66c9d0775f13a1e0fd5ef0192a9be50bd1))
* store the mp3 files in the cloud and use ffprobe to get metadata ([d475e87](https://github.com/engineervix/ten-lists/commit/d475e87246290561f0411e51e18545c19c6e3d38))


### ✅ Tests

* fix broken webapp test ([acc1f58](https://github.com/engineervix/ten-lists/commit/acc1f583b22cd5b0e96f49c4627f9f5c24012e70))


### ♻️ Code Refactoring

* do not load .prod.env in production ([f493a0d](https://github.com/engineervix/ten-lists/commit/f493a0d51164fbfe47ca1fe364112994c8255ac5))


### 👷 CI/CD

* add TENLISTS_MP3_CLOUD_STORAGE_BASE_URL environment variable to test job ([78c3f3f](https://github.com/engineervix/ten-lists/commit/78c3f3fa3aac404a496557df3a0f703e495d22eb))
* fix broken github actions test job ([ccac365](https://github.com/engineervix/ten-lists/commit/ccac365c02719771d525b45fb3e136b1bb289dc2))
* fix broken test ([f2f2f76](https://github.com/engineervix/ten-lists/commit/f2f2f76cc740fdb8d0f6c7b2095338088274693c))
* fix typo in circleci workflow ([ba604d5](https://github.com/engineervix/ten-lists/commit/ba604d54ab3082004a9ca5d44c719a765a53934c))


### 📝 Docs

* update README with info on mp3 files & cloud storage ([6461716](https://github.com/engineervix/ten-lists/commit/64617163207ab7d4ed4ae178439d0d96cf0a4a8a))


### ⚙️ Build System

* **deps-dev:** install bpython ([e502fce](https://github.com/engineervix/ten-lists/commit/e502fcecb4f4c22bfe4684d24fd120fa16f36858))
* **deps:** install ffmpeg ([48cf8ae](https://github.com/engineervix/ten-lists/commit/48cf8ae57e441908999ff7fa8cabe83b8cde682d))
* **docker:** ensure that node_modules/.bin is in PATH ([35e163d](https://github.com/engineervix/ten-lists/commit/35e163d8a97ed438ebe39dbc68bb24efc5670c6b))
* **docker:** fix Dockerfile ([a69937b](https://github.com/engineervix/ten-lists/commit/a69937b4c793b1ad4cbd61f3f2a3fb16833f0329)), closes [/github.com/dokku/dokku/issues/2742#issuecomment-351405317](https://github.com/engineervix//github.com/dokku/dokku/issues/2742/issues/issuecomment-351405317)
* RUN npm install -g grunt-cli ([5c2a08b](https://github.com/engineervix/ten-lists/commit/5c2a08b0f5addc2405eb43c295168e8f1f7bcd63))
* update .dockerignore file ([181d0a4](https://github.com/engineervix/ten-lists/commit/181d0a49a812221053df5c7ee49f133036d86c61))
* use `npm run build` instead of calling individual Grunt tasks ([4f5efc6](https://github.com/engineervix/ten-lists/commit/4f5efc6ada711f243a87c46571c468f8c3647746))

## [v0.6.3](https://github.com/engineervix/ten-lists/compare/v0.6.2...v0.6.3) (2022-09-27)


### 🐛 Bug Fixes

* add configuration for npm as well ([84e25c3](https://github.com/engineervix/ten-lists/commit/84e25c326df41f3e8a9c83d79f1c510c59d1b638))
* Name doesn’t conform to conventions ([dfa7300](https://github.com/engineervix/ten-lists/commit/dfa73006bcd43f78f8e347b7dde0969b339d0459))
* One-line docstring should fit on one line with quotes ([de92f8d](https://github.com/engineervix/ten-lists/commit/de92f8dc2e62d7543bea444f27de5e6d7b3119e2))
* put correct labels ([7d3c3fb](https://github.com/engineervix/ten-lists/commit/7d3c3fb65e4855d28ac062f581effeaacbf5e120))
* remove non-existent reference to favicon.png in template ([bc81283](https://github.com/engineervix/ten-lists/commit/bc81283ab340be090c62864aba960beec09eca92))
* requirements.txt to reduce vulnerabilities ([e9ed814](https://github.com/engineervix/ten-lists/commit/e9ed814040e12cc767d5b3f97b7d6a7f5f1f211b))
* requirements.txt to reduce vulnerabilities ([c0a6730](https://github.com/engineervix/ten-lists/commit/c0a6730a39df8c54f1c26e1f75859c750fd88015))
* requirements.txt to reduce vulnerabilities ([d7d8f56](https://github.com/engineervix/ten-lists/commit/d7d8f563f22b823c1e932cae60d9c748df5128e0))
* requirements.txt to reduce vulnerabilities ([b1bfdf0](https://github.com/engineervix/ten-lists/commit/b1bfdf0209a84fb0c7674b86b24b6ffaedbfb25d))
* requirements.txt to reduce vulnerabilities ([0cef07a](https://github.com/engineervix/ten-lists/commit/0cef07a274befae4e6086b6726c2e220cd758407))
* requirements.txt to reduce vulnerabilities ([e5dd48e](https://github.com/engineervix/ten-lists/commit/e5dd48ee08a6e4f5db21fbcaee98f9ff53dda976))


### ♻️ Code Refactoring

* avoid too many return statements within function ([678a233](https://github.com/engineervix/ten-lists/commit/678a2339d0a0dd0838a560e3043a7d59fc173d49))
* move env variables to repository root ([b3beab3](https://github.com/engineervix/ten-lists/commit/b3beab38550bc25607a5ac031c157391c0c26b29))
* only initialize debugtoolbar if app.debug is True ([c247c3d](https://github.com/engineervix/ten-lists/commit/c247c3d59eb73bfc38ae108de1d71e83747dc7e8))
* **package.json:** refactor to suit current setup ([3155340](https://github.com/engineervix/ten-lists/commit/3155340bd2f6b0aed6c35ebe9ac1bcbc829b329d))
* rearrange the project structure ([ba01c1c](https://github.com/engineervix/ten-lists/commit/ba01c1c6d00acaed4f4bbbcde3270df8d218ac58))
* reduce cognitive complexity ([ed7621a](https://github.com/engineervix/ten-lists/commit/ed7621a41281c61103c79cbc181e5aa89c3cf147))
* remove else after try..except ([e53cb61](https://github.com/engineervix/ten-lists/commit/e53cb6168b431f0b43c94611a93aac6be1279dd0))
* rename project to **ten-lists** ([#104](https://github.com/engineervix/ten-lists/issues/104)) ([579f6c6](https://github.com/engineervix/ten-lists/commit/579f6c6e484362a8c9e6a15b34b5879bc2e64805))
* update references to env variables in config ([5693c14](https://github.com/engineervix/ten-lists/commit/5693c148d2f718ad6eabb76569d7f47bd3ecd14c))
* **webapp:** refactor code and write simple test using pytest-flask ([00cae26](https://github.com/engineervix/ten-lists/commit/00cae2663ddc4b7bb2268bd2bf76027bc6adda64))


### 💄 Styling

* run black, isort and flake8 on entire codebase ([0c1d8d1](https://github.com/engineervix/ten-lists/commit/0c1d8d1c4d73ed4acc26f59866d774eaee49b8f2))


### ⚙️ Build System

* **deps-dev:** [Snyk] Security upgrade py from 1.9.0 to 1.10.0 ([d1e39c0](https://github.com/engineervix/ten-lists/commit/d1e39c09ca1a99091ce0a4242aaeada11a4b76b1)), closes [#138](https://github.com/engineervix/ten-lists/issues/138)
* **deps-dev:** add isort ([26a7df0](https://github.com/engineervix/ten-lists/commit/26a7df0b553735ec05ee6563ea1539da2e2a2811))
* **deps-dev:** bump black from 21.7b0 to 21.12b0 ([6465b27](https://github.com/engineervix/ten-lists/commit/6465b27e4fa1f828d201b77d7c7d3614670d163b))
* **deps-dev:** bump black to 21.7b0 ([fcf9240](https://github.com/engineervix/ten-lists/commit/fcf9240ec02050d6bdd0e0a5ca5af450e0bcc6ca))
* **deps-dev:** bump clean-css from 5.1.2 to 5.1.3 ([#269](https://github.com/engineervix/ten-lists/issues/269)) ([2981d45](https://github.com/engineervix/ten-lists/commit/2981d459f06c6e9bba207d9b3d67ef732d5d51a3))
* **deps-dev:** bump faker from 8.8.2 to 8.10.0 ([#274](https://github.com/engineervix/ten-lists/issues/274)) ([28d843f](https://github.com/engineervix/ten-lists/commit/28d843fcf2dc9f82495dc4788e96099610d57043))
* **deps-dev:** bump grunt from 1.2.1 to 1.3.0 ([f2504f1](https://github.com/engineervix/ten-lists/commit/f2504f11c20f03d6a28b8fc2552f6ff93a44a9f7))
* **deps-dev:** bump grunt from 1.2.1 to 1.3.0 ([855b8d2](https://github.com/engineervix/ten-lists/commit/855b8d2d3d5e7298439e904b54411a14029ceb0f))
* **deps-dev:** bump grunt-contrib-cssmin from 3.0.0 to 4.0.0 ([820757f](https://github.com/engineervix/ten-lists/commit/820757f1c51f16b1ffa718b7da0949f14afce4ae))
* **deps-dev:** bump gtts from 2.2.2 to 2.2.3 ([#264](https://github.com/engineervix/ten-lists/issues/264)) ([0a74da8](https://github.com/engineervix/ten-lists/commit/0a74da8039af9a6be35ce38959236cb9780c0097))
* **deps-dev:** fix vulnerabilities using npm audit fix ([5031d6e](https://github.com/engineervix/ten-lists/commit/5031d6ed31cc574b33ea0b02577115d52f50d933))
* **deps-dev:** install invoke and commitizen ([1396874](https://github.com/engineervix/ten-lists/commit/1396874820313c8594e485d927486e228e25080b))
* **deps-dev:** npm install cross-env -D ([a62e021](https://github.com/engineervix/ten-lists/commit/a62e021970c08ff4d039af521319a081694f89e4))
* **deps-dev:** update dependency clean-css to v5.1.5 ([#310](https://github.com/engineervix/ten-lists/issues/310)) ([a54030c](https://github.com/engineervix/ten-lists/commit/a54030c1b58226cc096a62373cf3bc13f5698bb2))
* **deps-dev:** update dependency doc8 to v0.9.0 ([7ea2d2d](https://github.com/engineervix/ten-lists/commit/7ea2d2dc5af94633c5bb98fb9fbc4a43c46fdcf1))
* **deps-dev:** update dependency faker to v8.10.1 ([c1c6d0a](https://github.com/engineervix/ten-lists/commit/c1c6d0af1c7a993096a282caebd746010b052ba4))
* **deps-dev:** update dependency faker to v8.10.2 ([a89e7c2](https://github.com/engineervix/ten-lists/commit/a89e7c2ffecda7cc57e141c1e6b582ba93efe28c))
* **deps-dev:** update dependency faker to v8.10.3 ([f909040](https://github.com/engineervix/ten-lists/commit/f90904056cd3d3e36fa6b3985ca5ed29e0593779))
* **deps-dev:** update dependency faker to v8.11.0 ([fe35420](https://github.com/engineervix/ten-lists/commit/fe3542019cdc63ad143c0570c4b982b3b031b0a9))
* **deps-dev:** update dependency gtts to v2.2.3 ([7633536](https://github.com/engineervix/ten-lists/commit/7633536cbfca258e08e83be9376ae8560e7c77c4))
* **deps-dev:** update dependency pre-commit to v2.14.0 ([e91927f](https://github.com/engineervix/ten-lists/commit/e91927f8713f1925b43b73613dbd7760f39184c0))
* **deps-dev:** update dependency sentry-sdk to v1.3.0 ([87ee9e7](https://github.com/engineervix/ten-lists/commit/87ee9e7a130ac538b4da6a1b07e85eb188624583))
* **deps-dev:** update dependency sentry-sdk to v1.3.1 ([ba5c11a](https://github.com/engineervix/ten-lists/commit/ba5c11a8b11b88c178d15790d9957084c440debc))
* **deps-dev:** update dependency tqdm to v4.61.2 ([d8bef01](https://github.com/engineervix/ten-lists/commit/d8bef0165cfb58218c7321b685c74dc71aae97ec))
* **deps-dev:** update dependency tqdm to v4.62.0 ([f56cf5b](https://github.com/engineervix/ten-lists/commit/f56cf5b7d4da4e6227455f93feaa4ad94622d3fa))
* **deps:** bump autopep8 from 1.5.4 to 1.5.5 ([b82c134](https://github.com/engineervix/ten-lists/commit/b82c134620ed19172e88ab34047888661b56c9d0))
* **deps:** bump autopep8 from 1.5.5 to 1.5.7 ([feda8e1](https://github.com/engineervix/ten-lists/commit/feda8e1b04a55c4a2267df9a3fe8f4b6ce1e8e88))
* **deps:** bump black from 20.8b1 to 21.5b1 ([05881db](https://github.com/engineervix/ten-lists/commit/05881db8da54362497d538a6b72faa1655a07e94))
* **deps:** bump black from 21.5b1 to 21.5b2 ([1b942a8](https://github.com/engineervix/ten-lists/commit/1b942a88f6b0d554927eabb98abd53078eceec99))
* **deps:** bump black from 21.5b2 to 21.6b0 ([#258](https://github.com/engineervix/ten-lists/issues/258)) ([e478763](https://github.com/engineervix/ten-lists/commit/e478763b64de75288d114679230d97722ad28cf7))
* **deps:** bump bootstrap from 4.3.1 to 4.6.0 ([#228](https://github.com/engineervix/ten-lists/issues/228)) ([86cad0b](https://github.com/engineervix/ten-lists/commit/86cad0b570541ffb53fc6a1937f131d9c13bdc16))
* **deps:** bump bpython from 0.20.1 to 0.21 ([561f34f](https://github.com/engineervix/ten-lists/commit/561f34f5c11c243a25a26646aba2f6f8e61ce9fb))
* **deps:** bump faker from 5.4.0 to 5.5.0 ([32dd750](https://github.com/engineervix/ten-lists/commit/32dd75096b903c143014244ddf141278801b1cf4))
* **deps:** bump faker from 5.5.0 to 5.5.1 ([2420048](https://github.com/engineervix/ten-lists/commit/24200480d5999913d73010d99d25740f980cd543))
* **deps:** bump faker from 5.5.1 to 5.6.0 ([003afeb](https://github.com/engineervix/ten-lists/commit/003afebe815b2e56574f56fe2ccd5d26f91448e1))
* **deps:** bump faker from 5.6.0 to 5.6.1 ([d775658](https://github.com/engineervix/ten-lists/commit/d775658c31be13e975dd4b981336c1cb245cd6b5))
* **deps:** bump faker from 5.6.1 to 5.6.3 ([69ebd9b](https://github.com/engineervix/ten-lists/commit/69ebd9bc62ea888eac03409aa7cc5c7a7331e1d6))
* **deps:** bump faker from 5.6.3 to 5.6.5 ([25a8ef5](https://github.com/engineervix/ten-lists/commit/25a8ef5b2418284cf6287f986b702718f0d6fe89))
* **deps:** bump faker from 5.6.5 to 5.7.0 ([b84ded5](https://github.com/engineervix/ten-lists/commit/b84ded5ba798e01e99768ffc4fdeaa9423afd139))
* **deps:** bump faker from 5.7.0 to 5.8.0 ([20913e7](https://github.com/engineervix/ten-lists/commit/20913e7816e3397bf5792678c02b53761917903d))
* **deps:** bump faker from 8.1.3 to 8.2.0 ([bf161f0](https://github.com/engineervix/ten-lists/commit/bf161f0c1302c50e6208c1fa33b13fda9b05fabe))
* **deps:** bump faker from 8.8.0 to 8.8.2 ([#268](https://github.com/engineervix/ten-lists/issues/268)) ([7d755de](https://github.com/engineervix/ten-lists/commit/7d755de2ee9d5f696060c10ed41f271bdb649782))
* **deps:** bump flask-httpauth from 4.2.0 to 4.3.0 ([f1b10e4](https://github.com/engineervix/ten-lists/commit/f1b10e4a0e9afed4761b504b8269c7cdc579e250))
* **deps:** bump flask-httpauth from 4.3.0 to 4.4.0 ([d889cbd](https://github.com/engineervix/ten-lists/commit/d889cbd2f26aaf7c35e13c7906c4565d4b587e08))
* **deps:** bump holderjs from 2.9.7 to 2.9.9 ([416b735](https://github.com/engineervix/ten-lists/commit/416b7357843917bf7db03d0a5e77ffed357571dc))
* **deps:** bump jquery from 3.5.1 to 3.6.0 ([#226](https://github.com/engineervix/ten-lists/issues/226)) ([566059c](https://github.com/engineervix/ten-lists/commit/566059c53e37c217071d030fb47e10daa897413a))
* **deps:** bump pip-chill from 1.0.0 to 1.0.1 ([39289e2](https://github.com/engineervix/ten-lists/commit/39289e26d1f34de5e94ead70888acb88dafee340))
* **deps:** bump pip-tools from 6.1.0 to 6.2.0 ([#266](https://github.com/engineervix/ten-lists/issues/266)) ([681cbf5](https://github.com/engineervix/ten-lists/commit/681cbf55acf964145d95815a7ccb71f41728070f))
* **deps:** bump pre-commit from 2.9.3 to 2.10.0 ([c9e0819](https://github.com/engineervix/ten-lists/commit/c9e08195418d071863039c435d86c53acaf94090))
* **deps:** bump pytest-cov from 2.10.1 to 2.11.0 ([1811a7a](https://github.com/engineervix/ten-lists/commit/1811a7a57c50e8a61d25d02dcf1a33628be21d21))
* **deps:** bump pytest-cov from 2.11.0 to 2.11.1 ([9db260d](https://github.com/engineervix/ten-lists/commit/9db260d8dea43dacb727f7e7a7bb4a90698a80a6))
* **deps:** bump pytest-cov from 2.11.1 to 2.12.0 ([84a2cfb](https://github.com/engineervix/ten-lists/commit/84a2cfbead9d3aa3a0665833d7eebf76dac7d648))
* **deps:** bump python packages ([1c04f88](https://github.com/engineervix/ten-lists/commit/1c04f883f11d69f94783d860fd706418738e8b73))
* **deps:** bump python-dotenv from 0.15.0 to 0.17.1 ([06770e3](https://github.com/engineervix/ten-lists/commit/06770e329d1c706721b831ba1f6ccf74a46cbd93))
* **deps:** bump python-dotenv from 0.17.1 to 0.18.0 ([#265](https://github.com/engineervix/ten-lists/issues/265)) ([db2a8a5](https://github.com/engineervix/ten-lists/commit/db2a8a577e16e63a550bb189fd41eb23a66c21dd))
* **deps:** bump sentry-sdk[flask] from 0.19.5 to 1.1.0 ([85df934](https://github.com/engineervix/ten-lists/commit/85df934d86905ca2a72e156d89af95469fb7b451))
* **deps:** bump sentry-sdk[flask] from 0.19.5 to 1.1.0 ([9e645a4](https://github.com/engineervix/ten-lists/commit/9e645a4eebe46bcf25de9e3fe153f24d8a779670))
* **deps:** bump sentry-sdk[flask] from 1.1.0 to 1.3.0 ([#275](https://github.com/engineervix/ten-lists/issues/275)) ([147235f](https://github.com/engineervix/ten-lists/commit/147235fdd963d8d034c8e4db40ad10650c5d20ac))
* **deps:** bump some outdated python dependencies ([c60e8fa](https://github.com/engineervix/ten-lists/commit/c60e8faf903f0e00f49650990f45748b63b9d977))
* **deps:** bump tqdm from 4.55.1 to 4.56.0 ([fe50556](https://github.com/engineervix/ten-lists/commit/fe50556c8657e521914781a7e2e8406ee45c6082))
* **deps:** bump tqdm from 4.61.1 to 4.61.2 ([#273](https://github.com/engineervix/ten-lists/issues/273)) ([e6f34df](https://github.com/engineervix/ten-lists/commit/e6f34df8c036573689feacea3937040a178d774a))
* **deps:** pin markupsafe==2.0.1 ([ec6d15e](https://github.com/engineervix/ten-lists/commit/ec6d15e5d218e9179aa1fc98ec68a74ebfc966bf))
* **deps:** update dependency flask to v1.1.4 ([f90ea2f](https://github.com/engineervix/ten-lists/commit/f90ea2fd74dae180cc6e44e1b3f30d958a997a51))
* **deps:** update dependency flask-moment to v1.0.2 ([1a4076a](https://github.com/engineervix/ten-lists/commit/1a4076a3dcf13863ba58c564989d0e94b08e2836))
* **deps:** update dependency python-dotenv to v0.18.0 ([46ba511](https://github.com/engineervix/ten-lists/commit/46ba5119e4e1bbd8ebe83eecfd86d97df7f9d11e))
* **deps:** update dependency python-dotenv to v0.19.0 ([89c923a](https://github.com/engineervix/ten-lists/commit/89c923aa075372c5c30b5b6e5d9a05ad8b92212e))
* **deps:** update Node.js dependencies ([2a9c2e7](https://github.com/engineervix/ten-lists/commit/2a9c2e7b6ded8d79fd131983c08cafefbe8c3b63))
* dockerize project ([752fe86](https://github.com/engineervix/ten-lists/commit/752fe8680d4b9e2111e07c57d46f0835f284d6f3))
* install & configure standard-version, commitizen, cz-conventional-changelog ([630bb7a](https://github.com/engineervix/ten-lists/commit/630bb7a72b2b8b7c7df7eb7b165987b2d81a4666))
* refactor Gruntfile to suit updated setup ([51db7b9](https://github.com/engineervix/ten-lists/commit/51db7b91d80f5053172eb332afbc8c454d949172))
* streamline dependencies using pip-chill ([de84186](https://github.com/engineervix/ten-lists/commit/de8418675a287396fdd8c2f0ee69d5123bde5b35))
* update Gruntfile Browsersync task and run prettier ([d811de6](https://github.com/engineervix/ten-lists/commit/d811de6d0abdb06e49436dc1f63af3bc4506d9c1))


### 👷 CI/CD

* add Codacy Coverage Reporter ([94e6de5](https://github.com/engineervix/ten-lists/commit/94e6de550750bc05d97073aaa4c43bc030dff14d))
* add codeclimate configuration ([e4eb74d](https://github.com/engineervix/ten-lists/commit/e4eb74dd4243f4fe09a585a6db6cefe852ecdaed))
* add dependencies label to pin update type ([4a3a173](https://github.com/engineervix/ten-lists/commit/4a3a1734b8d5eb96c45882cdc9d3344acf14d06c))
* add docker to renovate configuration ([1dc40ac](https://github.com/engineervix/ten-lists/commit/1dc40acde3251260695922b8a1a3161e3ff88ddd))
* add GitHub Actions release job ([ebfdf93](https://github.com/engineervix/ten-lists/commit/ebfdf93e94c993729603331d5df6b42e3faa16cc))
* add linting tasks ([#287](https://github.com/engineervix/ten-lists/issues/287)) ([345dfe3](https://github.com/engineervix/ten-lists/commit/345dfe3b3e9d9eaefa1fdd13f0aadc101d03d0e6))
* add renovate.json ([#276](https://github.com/engineervix/ten-lists/issues/276)) ([ddddb13](https://github.com/engineervix/ten-lists/commit/ddddb13fb505a36408d17731d6e4b8cca5af8116))
* automerge pin update types ([6fcee42](https://github.com/engineervix/ten-lists/commit/6fcee42f420bbf8358d0f5b09ff38ee01a59a41b))
* configure renovate ([4e34ff1](https://github.com/engineervix/ten-lists/commit/4e34ff11575e2b296d8593b33d7fd06e3c89941d))
* **deps:** update precommit hook pre-commit/pre-commit-hooks to v3.4.0 ([f57279c](https://github.com/engineervix/ten-lists/commit/f57279c796b2c1dd749b9097a53622bc1ced21e5))
* **deps:** update precommit hook pre-commit/pre-commit-hooks to v4 ([#301](https://github.com/engineervix/ten-lists/issues/301)) ([7d1d0a3](https://github.com/engineervix/ten-lists/commit/7d1d0a3e93f94c67cd2010abf9ad597cc97c5561))
* **deps:** update precommit hook pycqa/flake8 to v3.9.2 ([0812664](https://github.com/engineervix/ten-lists/commit/0812664f3fb67c000530b4e1e059bb0703b97dbd))
* fix renovate config ([#285](https://github.com/engineervix/ten-lists/issues/285)) ([e9dedcb](https://github.com/engineervix/ten-lists/commit/e9dedcb0844246fa36ac6099abbc3cbe15b96c82))
* fix renovate config ([#285](https://github.com/engineervix/ten-lists/issues/285)) ([992cd16](https://github.com/engineervix/ten-lists/commit/992cd169493067a53a40ad52f51a30d37cb95b59))
* fix typo (pyest --> pytest) ([6699ff6](https://github.com/engineervix/ten-lists/commit/6699ff6cdc7a0c3987afef8c12e73973b9f1a149))
* initial setup of env variables for tests ([aec6ec1](https://github.com/engineervix/ten-lists/commit/aec6ec1f0e8bc9b6b84d765c9f80e981c07b6b7e))
* install global npm packages as root ([2282eff](https://github.com/engineervix/ten-lists/commit/2282eff9a81f9d3fc451ffd4b3ae7d03792c1bbc))
* remove `dependabot.yml` configuration file ([f5dee2d](https://github.com/engineervix/ten-lists/commit/f5dee2d947c021282a9dde23ebe133241935475c))
* switch from circleci/python:3.7 to cimg/python:3.8-node ([4dbf8d7](https://github.com/engineervix/ten-lists/commit/4dbf8d7e09e7e8f04d24d0f2d70974cb0996a3a4))
* update circleCI config ([76ae8d7](https://github.com/engineervix/ten-lists/commit/76ae8d7763363edd073c8ac026e9451fd161fdda))
* update greeting message for issue submission ([bea69e6](https://github.com/engineervix/ten-lists/commit/bea69e6c296a68f94824edc07a4b6e96b80ec1b0))


### ✅ Tests

* add dirs_exist_ok=True to copytree command ([90fe44d](https://github.com/engineervix/ten-lists/commit/90fe44d506e576c6855a45d91efaf16e7c4d1ec4))
* update coverage configuration ([a1bf839](https://github.com/engineervix/ten-lists/commit/a1bf839db5d45373a2b5e291614818b3f0b4b212))
* write more tests for the webapp ([#286](https://github.com/engineervix/ten-lists/issues/286)) ([31ce52d](https://github.com/engineervix/ten-lists/commit/31ce52dc35fd43eb13760b3cc19a1e56b49e6f3b))


### 📝 Docs

* cleanup changelog in preparation for conventional changelog ([9238cb0](https://github.com/engineervix/ten-lists/commit/9238cb0e449a33a2cfae36a953146be4f370e839))
* hardcode issue URL ([7a57f87](https://github.com/engineervix/ten-lists/commit/7a57f87187739af65eebb18086a9d370bc24a9de))
* **README:** update the docs ([8c0a4ea](https://github.com/engineervix/ten-lists/commit/8c0a4eaf8aa6a4595bd39a39085831c505653287))
* update README ([427cbca](https://github.com/engineervix/ten-lists/commit/427cbca6790e2b49963ed1b981b7459acec08194))
* update README TOC and remove requires.io badge ([a178b3e](https://github.com/engineervix/ten-lists/commit/a178b3e0b621b16214bce60afa59bd5da3bb4c61))


## [v0.6.2](https://github.com/engineervix/ten-lists/compare/v0.6.1...v0.6.2) (2020-01-29)

### Added

- Windows Support

## [v0.6.1](https://github.com/engineervix/ten-lists/compare/v0.6.0...v0.6.1) (2019-09-29)

### Added

- the script now has tests! I'll still add some more tests

## [v0.6.0](https://github.com/engineervix/ten-lists/compare/v0.5.0...v0.6.0) (2019-09-28)

### Changed

- the structure of the code to make it easier to read and test. Far from perfect -- more work still needs to be done.
- switched from [`argparse`](https://docs.python.org/3/library/argparse.html) to [`Click`](https://click.palletsprojects.com/en/7.x/) for the CLI
- the `BIBLE_DIRECTORY` can now be specified through the CLI as an argument, but a default one is provided

### Added

- some fancy terminal enhancements courtesy of [`colorama`](https://github.com/tartley/colorama), [`termcolor`](https://pypi.org/project/termcolor/) and [`pyfiglet`](https://github.com/pwaller/pyfiglet)

## [v0.5.0](https://github.com/engineervix/ten-lists/compare/v0.4.0...v0.5.0) (2019-06-22)

### Changed

- the codebase from `python2` to `python3`.

## [v0.4.0](https://github.com/engineervix/ten-lists/compare/v0.2.0...v0.4.0) (2015-05-11)

### Added

- the ability to change ID3 tag info in the copied files, so that whenever you play the files from any device (eg car, home theatre), the desired order is maintained.
- the ability to rename the files so that their sequence follows the desired reading plan order, instead of the order of appearance in the Bible. Key Modules: eyed3, os.rename

### Changed

- the naming convention of files and directories by enforcing a 3-digit number by padding with zeroes using the `zfill()` function. This was done because I noticed that when I was creating a one week playlist from day 96 to 102; `day100` was considered as occuring before `day96` during processing, which isn't the case. This is because of the `1` after the `day`. Thus, to fix the problem, we need to have `day096` instead of `day96`.

> NOTE: I don't know what happened for v0.3.0 to be skipped! Anyway, these were my early dev days!

## [v0.2.0](https://github.com/engineervix/ten-lists/compare/v0.1.0...v0.2.0) (2014-05-27)

### Added

- the ability to copy (using [shutil](https://docs.python.org/3/library/shutil.html)) the files on the playlist file into a new folder so that you can carry the folder and listen anywhere (car, home theatre, etc).

## [v0.1.0](https://github.com/engineervix/ten-lists/releases/tag/v0.1.0) (2014-05-27)

- Initial version