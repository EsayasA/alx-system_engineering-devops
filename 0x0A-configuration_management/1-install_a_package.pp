#!/usr/bin/pup
# Install flask with version of (2.1.0)
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
