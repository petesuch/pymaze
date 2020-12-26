#!/usr/bin/python3

###############################################################################
# n1.py     An attempt at converting n1.pl to python
# A rudimentary Solve-a-Maze program where an array is given and the program
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
[ "O", "O", "O", "X", "O", "X", "X", "X", "X", "X", "O", "X", "X", "X", "X", "X", "X", "X", "X", "O" ], 

[ "O", "X", "X", "X", "X", "X", "X", "X", "X", "O", "O", "O", "O", "O", "X", "O", "O", "O", "X", "O" ],

[ "O", "X", "O", "X", "X", "O", "X", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "X", "O" ], 

[ "O", "X", "O", "O", "X", "O", "X", "O", "X", "X", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O" ],

[ "O", "X", "O", "O", "X", "O", "X", "X", "O", "X", "O", "O", "X", "X", "X", "X", "X", "O", "X", "O" ],

[ "O", "X", "O", "O", "X", "O", "X", "O", "X", "X", "X", "O", "O", "O", "X", "O", "O", "O", "X", "O" ], 

[ "O", "X", "O", "X", "O", "X", "X", "X", "X", "O", "X", "O", "O", "O", "X", "O", "O", "O", "X", "O" ],

[ "O", "X", "X", "O", "X", "O", "X", "O", "X", "O", "X", "X", "X", "X", "O", "O", "X", "X", "X", "O" ],

[ "O", "O", "X", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "X", "X", "O", "X", "O" ],

[ "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "X", "O" ],

[ "O", "X", "O", "O", "X", "X", "X", "X", "X", "O", "X", "X", "X", "O", "X", "X", "X", "O", "X", "O" ],

[ "O", "X", "X", "X", "O", "X", "X", "X", "X", "O", "X", "O", "O", "O", "X", "O", "X", "O", "X", "O" ],

[ "O", "X", "X", "X", "X", "O", "X", "X", "X", "O", "X", "O", "X", "O", "X", "O", "X", "O", "X", "O" ],

[ "O", "X", "X", "X", "X", "X", "O", "X", "X", "O", "X", "X", "X", "O", "X", "O", "O", "O", "X", "O" ],

[ "O", "X", "X", "X", "X", "X", "X", "X", "X", "O", "X", "O", "X", "O", "X", "O", "O", "O", "X", "O" ],

[ "O", "X", "X", "X", "X", "X", "X", "O", "X", "O", "X", "O", "X", "O", "X", "O", "O", "O", "X", "O" ],

[ "O", "X", "X", "X", "X", "X", "X", "O", "X", "X", "X", "O", "X", "O", "X", "O", "O", "O", "X", "O" ],

[ "O", "X", "X", "X", "X", "X", "X", "X", "X", "O", "O", "O", "X", "O", "X", "O", "O", "O", "X", "O" ],

[ "O", "X", "X", "X", "X", "X", "X", "X", "X", "O", "O", "O", "X", "O", "X", "X", "X", "X", "X", "O" ],

[ "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O" ]
)
xp=0
yp=0
cp = copy.deepcopy(maze)
solved = "NO"
for j in range(20):
	if cp[0][j] == "X":
		if solved == "YES":
			break
		print ("*******************************************************************************")
		print ('Entering Maze at:   (',j,', 0',')')
		print ("*******************************************************************************")
		xs = xstart = j
		ys = ystart = 0

		DONE = "NO"
		while DONE != "YES":
			print ("##############################################")
			print ("Begin while-loop with: DONE =",DONE)
			germ = ""
			solved = "NO"
			x = xs
			y = ys
			xprev =	xp
			yprev =	yp

			cp[yprev][xprev] = "+"

			xright=x+1	
			xleft=x-1
			yup=y+1
			ydown=y-1
			counter=0

			print ("xprev = ", xprev , "yprev = ", yprev)
			print ("--->In while-loop with: ",  x , y  )


			# check below
			if cp[ydown][x] == "X":
				#addbud($x,$y,$x,$ydown)
				counter+=1
				print("hello from check below")

			# check to the right
			if cp[y][xright] == "X" :
				#addbud($x,$y,$xright,$y);
				counter+=1
				print("hello from check below")

			# check to the left
			if cp[y][xleft] == "X":
				#addbud($x,$y,$xleft,$y);
				counter+=1
				print("hello from check left")

			# check above
			if cp[yup][x] == "X":
				#addbud($x,$y,$x,$yup);
				counter+=1
				print("hello from check above")


###############################################################################

""" my $x; my $y; my $xnew; my $ynew;
my $xs ;
my $ys ;
my $xp ;
my $yp ;
my $xprev= ""; my $yprev="";
my $xstart;
my $ystart;
my $xright; my $xleft; my $yup; my $ydown;
my $temp; my $xtemp; my $ytemp;
my $DONE;
my $solved;
my $tm;
my $germ; my @branch;
my $j; my $i;
for $j ( 0 .. 19 ) {
	if ( $cp[0][$j] eq "x" ) {
		last if ( $solved eq "YES" );
		print "********************************************\n";
		print "********************************************\n";
		print "********************************************\n";
		print "      *** Entering Maze at: ($j,0) ***\n";
		print "********************************************\n";
		print "********************************************\n";
		print "********************************************\n";
		$xs = $xstart = $j;
        $ys = $ystart = 0;
		$DONE = "NO";

		while ( "$DONE" ne "YES" ) {
			print "\n#######################################################\n";
			print "      *** Begin while-loop with: \$DONE = $DONE\n\n";
			$germ = "";
			$solved = "NO";
			$x =		$xs;
			$y =		$ys;
			$xprev =	$xp;
			$yprev =	$yp;

			$cp[$yprev][$xprev] = "+";

			my $xright	=		$x+1;	
			my $xleft	=		$x-1;
			my $yup		=		$y+1;
			my $ydown	=		$y-1;
			my $counter =		0;

			print "\$xprev = $xprev\n\$yprev = $yprev\n";
			print "\n### In while-loop with:($x,$y) ###\n";


			# check below
			if ( $cp[$ydown][$x] eq "X" ) {
				addbud($x,$y,$x,$ydown);
				$counter++;
			}

			# check to the right
			if ( $cp[$y][$xright] eq "X" ) {
				addbud($x,$y,$xright,$y);
				$counter++;
			}

			# check to the left
			if ( $cp[$y][$xleft] eq "X" ) {
				addbud($x,$y,$xleft,$y);
				$counter++;
			}

			# check above
			if ( $cp[$yup][$x] eq "X" ) {
				addbud($x,$y,$x,$yup);
				$counter++;
			}
"""
###############################################################################
"""
			# there yet?
			if ( $cp[$yup][$x] eq "X" && $yup eq "19" ) {
				$solved = "YES";
				print "************* FINISH ***************\n";
				print "************* FINISH ***************\n";
				$DONE = "YES";
				#print "# there yet? \$DONE is $DONE\n";
				$cp[$y][$x] = "+"; # if its there mark it
				$cp[$yup][$x] = "+"; # if its there mark it
    		}


			print "Branch Array \@branch contains these points:\n(@branch)\n";
			#print "Branch Array Created B$xstart with these points:\n($B[$xstart])\n";



#########	# not dead 
			if ( $counter gt 0 ) {
				addbranch($germ);
				print "Array $germ contains the following points:\n(@$germ)\n";
				my $temp = pop @$germ; 
				my ($xnew, $ynew) = split(/\,/, $temp);
				print "$xnew,$ynew\n";
				print "The value of $germ:(@$germ)\n";

				$xp = $x;
				$yp = $y;

				$xs = $xnew;
				$ys = $ynew;
		

			}

			##### dead end


			if ( $counter eq 0 ) {
				print "\nDEAD END: $x,$y \n";
				$tm = pop @branch; # pop the branch 
				print "\t \@$tm = (@$tm)\n";
				until ( "@$tm" ne "" || "$#branch" eq "-1" ) {
					$tm = pop @branch;
					#print "\@$tm = @$tm\n";
					#print "DURING:\t$tm contains: (@$tm)\n";
					#print "DURING: the branch has: @branch\n";
				} 
				# if last element not empty push back on the branch
				if ( "@$tm" ne "" ) {
					print "BEFORE: @branch\n";
					print "pushing back on the branch:\n";
					print " because $tm contains: (@$tm)\n";
					push @branch, $tm;
					print "AFTER: @branch\n";
				}
			#### pop the bud
				$temp = pop @$tm;
				($xtemp, $ytemp) = split( /,/, $temp);	

				if ( $xtemp ne "" && $ytemp ne "" ) {
					$xs = $xtemp; $ys = $ytemp;	
				}

				elsif ( $xtemp eq "" && $ytemp eq "" ) {
					print "\t\$xtemp and \$ytemp are NULL\n";
					print "\t###  branch: @branch\n";
					$DONE = "YES";	
				}
				print "\tPITSTOP: \$xs:($xs),\$ys:($ys)\n";
			}	# end of dead end
	
			print "\n#### END of while-loop:\$DONE is $DONE\n";
			print "\n\t\$xs:($xs),\$ys:($ys),\$xp:($xp),\$yp:($yp)\n";
			print "\t###  branch: @branch\n";
			print "#### END of while-loop:\$DONE is $DONE\n";
			print "#######################################################\n";
				$cp[$y][$x] = "+"; # if its there mark it

		printarray(); sleep 2;
		} # # # # end of while-loop
	} #end of if
} # end of for



if ( $solved eq "YES" ) {
	print "***************************************************\n";
	print "***************************************************\n";
	print "**********    HOORAY I SOLVED THE PUZZLE    *******\n";
	print "***************************************************\n";
	print "***************************************************\n";
}

elsif ( $solved eq "NO" ) {
	print "***************************************************\n";
	print "***************************************************\n";
	print "*****    BUMMER: COULD NOT FIND A WAY OUT   *******\n";
	print "***************************************************\n";
	print "***************************************************\n";
}	

printarray();

#### END main program

##########################################################
##########################################################


####    SUBROUTINES

sub addbud()
{
	$germ= "G$_[0]$_[1]";
	if ( @$germ) {
		 push @$germ, "$_[2],$_[3]";
	}
	else {
		@$germ= ( "$_[2],$_[3]" );
	}
}	

sub addbranch()
{
	#$branch = "B[$xstart]"; # ie B3	
	if ( @branch ) {		# if one already exists 
		 push @branch, "$_[0]";
	}
	else {
		@branch = ( "$_[0]" ); 
	}
#	print "Branch Array Created $branch with these points:\n(@$branch)\n";
}

sub printarray()
{
    for  $i ( 0 .. 19 ) {
        for $j (  0 .. 19 ) {
                print "$cp[$i][$j]    ";
        }
        print "\n";
    }
}
 """