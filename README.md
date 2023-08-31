# Hades

[![Documentation Status](https://readthedocs.org/projects/plouton/badge/?version=latest)](https://plouton.readthedocs.io/en/latest/?badge=latest)

**HADES** is an astronomical image reduction and photometry toolbox.

---

## Usage

### Structure

There are currently six classes in the toolbox:

- Calculator
- Photometer
- Plotter
- Querier
- Reader
- Reducer

All parameters are read from the `config.ini` file.

### File Format

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

### Example 1: Single-Field Reduction

```
$ python script_driver.py
```

### Example 2: Quick Reduction

```
$ python script_quick_reduce.py
```

---

## Installation

---

7 Jun 2019<br>
Last update: 17 Aug 2023

Richard Camuccio<br>
rcamuccio@gmail.com

(Imageredux > CAL > Hades)

Test