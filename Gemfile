source 'https://rubygems.org'

gem 'github-pages', '~> 231'
gem 'jekyll', '~> 3.9.0'
gem 'jekyll-sass-converter', '~> 1.5.2'
gem 'liquid', '~> 4.0'
gem 'kramdown', '~> 2.4.0'
gem "webrick"

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
