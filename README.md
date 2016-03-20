# GSoC CuckooML proposal

So we're given 199 malware reports to start warming up for the real challenge. Since the amount of samples is pretty low, I'll focus on an unsupervised learning method and see if something interesting comes out of it.

Making use of the scientific method, I'll start by formulating hypotheses and see if it holds for the given samples. My first hypothesis is that **malware behaves differently from *regular* software**. My second hypothesis is that **malware will behave differently depending on its purpose**.

Before going any deeper on the hypotheses, I'll try to get a better understanding of the samples, specifically:
- [x] ~~Report's structure~~
- [ ] Type of samples

## Report's structure
- target -- [Metadata about the analyzed file](https://github.com/cuckoosandbox/cuckoo/blob/master/modules/processing/targetinfo.py)
- virustotal -- [Checks for a signature match on virustotal.com (meaning it's not uploaded to virustotal)](https://github.com/cuckoosandbox/cuckoo/blob/master/modules/processing/virustotal.py)
- debug -- [Debug info, for humans](https://github.com/cuckoosandbox/cuckoo/blob/master/modules/processing/debug.py)
- signatures -- [Predefined patterns that might represent a malicious behavior](http://docs.cuckoosandbox.org/en/latest/customization/signatures/)
- buffer -- [Metadata from buffers Cuckoo considered *interesting*](https://github.com/cuckoosandbox/cuckoo/blob/master/modules/processing/buffer.py)
- network -- [Network analysis](https://github.com/cuckoosandbox/cuckoo/blob/master/modules/processing/network.py)
- strings -- [Result of `strings` on file](https://github.com/cuckoosandbox/cuckoo/blob/master/modules/processing/strings.py)
- info -- [Cuckoo metadata](https://github.com/cuckoosandbox/cuckoo/blob/master/modules/processing/analysisinfo.py)
- behavior -- [Result of dynamic analysis](https://github.com/cuckoosandbox/cuckoo/blob/master/modules/processing/behavior.py)
- static -- [Result of static analysis](https://github.com/cuckoosandbox/cuckoo/blob/master/modules/processing/static.py)
- dropped -- [Files created by the malware and Cuckoo](https://github.com/cuckoosandbox/cuckoo/blob/master/modules/processing/dropped.py)

More info in [Processing Modules](http://docs.cuckoosandbox.org/en/latest/customization/processing/).
