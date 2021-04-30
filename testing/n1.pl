#! /usr/bin/perl -w

#    n1.pl
#
#   @author:  Peter A. Suchsland
#   A maze solving program
#   Inspired by a physics project this version works

# TODO:
#
# * reduce number of variables!
# * random maze generation or use array from file
#

#### START main program

no warnings;
use Time::HiRes;

my $SZ = 40;
my @maze;
my @cp;

#####################################################################################################################################################################

@maze = (
["A","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","B"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","x","o","x","x","x","x","x","x","x","x","x","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","x","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","x","o","o","o","o","x","x","x","x","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","x","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","x","x","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","x","x","x","x","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o"],
["o","o","o","o","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o"],
["x","x","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","x","x","o","o","o","o","o","o"],
["x","o","o","o","o","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","x","x","o","o","o","o","o","o","o"],
["x","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","x","x","x","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o"],
["x","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o"],
["x","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","x","o","x","o","o","o","x","x","x","o","o","x","o","o","o","o","o","o","o","o"],
["x","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","x","x","o","x","x","x","x","x","x","x","o","x","x","x","x","x","o","o","o","o","o","o","o"],
["x","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","x","x","x","x","o","o","o","o","x","o","o","x","o","o","o","x","o","o","o","o","o","o","o"],
["x","o","o","o","o","x","o","x","o","x","x","x","x","o","o","o","o","x","o","o","x","o","o","o","o","x","o","o","x","o","o","o","x","o","o","o","o","o","o","o"],
["x","o","o","x","x","x","o","x","o","x","o","o","x","o","o","o","o","x","o","o","x","x","o","o","o","x","o","o","x","o","o","o","x","o","o","o","o","o","o","o"],
["x","o","o","x","o","x","o","x","o","x","o","o","x","o","o","o","o","x","o","o","o","x","o","o","o","x","o","o","x","x","x","x","x","o","o","o","o","o","o","o"],
["x","o","o","x","o","x","o","x","x","x","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o"],
["x","o","o","x","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","x","o","o","o","o","o","o","x","x","x","x","x","x","x","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","o","o","x","x","x","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","x","x","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","x","x","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","x","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","o","o","o","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","o","o","o","o","o","o","o","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","x","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","Z"]
);

#####################################################################################################################################################################


@cp = @maze;

my $go= "x";
my $x;
my $y;
my $xnew;
my $ynew;
my $xs ;
my $ys ;
my $xp ;
my $yp ;
my $xprev= "";
my $yprev="";
my $xstart;
my $ystart;
my $xright;
my $xleft;
my $yup;
my $ydown;
my $temp;
my $xtemp;
my $ytemp;
my $DONE;
my $solved;
my $tm;
my $germ;
my @branch;
my $j;
my $i;


print "********************************************\n";
for $j ( 0 .. $SZ ) {
    if ( $cp[0][$j] eq $go ) {
        last if ( $solved eq "YES" );

        print "********************************************\n";
        print "      *** Entering Maze at: ($j,0) ***\n";
        print "********************************************\n";

        $xs = $xstart = $j;
        $ys = $ystart = 0;
        $DONE = "NO";

        while ( "$DONE" ne "YES" ) {
            print "###############################################\n";
            print "      *** Begin while-loop with: \$DONE = $DONE\n";
            $germ = "";
            $solved =   "NO";
            $x =        $xs;
            $y =        $ys;
            $xprev =    $xp;
            $yprev =    $yp;

            $cp[$yprev][$xprev] = "+";
            print "marking: \$cp[\$yprev][\$xprev]\n";

            my $xright =   $x+1;
            my $xleft =    $x-1;
            my $yup =      $y+1;
            my $ydown =    $y-1;
            my $counter =    0;

            print "\$xprev = $xprev\n\$yprev = $yprev\n";
            print "### In while-loop with:($x,$y) ###\n";
            # check below
            if ( $cp[$ydown][$x] eq $go ) {
                addbud($x,$y,$x,$ydown);
                $counter++;
            }
            # check to the right
            if ( $cp[$y][$xright] eq $go ) {
                addbud($x,$y,$xright,$y);
                $counter++;
            }
            # check to the left
            if ( $cp[$y][$xleft] eq $go ) {
                addbud($x,$y,$xleft,$y);
                $counter++;
            }
            # check above
            if ( $cp[$yup][$x] eq $go ) {
                addbud($x,$y,$x,$yup);
                $counter++;
            }


#########    # there yet?
            if ( $cp[$yup][$x] eq $go && $yup eq $SZ ) {
                $solved = "YES";
                print "************* FINISH ***************\n";
                print "************* FINISH ***************\n";
                $DONE = "YES";
                print "# there yet? \$DONE is $DONE\n";
                $cp[$y][$x] = "+"; # if its there mark it
                $cp[$yup][$x] = "+"; # if its there mark it
            }

            print "Branch Array \@branch contains these points:\n(@branch)\n";
            print "Branch Array Created B$xstart with these points:\n($B[$xstart])\n";

            ##### not dead
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
                print "\@$tm = (@$tm)\n";
                until ( "@$tm" ne "" || "$#branch" eq "-1" ) {
                    $tm = pop @branch;
                    print "\@$tm = @$tm\n";
                    print "DURING:\t$tm contains: (@$tm)\n";
                    print "DURING: the branch has: @branch\n";
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
                    print "\$xtemp and \$ytemp are NULL\n";
                    print "#  branch: @branch\n";
                    $DONE = "YES";
                }
                print "\tPITSTOP: \$xs:($xs),\$ys:($ys)\n";
            }    # end of dead end

            print "# END of while-loop:\$DONE is $DONE\n";
            print "\$xs:($xs),\$ys:($ys),\$xp:($xp),\$yp:($yp)\n";
            print "# branch: @branch\n";
            print "# END of while-loop:\$DONE is $DONE\n";
            print "###########################################\n";
                $cp[$y][$x] = "+"; # if its there mark it

        printarray();
        #Time::HiRes::sleep(0.5); #.5 seconds
        #Time::HiRes::usleep(1); # 1 microsecond.
        #sleep 1;
        } # end of while-loop
    } # end of if
} # end of for

if ( $solved eq "YES" ) {
    print "***************************************************\n";
    print "********** MAZE SOLVED ****************************\n";
    print "***************************************************\n";
}

elsif ( $solved eq "NO" ) {
    print "***************************************************\n";
    print "*****  MAZE NOT SOLVED ****************************\n";
    print "***************************************************\n";
}

printarray();
#### END main program
#
##########################################################
#
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
    if ( @branch ) { # if one already exists
         push @branch, "$_[0]";
    }
    else {
        @branch = ( "$_[0]" );
    }
    print "Branch Array Created $branch with these points:\n(@$branch)\n";
}
sub printarray()
{
    for $i ( 0 .. $SZ ) {
        for $j (  0 .. $SZ ) {
            print "$cp[$i][$j] "; # number of spaces here between go chars
        }
        print "\n";
    }
}
