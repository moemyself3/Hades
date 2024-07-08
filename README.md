# Hades

**HADES** is an astronomical observer's toolbox. It contains a set of tools designed to accomplish a variety of observational tasks, including image processing, aperture photometry, and responding to astronomical alerts.

---

## Usage

The code is run through a set of scripts from the main HADES directory. The scripts currently available include:

- GCN listener (`gcn_listener.py`)
- Limiting magnitude (`limiting_magnitude.py`)
- Quick reduction (`quick_reduction.py`)
- Relative photometry (`relative_photometry.py`)

### Configuration

The settings are controlled in the `config.py` file.

### Example 1: Running the GCN listener

```
$ python -m scripts.gcn_listener
```

### Example 2: Running quick reduction on observational data

```
$ python -m scripts.quick_reduction
```

The toolbox is run on a single night (yyyy-mm-dd) of data, assuming the following directory format:

```
[yyyy-mm-dd]
	[dark]
		[dark-flat]
			image1.fit
			image2.fit
			...
		[dark-obj]
			image1.fit
			image2.fit
			...
	[flat]
		image1.fit
		image2.fit
		...
	[obj]
		image1.fit
		image2.fit
		...
```

---

## Installation

HADES was developed on a machine (`Epimetheus`) running Ubuntu 22.04.4 LTS and using an Anaconda environment with Python 3.12.3. The list of library requirements are listed in the the `requirements.txt` file in the main directory.

---

7 Jun 2019<br>
Last update: 8 Jul 2024

Richard Camuccio<br>
rcamuccio@gmail.com

(Imageredux > CAL > Hades)