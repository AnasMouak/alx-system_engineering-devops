#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:)\S*[A-z]*\b|(?<=to:)\S*[A-z]*\b|(?<=flags:)\S*[A-z]*\b/).join(",")
