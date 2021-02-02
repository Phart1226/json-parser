import json

def check_char_count(mystr):
	
	""" This is a docstring - it is a descritptive message about what this function is and how to use it """

	assert isinstance(mystr, str), 'Input to this function should be a string'

	if(len(mystr) == 2):
		return(f'{mystr} count passes')
	else:
		return(f'{mystr} count FAILS')

def check_char_type(mystr):
    if (mystr.isalpha() and mystr.isupper()):
        return( f'{mystr} type passes' )
    else:
        return( f'{mystr} type FAILS' )

def check_first_letter(mystr, mystate):
	if(mystr[0] == mystate[0]):
		return(f'{mystr} letter passes')
	else:
		return(f'{mystr} letter FAILS')
def main():
	with open('states.json', 'r') as f:
		states = json.load(f)

	for i in range(50):
		print(check_char_count(states['states'][i]['abbreviation']))
		print(check_char_type(states['states'][i]['abbreviation']))
		print(check_first_letter(states['states'][i]['abbreviation'], states['states'][i]['name']))


if __name__ == '__main__':
    main()
