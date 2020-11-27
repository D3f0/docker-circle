from invoke import task


@task()
def docker_build(ctx):
    ctx.run("docker-compose build")


@task()
def docker_shell(ctx, service="django", command=""):
    ctx.run(f"docker-compose run --rm {service} {command}", echo=True, pty=True)

@task()
def poetry_add(ctx, package, development=False):
    with ctx.cd('./src'):
        args = '' if not development else '-D'
        ctx.run(f'poetry add {args} {package}', echo=True, pty=True)


@task()
def poetry_lock(ctx):
    """
    docstring
    """
    with ctx.cd('./src'):
        ctx.run('poetry lock')

@task()
def docker_test(ctx, name='my-tests'):
    ctx.run(f'docker-compose run --name {name} django mkdir /tmp/test-results')
    ctx.run(f'docker-compose run --name {name} django poetry install')
    ctx.run(f'docker-compose run --name {name} django pytest')
    ctx.run(f'docker rm {name}')
