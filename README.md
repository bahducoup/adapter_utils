### description
* add adapters to `wav2vec2` model instances used in [s3prl](https://github.com/s3prl/s3prl)

### how to use
```
from add_adapters import add_adapters_wav2vec2

add_adapters_wav2vec2(model, adapter_down_dim=192, adapt_layers=[0, 1, 2])
```

* sample code can be found in example.py (`python example.py`)