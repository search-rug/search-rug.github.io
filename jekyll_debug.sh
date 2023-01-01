#! /bin/sh
IDu=$(id -u) # UID saves your user id in the ID variable
IDg=$(id -g) # GID

docker run --rm \
 -p 0.0.0.0:4000:4000 \
 --hostname=jekyll \
 --name=jekyll \
 -v $PWD:/srv/jekyll \
 -v $PWD/cache:/usr/local/bundle \
 -v $PWD/build:/srv/jekyll/build \
 -e 'TZ=Europe/Amsterdam' \
 -e JEKYLL_UID=$IDu \
 -e JEKYLL_GID=$IDg \
 jekyll/jekyll \
  jekyll serve --source /srv/jekyll \
  --destination /srv/jekyll/build \
  --disable-disk-cache \
  --watch \
  --force_polling \
