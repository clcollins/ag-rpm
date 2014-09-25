ag-rpm
======

**ag**, The Silver Searcher, [\(https://github.com/ggreer/the_silver_searcher\)](https://github.com/ggreer) is a fanstastic, super-fast command-line text search tool like **grep** focused on speed.  Unfortunately, the upstream RPM packages, when I can find them, don't update as quickly as I'd like, so I roll my own RPMs.  This is the spec file I use, and a build script to do it with.

## Building

*Note: This spec file is complete and works, but the build script and documentation in this repository is still being worked on.*

1. `git clone https://github.com/clcollins/ag-rpm.git`
2. `yum install rpm-build rpmdevtools automake pcre pcre-devel ppl cpp mpfr xz-devel zlib zlib-devel`
3. `./build.sh ag`
4. `sudo yum install ~/rpmbuild/RPMS/*/*.rpm`
5. PROFIT!

## Acknowledgements

Thanks to:

* Geoff Greer [\(https://github.com/ggreer\)](https://github.com/ggreer) for writing The Silver Searcher in the first place.  It's *superman* fast.

* Ian Meyer [\(https://github.com/imeyer\)](https://github.com/imeyer) for giving me the idea to do this and the code to base some of this off of (check out his awesome Runit rpm spec file and build script for RHEL-based systems).

## Copyright Information

ag, The Silver Searcher is released by Geoff Greer under the Apache 2.0 license.

This repo, and the .spec file and build script are:

Copyright (C) 2014 Chris Collins

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.

