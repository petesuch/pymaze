#!/usr/bin/python2.7 -u
import sys

# n1.pl the cutting edge version of 
 -= 1;
# inspired by a physics project 
# this version works fine

##################################################################
##################################################################
##################################################################
# TODO:
# * try to 'use strict' 
# * too many variables!
# * random maze generation
# * use array from file?  
# * perl doesnt like to create arrays on the fly coz you have to
# ...
# * show exactly  all points and list them
# * don't like the fact that $blah[-1] is the same as the
# last element ... that sucks.  though perhaps I could test
# for it and/or make it a function of arraylength...
# * compartmentalize more with functions
 += 1;
# java, python, and ...
##################################################################
##################################################################
##################################################################

#### START main program


#use strict; 

#no strict 'refs';


#my @maze;

#my @cp;


#@maze = (

#[ "A", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "B" ], 

#[ "0", "x", "x", "x", "x", "x", "x", "x", "x", "0", "0", "0", "0", "0", "x", "0", "0", "0", "x", "0" ],

#[ "0", "x", "0", "x", "x", "0", "x", "0", "x", "0", "0", "0", "x", "x", "x", "0", "0", "0", "x", "0" ], 

#[ "0", "x", "0", "0", "x", "0", "x", "0", "x", "x", "0", "0", "x", "0", "0", "0", "0", "0", "x", "0" ],

#[ "0", "x", "0", "0", "x", "0", "x", "x", "0", "x", "0", "0", "x", "x", "x", "x", "x", "0", "x", "0" ],

#[ "0", "x", "0", "0", "x", "0", "x", "0", "x", "x", "x", "0", "0", "0", "x", "0", "0", "0", "x", "0" ], 

#[ "0", "x", "0", "x", "0", "x", "x", "x", "x", "0", "x", "0", "0", "0", "x", "0", "0", "0", "x", "0" ],

#[ "0", "x", "x", "0", "x", "0", "x", "0", "x", "0", "x", "x", "x", "x", "0", "0", "x", "x", "x", "0" ],

#[ "0", "0", "x", "0", "0", "0", "0", "0", "x", "0", "0", "0", "0", "0", "x", "x", "x", "0", "x", "0" ],

#[ "0", "0", "x", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "x", "0", "x", "0" ],

#[ "0", "x", "0", "0", "x", "x", "x", "x", "x", "0", "x", "x", "x", "0", "x", "x", "x", "0", "x", "0" ],

#[ "0", "x", "x", "x", "0", "x", "x", "x", "x", "0", "x", "0", "0", "0", "x", "0", "x", "0", "x", "0" ],

#[ "0", "x", "x", "x", "x", "0", "x", "x", "x", "0", "x", "0", "x", "0", "x", "0", "x", "0", "x", "0" ],

#[ "0", "x", "x", "x", "x", "x", "0", "x", "x", "0", "x", "x", "x", "0", "x", "0", "0", "0", "x", "0" ],

#[ "0", "x", "x", "x", "x", "x", "x", "x", "x", "0", "x", "0", "x", "0", "x", "0", "0", "0", "x", "0" ],

#[ "0", "x", "x", "x", "x", "x", "x", "0", "x", "0", "x", "0", "x", "0", "x", "0", "0", "0", "x", "0" ],

#[ "0", "x", "x", "x", "x", "x", "x", "0", "x", "x", "x", "0", "x", "0", "x", "0", "0", "0", "x", "0" ],

#[ "0", "x", "x", "x", "x", "x", "x", "x", "x", "0", "0", "0", "x", "0", "x", "0", "0", "0", "x", "0" ],

#[ "0", "x", "x", "x", "x", "x", "x", "x", "x", "0", "0", "0", "x", "0", "x", "x", "x", "x", "x", "0" ],

#[ "C", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "x", "0", "0", "0", "Z" ]

#);



#@cp = @maze;


#my $x; my $y; my $xnew; my $ynew;

#my $xs ;

#my $ys ;

#my $xp ;

#my $yp ;

#my $xprev= ""; my $yprev="";

#my $xstart;

#my $ystart;

#my $xright; my $xleft; my $yup; my $ydown;

#my $temp; my $xtemp; my $ytemp;

#my $DONE;

#my $solved;

#my $tm;

#my $germ; my @branch;

#my $j; my $i;


if cp[0][j] == "x" :
#		last if ( $solved eq "YES" );


    print "********************************************"
    print "********************************************"
    print "********************************************"
    print "      *** Entering Maze at: (j,0) ***"
    print "********************************************"
    print "********************************************"
    print "********************************************"

    xs = xstart = j
    ys = ystart = 0
    DONE = "NO"

    while "DONE" ne "YES" :
        print "\n#######################################################"
        print *** Begin while-loop with: \$DONE = DONE\n
        germ = ""
        solved = "NO"
        x = xs
        y = ys
        xprev = xp
        yprev = yp

        cp[$yprev][$xprev] = "+"

#			my $xright	=		$x+1;	

#			my $xleft	=		$x-1;

#			my $yup		=		$y+1;

#			my $ydown	=		$y-1;

#			my $counter =		0;


        print \$xprev = $xprev\n\$yprev = yprev
        print "\n### In while-loop with:(x,y) ###"

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
        if cp[yup][x] == "x" & yup eq "19" :
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
#				my $temp = pop @$germ; 

#				my ($xnew, $ynew) = split(/\,/, $temp);

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
#				until ( "@$tm" ne "" | "$#branch" eq "-1" ) {

            tm = pop @branch
					#print "\@$tm = @$tm\n";
					#print "DURING:\t$tm contains: (@$tm)\n";
					#print "DURING: the branch has: @branch\n";
				# if last element not empty push back on the branch
        if "@tm" ne "" :
            print "BEFORE: @branch"
            print "pushing back on the branch:"
            print "because", tm contains: (@$tm)
#					push @branch, $tm;

            print "AFTER: @branch"
			#### pop the bud
        temp = pop @tm
#				($xtemp, $ytemp) = split( /,/, $temp);	


        if xtemp ne "" & ytemp ne "" :
            xs = xtemp; ys = ytemp

        elif xtemp == "" & ytemp eq "" :
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
    print "***************************************************"
    print "***************************************************"
    print "**********    HOORAY I SOLVED THE PUZZLE    *******"
    print "***************************************************"
    print "***************************************************"

elif solved == "NO" :
    print "***************************************************"
    print "***************************************************"
    print "*****    BUMMER: COULD NOT FIND A WAY OUT   *******"
    print "***************************************************"
    print "***************************************************"

sys.stdout.write(array())

#### END main program

##########################################################
##########################################################


####    SUBROUTINES

#sub addbud()

germ = "G_[0]_[1]"
if @germ:
#		 push @$germ, "$_[2],$_[3]";

else:
#		@$germ= ( "$_[2],$_[3]" );

}

#sub addbranch()

	#$branch = "B[$xstart]"; # ie B3	
if @branch :
#		 push @branch, "$_[0]";

else:
#		@branch = ( "$_[0]" ); 

#	print "Branch Array Created $branch with these points:\n(@$branch)\n";
}

#sub printarray()

sys.stdout.write(str("cp[i][j]    "))
}
print ""
}
}
