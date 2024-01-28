Example usage of argparse module. Discusses:
- positional arguments
- optional arguments
- mutually exclusive arguments
- subcommands

## Example Usage
`python` refers to the python3 interpreter. Examples should work with any version of python 3.X 
Argparse is a module in the standard library, so no additional installation is required.
```shell script
python 01-basics.py --help

# every "v" increases the verbosity level
python 02-verbosity.py -vv

python 03-argslist.py --mark 1 --move left --two_values 1 2 --zero_or_more abc def ghi --one_or_more 0

# mutually exclusive arguments are not allowed to be used together (--drop vs --select)
python 04-mutually_exclusive.py --host abc.domain.com --user admin --password supersecret --schema my_db --drop

# subcommands ("insert", "select"...) make it possible to have multiple entry points to the same program
python 05-subparsers.py \
  --host abc.domain.com \
  --user admin \
  --password supersecret \
  --schema my_db \
  insert \
  --table my_table \
  --values abc def
```
