# Water Jug Riddle

A solution for the classic Water Jug Riddle made famous by the Die Hard 3 movie, written in Python. The riddle involves using two jugs with different capacities (X gallons and Y gallons) to measure exactly Z gallons of water. The application is an API endpoint that provides a step-by-step solution in a JSON response.

## Limitations

- Allowed Actions: Fill, Empty, Transfer (between the two jugs only).
- X, Y and Z are greater than 0
- X, Y and Z are integers (no decimals, fractions)

## Algorithmic Approach

We use a _Naive Approach_, based on the fact that the problem can be solved simply by repeatedly filling from one bucket to the next until it fills up with the desired amount. This gives us two possible solutions (i.e., filling from bucket X to Y or filling from bucket Y to X), and then we choose the best solution of the two. We believe the problem to be simple enough to use this approach; the arithmetics involved in our algorithm are not sufficiently complex (no data structures are used) to affect performance even when using large values or when a substantial number of steps are needed for the outcome. We do, however, know that the problem can be modeled by means of a _Diophantine Equation_, so we check _a priori_ that Z is divisible by the greatest common divisor of X and Y in order to check the problem’s feasibility.

## Running the application

A [Python 3](https://www.python.org/downloads/) installation is the only requirement. To start the server run the following in a terminal:

```
python server.py
```

Please make sure to have port 8000 available.

You can do a POST type request from any method you want, just send a JSON body to `http://localhost:8000/` with the following format (X, Y, Z are case-sensitive):

```
{
  "X": 5,
  "Y": 3,
  "Z": 4
}
```

Example request using Visual Studio Code’s REST client extension:

```
POST http://localhost:8000/ HTTP/1.1
content-type: application/json

{
  "X": 5,
  "Y": 3,
  "Z": 4
}
```

We also provide a simple script `waterjug.py` that takes `X, Y, Z` inputs and does the request for you. To run it:

```
python waterjug.py
```

Example output for values `X=5, Y=4, Z=3`:

```
Enter X value (greater than 0 integer): 5
Enter Y value (greater than 0 integer): 4
Enter Z value (greater than 0 integer): 3
{
    "Values": {
        "X": 5,
        "Y": 4,
        "Z": 3
    },
    "Best Solution": "4 steps",
    "Worst Solution": "10 steps",
    "Best Solution step-by-step": {
        "STEP 1": {
            "X": "0",
            "Y": "4",
            "Explanation": "Fill bucket Y"
        },
        "STEP 2": {
            "X": "4",
            "Y": "0",
            "Explanation": "Transfer from bucket Y to bucket X"
        },
        "STEP 3": {
            "X": "4",
            "Y": "4",
            "Explanation": "Fill bucket Y"
        },
        "STEP 4": {
            "X": "5",
            "Y": "3",
            "Explanation": "Transfer from bucket Y to bucket X. SOLVED"
        }
    }
}
```

## Testing

If you don't feel like manually testing values, we also provide a unit testing script `test.py` (`waterjug.py` needs to be in the same folder) that has several tests already set, with instructions on how to add more in its source code. To run it:

```
python test.py
```

Example output:

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.056s

OK
```

## Contact

[livres@tuta.io](mailto:livres@tuta.io)