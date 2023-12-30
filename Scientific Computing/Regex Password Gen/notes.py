# The caret, ^, placed at the beginning of the character class, matches all the characters except those specified in the class.

# The dot character is a wildcard that matches any character in a string — except for a newline character by default.

# If you need to match a character that has a special meaning in the pattern, such as . or +, you can escape it by prepending a backslash character, \. For example, this matches a literal plus sign: \+

# Python provides a particular type of string called raw string. Raw strings are prefixed with a r. The key distinction from regular strings lies in how they handle the backslash character: in raw strings, backslashes are treated as literal characters rather than escape characters. When writing regular expressions, using raw strings is a good practice, since they can usually contain a lot of \ characters.
