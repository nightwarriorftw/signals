[![Open Issues](https://img.shields.io/github/issues/nightwarriorftw/signals?style=for-the-badge&logo=github)](https://github.com/nightwarriorftw/signals/issues) [![Forks](https://img.shields.io/github/forks/nightwarriorftw/signals?style=for-the-badge&logo=github)](https://github.com/nightwarriorftw/signals/network/members) [![Stars](https://img.shields.io/github/stars/nightwarriorftw/signals?style=for-the-badge&logo=reverbnation)](https://github.com/nightwarriorftw/signals/stargazers) ![Maintained](https://img.shields.io/maintenance/yes/2021?style=for-the-badge&logo=github) ![Made with Python](https://img.shields.io/badge/Made%20with-Python-blueviolet?style=for-the-badge&logo=python) ![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red?style=for-the-badge&logo=open-source-initiative) ![Built with Love](https://img.shields.io/badge/Built%20With-%E2%99%A5-critical?style=for-the-badge&logo=ko-fi) [![Follow Me](https://img.shields.io/twitter/follow/nightwarriorftw?color=blue&label=Follow%20%40nightwarriorftw&logo=twitter&style=for-the-badge)](https://twitter.com/intent/follow?screen_name=nightwarriorftw) [![Telegram](https://img.shields.io/badge/Telegram-Chat-informational?style=for-the-badge&logo=telegram)](https://telegram.me/nightwarriorftw)


# signals - Django Custom Signals

## :ledger: Index

- [About](#beginner-about)
  - [Commands](#package-commands)
- [Development](#wrench-development)
  - [Pre-Requisites](#notebook-pre-requisites)
  - [Development Environment](#nut_and_bolt-development-environment)
- [Credit/Acknowledgment](#star2-creditacknowledgment)
- [License](#lock-license)

## :beginner: About

A simple project to demonstrate how to signal works in django.

Please refer my blog for more details :)

## :wrench: Development

### :notebook: Pre-Requisites

Signal Dispatcher are nothing but a well known design pattern [Observer Pattern](https://en.wikipedia.org/wiki/Observer_pattern) with just a basic difference that signal is known as `subject` and receiver is known as `observer`.


### :nut_and_bolt: Development Environment

#### 1. Clone the repo

```
git clone https://github.com/nightwarriorftw/signals.git
cd signals
```

#### 2. Setup project

Install [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/). After installing those run the following commands

- build the docker image

```
docker-compose build
```

- run docker-compose

```
docker-compose up
````

It may take some time to pull all images and build them. Be patient :)


#### 4. Makemigrations, migrate and run the server

Open a new terminal and enter the `api` container with the help of the following command

```
docker-compose exec api bash
```

Now, run the following commands :

```
python manage.py makemigrations
python manage.py migrate
```



## :star2: Credit/Acknowledgment
[Aman Verma](https://nightwarriorftw.netlify.app)
  - Github: [nightwarriorftw](https://github.com/nightwarriorftw)
  - Linkedin: [nightwarriorftw](https://linkedin.com/in/nightwarriorftw)
  - Twitter: [nightwarriorftw](https://twitter.com/nightwarriorftw)


Credits goes to me 
## :lock: License

[LICENSE](/LICENSE)
