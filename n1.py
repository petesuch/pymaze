#!/usr/bin/python2.7 -u
# n1.py     An attempt at converting n1.pl to python
# A rudimentary solve a Maze program where an array is given and the program
# attempts to solve whether there is a way to get from top to bottom.
# Author: Peter Suchsland
###############################################################################
# TODO:
# Learn how to creates variables and arrays in python
# Learn proper syntax for while, if loops
# Proper indentation
###############################################################################

#### START main program
import sys
import copy

maze = (

[ "A", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "B" ], 

[ "0", "x", "x", "x", "x", "x", "x", "x", "x", "0", "0", "0", "0", "0", "x", "0", "0", "0", "x", "0" ],

[ "0", "x", "0", "x", "x", "0", "x", "0", "x", "0", "0", "0", "x", "x", "x", "0", "0", "0", "x", "0" ], 

[ "0", "x", "0", "0", "x", "0", "x", "0", "x", "x", "0", "0", "x", "0", "0", "0", "0", "0", "x", "0" ],

[ "0", "x", "0", "0", "x", "0", "x", "x", "0", "x", "0", "0", "x", "x", "x", "x", "x", "0", "x", "0" ],

[ "0", "x", "0", "0", "x", "0", "x", "0", "x", "x", "x", "0", "0", "0", "x", "0", "0", "0", "x", "0" ], 

[ "0", "x", "0", "x", "0", "x", "x", "x", "x", "0", "x", "0", "0", "0", "x", "0", "0", "0", "x", "0" ],

[ "0", "x", "x", "0", "x", "0", "x", "0", "x", "0", "x", "x", "x", "x", "0", "0", "x", "x", "x", "0" ],

[ "0", "0", "x", "0", "0", "0", "0", "0", "x", "0", "0", "0", "0", "0", "x", "x", "x", "0", "x", "0" ],

[ "0", "0", "x", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "x", "0", "x", "0" ],

[ "0", "x", "0", "0", "x", "x", "x", "x", "x", "0", "x", "x", "x", "0", "x", "x", "x", "0", "x", "0" ],

[ "0", "x", "x", "x", "0", "x", "x", "x", "x", "0", "x", "0", "0", "0", "x", "0", "x", "0", "x", "0" ],

[ "0", "x", "x", "x", "x", "0", "x", "x", "x", "0", "x", "0", "x", "0", "x", "0", "x", "0", "x", "0" ],

[ "0", "x", "x", "x", "x", "x", "0", "x", "x", "0", "x", "x", "x", "0", "x", "0", "0", "0", "x", "0" ],

[ "0", "x", "x", "x", "x", "x", "x", "x", "x", "0", "x", "0", "x", "0", "x", "0", "0", "0", "x", "0" ],

[ "0", "x", "x", "x", "x", "x", "x", "0", "x", "0", "x", "0", "x", "0", "x", "0", "0", "0", "x", "0" ],

[ "0", "x", "x", "x", "x", "x", "x", "0", "x", "x", "x", "0", "x", "0", "x", "0", "0", "0", "x", "0" ],

[ "0", "x", "x", "x", "x", "x", "x", "x", "x", "0", "0", "0", "x", "0", "x", "0", "0", "0", "x", "0" ],

[ "0", "x", "x", "x", "x", "x", "x", "x", "x", "0", "0", "0", "x", "0", "x", "x", "x", "x", "x", "0" ],

[ "C", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "x", "0", "0", "0", "Z" ]

)

################################################################################
# These are all the Perl variables that will need to be changed....
#
# @maze;
# @cp;
# $x;  $y;  $xnew;  $ynew;
# $xs ;
# $ys ;
# $xp ;
# $yp ;
# $xprev= "";  $yprev="";
# $xstart;
# $ystart;
# $xright;  $xleft;  $yup;  $ydown;
# $temp;  $xtemp;  $ytemp;
# $DONE;
# $solved;
# $tm;
# $germ;  @branch;
# $j;  $i;

cp = copy.deepcopy(maze)
if cp[0][j] == "x" :
#last if ( $solved == "YES" );

print "*******************************************************************************"
print "*******************************************************************************"
print " Entering Maze at: (j,0) ***"
print "*******************************************************************************"
print "*******************************************************************************"

    xs = xstart = j
    ys = ystart = 0
    DONE = "NO"

    while "DONE" != "YES" :
        print "*******************************************************************************"
        print (*** Begin while-loop with: \$DONE = DONE\n)
        germ = ""
        solved = "NO"
        x = xs
        y = ys
        xprev = xp
        yprev = yp

        cp[$yprev][$xprev] = "+"

#			 $xright	=		$x+1;	

#			 $xleft	=		$x-1;

#			 $yup		=		$y+1;

#			 $ydown	=		$y-1;

#			 $counter =		0;


        print (\$xprev = $xprev\n\$yprev = yprev)
        print ("\n### In while-loop with:(x,y) ###a")

			# check below
        if cp[ydown][x] == "x" :
#				addbud($x,$y,$x,$ydown);

            counter += 1;

			# check to the right
        if cp[y][xright] == "x" :
#				addbud($x,$y,$xright,$y);

            counter += 1;

			# check to the left
        if cp[y][xleft] == "x" :
#				addbud($x,$y,$xleft,$y);

            counter += 1;

			# check above
        if cp[yup][x] == "x" :
#				addbud($x,$y,$x,$yup);

            counter += 1;


#########	# there yet?
        if cp[yup][x] == "x" & yup == "19" :
            solved = "YES"
            print "************* FINISH ***************"
            print "************* FINISH ***************"
            DONE = "YES"
				#print "# there yet? \$DONE is $DONE\n";
            cp[$y][$x] = "+"
            cp[$yup][$x] = "+"


        print "Branch Array \@branch contains these points:\n(@branch)"
			#print "Branch Array Created B$xstart with these points:\n($B[$xstart])\n";



#########	# not dead 
        if counter gt 0 :
#				addbranch($germ);

            print "Array", germ contains the following points:\n(@$germ)
#				 $temp = pop @$germ; 

#				 ($xnew, $ynew) = split(/\,/, $temp);

            print xnew,ynew
            print "The value of", germ:(@$germ)

            xp = x
            yp = y

            xs = xnew
            ys = ynew
		


			##### dead end


        if counter == 0 :
            print "\nDEAD END:", x,$y 
            tm = pop @branch
            print "\t \@tm = (@tm)"
#				until ( "@$tm" != "" | "$#branch" == "-1" ) {

            tm = pop @branch
					#print "\@$tm = @$tm\n";
					#print "DURING:\t$tm contains: (@$tm)\n";
					#print "DURING: the branch has: @branch\n";
				# if last element not empty push back on the branch
        if "@tm" != "" :
            print "BEFORE: @branch"
            print "pushing back on the branch:"
            print "because", tm contains: (@$tm)
#					push @branch, $tm;

            print "AFTER: @branch"
			#### pop the bud
        temp = pop @tm
#				($xtemp, $ytemp) = split( /,/, $temp);	


        if xtemp != "" & ytemp != "" :
            xs = xtemp; ys = ytemp

        elif xtemp == "" & ytemp == "" :
            print "\t\xtemp and \ytemp are NULL"
            print "\t###  branch: @branch"
            DONE = "YES"
        print "\tPITSTOP: \xs:(xs),\ys:(ys)"
	
    print \n#### END of while-loop:\$DONE is DONE
    print "\n\t\xs:(xs),\ys:(ys),\xp:(xp),\yp:(yp)"
    print "\t###  branch: @branch"
    print #### END of while-loop:\$DONE is DONE
    print "#######################################################"
    cp[$y][$x] = "+"

#		printarray(); sleep 2;

}
}



if solved == "YES" :
    print ("***************************************************")
    print ("***************************************************")
    print ("***************************************************")
    print ("**********    HOORAY I SOLVED THE PUZZLE    *******")
    print ("***************************************************")
    print ("***************************************************")
    print ("***************************************************")

elif solved == "NO" :
    print ("***************************************************")
    print ("***************************************************")
    print ("***************************************************")
    print ("*****    BUMMER: COULD NOT FIND A WAY OUT   *******")
    print ("***************************************************")
    print ("***************************************************")
    print ("***************************************************")

sys.stdout.write(array())

###############################################################################
#### END main program #########################################################
###############################################################################





###############################################################################
### SUBROUTINES ###############################################################
###############################################################################

def addbud():

    germ = "G_[0]_[1]"
    if @germ:
#       push @$germ, "$_[2],$_[3]";

    else:
#	@$germ= ( "$_[2],$_[3]" );



def addbranch():

    #$branch = "B[$xstart]"; # ie B3	
if @branch :
#   push @branch, "$_[0]";

else:
#   @branch = ( "$_[0]" ); 

#   print "Branch Array Created $branch with these points:\n(@$branch)\n";


def printarray():

    sys.stdout.write(str("cp[i][j]    "))
    print ""


