# Sylvera coding assignment

This repository contains small working example that takes several JSON objects as an input (using a console) interface, then performs some calculations and outputs JSON object containing the final result. Input objects are all validated using Pydantic library. The same library is also used for printing JSON objects to console. The repository also contains an example of the unit test for one of the transformations. 

The code is divided among several files: 
- `Sylvera_rating_calc`: main application script
- `JSON_models`: contains all JSON models (input and output)
- `Transformations`: contains score calculation logic
- `Tests`: contains example of the unit test using `unittest`

The aplication can be started by running `Sylvera_rating_calc.py`

Some ideas for improvement: 
- More tests, so all transformations are properly covered (both happy and negative cases)
- Better excaption handling
- Better interface
- Ruuning the application as a service that exposes REST interface (so it can be called remotely if needed)
- Adding poetry file

**Note**: The code was written using Python 3.12.4 on Windows 11 machine in VS Code.  
