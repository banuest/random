#!/usr/bin/env python
#
# SPDX-License-Identifier: BSD-3-Clause
#
# Copyright (c) 2019 Ben Nuest
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#


import os
import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', default=sys.stdin, dest='filename', \
            help='The filename to pull input from')
    parser.add_argument('-o', nargs='?', default=sys.stdout, dest='outfile', \
            help='Filename to write to, default is stdout')
    args = parser.parse_args()
    return args

def read_input(filename):
    """Read the input from the provided filename"""
    if filename == sys.stdin:
        lines = sys.stdin.readlines()
    else:
        with open(filename, 'r') as f:
            lines = f.readlines()
    return lines

def rem_end(lines):
    """Remove the last character from each line"""
    for line in lines:
        line = line[:-1]
    return lines

def write_output(outfile, lines):
    """Write output to the specified file"""
    if outfile == sys.stdout:
        for line in lines:
            sys.stdout.write(line)
    else:
        with open(outfile, 'w') as f:
            for line in lines:
                f.write(line)

if __name__ == '__main__':
    args = parse_args()
    
    filename = args.filename
    outfile = args.outfile

    lines = read_input(filename)
    lines = rem_end(lines)
    write_output(outfile, lines)
