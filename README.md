If building fails:

[https://stackoverflow.com/questions/65989040/bundle-exec-jekyll-serve-cannot-load-such-file](https://stackoverflow.com/questions/65989040/bundle-exec-jekyll-serve-cannot-load-such-file)

1. Updated github-pages, jekyll and jekyll-feed gems by running `gem install github-pages`, `gem install jekyll` and `gem install jekyll-feed`. I had to do this step as a simple bundle update wasn't installing the latest version.

2. Modify those gems in the Gemfile to the latest version.

3. Run `bundle update`

4. Finally run `bundle exec jekyll serve`
