# pythreatgrid
A Python wrapper for the ThreatGrid API

### Installation
Install via PIP
```
pip install pythreatgrid
```

Install from source
```
git clone https://github.com/RustyBower/pythreatgrid.git
cd pythreatgrid
python setup.py install
```

### Usage
```
import pythreatgrid
t = pythreatgrid.ThreatGrid(api_key='API_KEY')
result = t.submit_sample(open('/path/to/executable', 'rb'))
```