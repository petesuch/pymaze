#! /usr/bin/perl

#  Perl version
#
#  mazesolver.pl -- a maze program -- Peter A. Suchsland
#  Inspired by a physics project; this version works

##################################################################
#    TODO:
#   reduce number of variables!
#   random maze generation
#   make larger array
#   C, C++,Java, Python, JavaScript
##################################################################

# ten by ten array
@ar0 = ( "x", "0", "0", "0", "0", "0", "x", "0", "0", "0" );
@ar1 = ( "0", "0", "x", "0", "x", "x", "x", "x", "0", "0" );
@ar2 = ( "0", "x", "x", "x", "x", "0", "x", "0", "x", "0" );
@ar3 = ( "0", "x", "0", "x", "0", "0", "x", "0", "x", "0" );
@ar4 = ( "0", "x", "0", "x", "0", "x", "x", "x", "0", "0" );
@ar5 = ( "0", "x", "0", "x", "0", "x", "x", "0", "0", "0" );
@ar6 = ( "0", "x", "0", "x", "0", "x", "x", "x", "x", "0" );
@ar7 = ( "0", "x", "x", "0", "x", "0", "x", "0", "x", "0" );
@ar8 = ( "0", "0", "x", "0", "0", "0", "0", "0", "x", "0" );
@ar9 = ( "0", "0", "x", "0", "0", "0", "0", "0", "0", "0" );


# start of main

copyarray();

my $xs = "";
my $ys = "";
my $xp = "";
my $yp = "";

for $j ( 0 .. 9 ) {
    if ( $cp0[$j] eq "x" ) {
        print "********************************************\n";
        print "      *** Entering Maze at: ($j,0) ***\n";
        print "********************************************\n";

        $xs = $xstart = $j;
        $ys = $ystart = 0;
        $DONE = "NO";

        while ( "$DONE" ne "YES" ) {
        print "\n\n *** Begin while-loop with: \$DONE = $DONE\n\n";

            $solved = "NO";
            my $x =     $xs;
            my $y =     $ys;
            my $xprev =     $xp;
            my $yprev =     $yp;

            my $altcp =     "cp$yprev";
            $$altcp[$xprev] = "P";

            #if ( $x+1 gt 0 && $x+1 lt 10 ) { my $xright=$x+1;}
            my $xright = $x+1;

            my $xleft = $x-1;
            my $yup = $y+1;
            my $ydown = $y-1;
            my $samerow = "cp$y";
            my $uprow = "cp$yup";
            my $downrow = "cp$ydown";
            my $counter = 0;

            print "\$xprev = $xprev\n\$yprev = $yprev\n";
            print "\n### In while-loop with:($x,$y) ###\n";
            print "\$altcp: $altcp: @$altcp\n";

            # check below
            if ( $$downrow[$x] eq "x" ) {
                addbud($x,$y,$x,$ydown);
                $counter++;
                print "below:\$counter is $counter\n";
            }

            # check to the right
            if ( $$samerow[$xright] eq "x" ) {
                addbud($x,$y,$xright,$y);
                $counter++;
                print "right:\$counter is $counter\n";
            }

            # check to the left
            if ( $$samerow[$xleft] eq "x" ) {
                addbud($x,$y,$xleft,$y);
                $counter++;
            print "left:\$counter is $counter\n";
            }

            # check above
            if ( $$uprow[$x] eq "x" ) {
            addbud($x,$y,$x,$yup);
            $counter++;
            #    print "above:\$counter is $counter\n";
            }

            # there yet?
            if ( $$uprow[$x] eq "x" && $yup eq "9" ) {
                print "************* FINISH ***************\n";
                print "************* FINISH ***************\n";
                $DONE = "YES";
                print "# there yet? \$DONE is $DONE\n";
                $solved = "YES";
            }

            print "after there yet?:\$counter is $counter\n";
            # not dead
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

            # dead end


            if ( $counter eq 0 ) {

                print "\nDEAD END: $x,$y \n";
                print "\t$branch: @$branch\n";

                # pop the branch
                $tm = pop @$branch;
                print ":  \@$tm = (@$tm)\n";
                until ( "@$tm" ne "" || "$#$branch" eq "-1" ) {
                    $tm = pop @$branch;
                    print "\@$tm = @$tm\n";
                    print "DURING:\t$tm contains: (@$tm)\n";
                    print "DURING: the branch has: @$branch\n";
                }
                # if last element not empty push back on the branch
                if ( "@$tm" ne "" ) {
                    print "push back on the branch\n";
                    print "\t$tm contains: (@$tm)\n";
                    print "AFTER: @$branch\n";
                    push @$branch, $tm;
                    print "FINAL: @$branch\n";
                }

                # pop the germ
                $temp = pop @$tm;
                ($xtemp, $ytemp) = split( /,/, $temp);


                if ( $xtemp ne "" && $ytemp ne "" ) {
                    $xs = $xtemp; $ys = $ytemp;
                }

                elsif ( $xtemp eq "" && $ytemp eq "" ) {
                    print "\t\$xtemp and \$ytemp are NULL\n";
                    print "\t###\$branch:$branch:@$branch\n";
                    $DONE = "YES";
                }
                print "\tPITSTOP: \$xs:($xs),\$ys:($ys)\n";
            }
            print "\n#### END of while-loop:\$DONE is $DONE\n";
            print "\n\t\$xs:($xs),\$ys:($ys),\$xp:($xp),\$yp:($yp)\n";
            print "\t###\$branch:$branch:@$branch\n";

            print "\n#### END of while-loop:\$DONE is $DONE\n";
            print "#########################################\n\n";
        } # # # # end of while-loop
    } #end of if
} # end of for


if ( $solved eq "YES" ) {
    print "***************************************************\n";
    print "***** MAZE SOLVED *********************************\n";
    print "***************************************************\n";
}
elsif ( $solved eq "NO" ) {
    print "***************************************************\n";
    print "***** MAZE NOT SOLVED *****************************\n";
    print "***************************************************\n";
}

printarray();

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#SUBROUTINES

sub addbud()
{
    $germ= "G$_[0]$_[1]";
    if ( @$germ) {
        push @$germ, "$_[2],$_[3]";
    }
    else {
        @$germ= ( "$_[2],$_[3]" );
    }
    my $arraylength = $#$germ+1;
}

sub addbranch()
{
    my $btemp = "$xstart$ystart";
    print "btemp is $btemp\n";
    $branch = "B$btemp";
    if ( @$branch ) {
         push @$branch, "$_[0]";
    }
    else {
        @$branch = ( "$_[0]" );
    }
    print "Branch Array Created $branch with these points:\n(@$branch)\n";
}

sub copyarray()
{
    for $r  ( 0 .. 10 ) {
        my $temp = "ar$r";
        my $cp = "cp$r";
        @$cp = @$temp;
        print "@$cp\n";
    }
}

sub printarray()
{
    for  $i ( 0 .. 10 ) {
        $newar = "cp$i";
        for ( $j = 0; $j < 10; $j++ ) {
                print "$$newar[$j]    ";
        }
        print "\n";
    }
}
