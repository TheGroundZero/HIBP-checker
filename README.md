# Have I Been Pwned Checker

Check whether a password (hash) is present in the [Have I Been Pwned][hibp] database.

This uses HIBP's k-anonymity scheme to protect the anonymity of the passwords over the wire.  
More info on this k-anonymity scheme can be found in [Troy Hunt's blog post][kanon]


## Usage

Help info

    $ python hibp_checker.py -h

    usage: HIBP checker [-h] -f FILEPATH [-s] [-i]
    
    Check if a password (hash) is present in the HIBP database
    
    optional arguments:
      -h, --help            show this help message and exit
      -f FILEPATH, --file FILEPATH
                            File path to password list
      -s, --sha1            Provided password are already (SHA1) hashed? (default:
                            False)
      -i, --inplace         Modify [FILE] to append results to each line?
                            (default: False)


Provide password list with passwords in plain-text

    $ python hibp_checker.py -f passwords.lst
    
     + Found no matching entry on HIBP for 'P@ssw0rd'. It has occurred 51259 times.
     + Found no matching entry on HIBP for 'password'. It has occurred 3645804 times.
     + Found no matching entry on HIBP for 'abcdef'. It has occurred 178998 times.
     + Found no matching entry on HIBP for '123456789'. It has occurred 7671364 times.
     + Found no matching entry on HIBP for 'monkey'. It has occurred 980209 times.
     + Found no matching entry on HIBP for 'hunter2'. It has occurred 17043 times.
     - Found matching entry on HIBP for 'Tr0ub4dor&3'. It has occurred 0 times.
     + Found no matching entry on HIBP for 'correcthorsebatterystaple'. It has occurred 114 times.


Provide password list with passwords hashed using SHA1

    $ python hibp_checker.py -f passwords-hashes.lst -s
    
     + Found no matching entry on HIBP for '21BD12DC183F740EE76F27B78EB39C8AD972A757'. It has occurred 51259 times.
     + Found no matching entry on HIBP for '5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8'. It has occurred 3645804 times.
     + Found no matching entry on HIBP for '1F8AC10F23C5B5BC1167BDA84B833E5C057A77D2'. It has occurred 178998 times.
     + Found no matching entry on HIBP for 'F7C3BC1D808E04732ADF679965CCC34CA7AE3441'. It has occurred 7671364 times.
     + Found no matching entry on HIBP for 'AB87D24BDC7452E55738DEB5F868E1F16DEA5ACE'. It has occurred 980209 times.
     + Found no matching entry on HIBP for 'F3BBBD66A63D4BF1747940578EC3D0103530E21D'. It has occurred 17043 times.
     - Found matching entry on HIBP for '874572E7A5AE6A49466A6AC578B98ADBA78C6AA6'. It has occurred 0 times.
     + Found no matching entry on HIBP for 'BFD3617727EAB0E800E62A776C76381DEFBC4145'. It has occurred 114 times.


Update password file with results

    $ pythonhibp_checker.py -f examples/passwords-inplace.lst -i
    $ cat examples/passwords-inplace.lst
    
    +:P@ssw0rd:51259
    +:password:3645804
    +:abcdef:178998
    +:123456789:7671364
    +:monkey:980209
    +:hunter2:17043
    -:Tr0ub4dor&3:0
    +:correcthorsebatterystaple:114



[hibp]: https://haveibeenpwned.com/
[kanon]: https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/#cloudflareprivacyandkanonymity
