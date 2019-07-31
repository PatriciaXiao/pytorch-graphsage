### graphsage

`pytorch` version of https://github.com/williamleif/GraphSAGE

There are also a handful of new features, including:
  - scripts for preprocessing data
  - attention-based aggregator
  - sparse edge sampler (eg, don't use the dense 2D edgelist)
  - richer, pluggable preprocessing classes

This version is missing some features, as well.  Namely:
  - we don't support unsupervised models (yet)

A simplified version of the original Tensorflow version can be found on branch `tf-simple`.

##### LICENSE
MIT

### Personal note (by Patricia)

This piece of code requires the same environment as the official GraphSAGE code, plus pytorch installed.

All prefix of the files need to be deleted.

Run convert first, e.g.:

```shell
python convert.py --inpath ../data/example_data/ --task multilabel_classification
```

then run:
```shell
python train.py --problem-path ./data/example_data/problem.h5 --aggregator-class mean --epochs 2
```

