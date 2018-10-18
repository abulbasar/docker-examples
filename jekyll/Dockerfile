FROM ubuntu:18.04
RUN apt-get update && \
apt-get install ruby ruby-dev build-essential -y
RUN gem install jekyll bundler
RUN mkdir /blogs && cd /blogs && if [ ! -d "myblog" ]; then jekyll new myblog; fi
WORKDIR /blogs/myblog
EXPOSE 4000
CMD bundle exec jekyll serve --host=0.0.0.0