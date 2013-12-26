#!/bin/sh
{
    echo "This script requires superuser access to install apt packages."
    echo "You will be prompted for your password by sudo."

    # clear any previous sudo permission
    sudo -k

    # run inside sudo
    sudo sh <<SCRIPT

  # add heroku repository to apt
  echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list

  # install heroku's release key for package verification
  wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

  # update your sources
  apt-get update

  # install the toolbelt
  aptget install libpq-dev
  apt-get install pgadmin3 postgresql-9.3

  # update your sources again
  apt-get update

SCRIPT
}
