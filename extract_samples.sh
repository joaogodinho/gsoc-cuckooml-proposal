#!/bin/sh
echo "Creating samples dir..."
mkdir samples
echo "Unpacking samples..."
tar xzf sample.tar.gz -C samples
echo "Removing file 1 (gz with the same 199 samples)"
rm samples/1
