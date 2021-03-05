import os
from invoke import task


@task
def clean_dist(c):
    c.run(f'rm -rf dist')

@task
def build_backend(c):
    dist_dir = os.path.join(os.getcwd(), 'dist')
    with c.cd('sources'):
        c.run(f'python setup.py sdist --dist-dir {dist_dir}')

@task
def build_admin_spa(c):
    admin_spa_dir = os.path.join(os.getcwd(), 'admin_site-spa')
    with c.cd(admin_spa_dir):
        c.run('npm run build')
        c.run('cp -rf dist/ ../dist/admin_site-spa/')

@task
def build_static(c):
    c.run('mkdir dist/static')
    c.run('cp -r sources/interfaces/*/static/* dist/static')

@task
def upload_to_stage(c):
    c.run('scp -r dist plates-staging:/opt/sapegin_autoplates_system')

@task(pre=[clean_dist], post=[upload_to_stage])
def build_all(c):
    build_backend(c)
    build_admin_spa(c)
    build_static(c)
