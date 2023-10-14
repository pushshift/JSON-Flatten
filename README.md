This Python script will flatten a nested JSON object (or Python dict).

If you run it directly, it will load an example Youtube object and flatten the keys.

You can also pipe a JSON object into it and get the flattened keys that way.

There are two parameters that can be used to modify the behavior of the flatten method.

The "sep" parameter is the separation character used between each key and child key. This
defaults to ".". 

The "include_values" parameter is a boolean and if set to True will also include the values
of each of the flattened keys.
