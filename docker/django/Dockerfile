ARG UID=1000
ARG PYTHON_VERSION=3.8


FROM python:${PYTHON_VERSION}
ENV POETRY_VERSION=1.1.4 \
    POETRY_VIRTUALENVS_CREATE=0

RUN pip install -U pip && pip install poetry==${POETRY_VERSION}
COPY ./src /src
WORKDIR /src
RUN poetry install --no-dev --no-root && rm -rf /root/.cache


ENV ENV=prod \
    UID=1000 \
    USER=circular \
    PORT=8000 \
    DJANGO_SETTINGS_MODULE=circular.settings \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1  \
    POETRY_VIRTUALENVS_CREATE=0 \
    PATH=${PATH}:.:/home/${USER}/.local/bin


# COPY docker/django/entrypoint.sh /entrypoint.sh

# Add User
RUN groupadd -g ${UID} -r ${USER} && \
    useradd -u ${UID} -r -g ${USER} ${USER} && \
    mkdir -p /home/${USER}/.local && \
    mkdir -p /home/${USER}/.cache && \
    chown -R ${USER} /home/${USER} && \
    mkdir -p /static && chown ${USER} /static && \
    # Test results must be owned by the user
    mkdir /test-results && chown ${USER} /test-results

    # && chmod +x /entrypoint.sh

# ... and make these location persistable
VOLUME [ "/home/${USER}/.local", "/home/${USER}/.cache", "/static", "/test-results"]


USER ${USER}
WORKDIR /src/

# ENTRYPOINT [ "/entrypoint.sh" ]
