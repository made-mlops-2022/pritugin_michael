# HomeWork #2

## Local build
### How to build
```bash
docker build . -t online_inference
```
### How to run
```bash
docker run -p 9000:9000 online_inference
```

## Using dockerhub
### How to pull
```bash
docker pull viliars/online_inference:latest
```
## How to run
```bash
docker run -p 9000:9000 viliars/online_inference:latest
```

After running docker we can send requests:
```bash
python send_request.py
```
------

# How to run tests
```bash
pip install -r requirements-dev.txt
```
```bash
python -m unittest test_*
```

# Docker optimization
В первой версии я уже попытался сделать оптимальный Dockerfile. Следуя dockerfile_best-practices я выяснил, что только инструкции RUN, COPY, ADD создают новые слои - которые увеличивают вес контейнера. Поэтому я минимизировал их использование. Также написал .dockerignore файл.

Первая версия image:

[viliars/online_inference:v1.0](https://hub.docker.com/layers/viliars/online_inference/v1.0/images/sha256-4648a926c4cebd1c88b4622e6c3ba5d6fca0b6aa3fa5b907e3827d86dbea674e?context=repo&tab=layers) - COMPRESSED SIZE 644.63 MB

Далее я проанализировал IMAGE LAYERS и выяснил, что самые большие по весу слои - это обновление всех зависимостей в `python:3.10` (187.75 MB) и установка всех зависимостей проекта (309.01 MB). 

Дальнейшую оптимизацию я начал с анализа всех зависимостей на предмет нужности. Оказалось, что для запуска сервиса не нужны все зависимости - оставил только те, без которых сервис не запускался.

Вторая версия image:

[viliars/online_inference:v2.0](https://hub.docker.com/layers/viliars/online_inference/v2.0/images/sha256-e43f9144f27821ad2043d74703717635be9a082dc987f70d29b4ee9033b9ed6d?context=repo) - COMPRESSED SIZE 591.39 MB

Размер слоя установки зависимостей уменьшился с 309.01 MB до 255.77 MB.

Далее я понял, что нужно оптимизировать базовый образ. На официальном dockerhub питона я нашел slim версию.

Третья версия image:

[viliars/online_inference:v3.0](https://hub.docker.com/layers/viliars/online_inference/v3.0/images/sha256-f7d658d542b7af7df0542d873278a0aa69ec017596d113b9a576750c1b7f1e24?context=repo) - COMPRESSED SIZE 301.48 MB

На slim-buster версии:

[viliars/online_inference:v3.2](https://hub.docker.com/layers/viliars/online_inference/v3.2/images/sha256-e66d873bea076b9297128f5d39830876bfe48364b3bf29185672afd543f2a18b?context=repo) - COMPRESSED SIZE 298.94 MB

На alpine версии нужные зависимости не установились, поэтому остановился на slim-buster.

ИТОГ: уменьшение размера более, чем в 2 раза по сравнению с первоначальным image (644.63 MB -> 298.94 MB)