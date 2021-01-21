#! /usr/bin/perl

#    n3.pl
#    active version of mazesolver.pl
#    may or may not be broken working on pruning variables

#   @author:  Peter A. Suchsland
#   A maze solving program inspired by a physics project

####################################################################################
#   TODO:
#
#   * use array from file and/or gui

#   *   Relavant information exchanged:
#   A point that has other go points nearby that are not immediately pursued.
#   What is immediately pursued is a go point that is a step closer to the goal.
#
#   So what are all the possible encounters?
#       An entry to the puzzle.
#       A last go point exit point.
#       A go point found to the left,right, up or down.
#       A dead end with more go points to look at.
#       A dead end with no more go points to look at.
#
#   The order of information is LIFO.
#   A germ has 3 points maximum but could I just push all the points onto the
#   branch -- bypassing the need for the germ/bud?
#
####################################################################################

#### START main program

my $SZ = 40; # 40x40 array
my @maze;
my @cp;

##################################################################################################################################################################

@maze = (
["A","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","B"],
["o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","x","o","x","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["o","o","o","o","o","x","x","x","o","o","o","o","o","o","o","x","x","x","x","x","x","x","x","o","x","x","x","x","x","x","x","x","x","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","x","o","o","x","o","o","x","o","x","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","x","o","o","o","o","x","x","x","x","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","x","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o"],
["o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","x","x","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o"],
["o","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o"],
["o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","x","x","x","x","o","o","o","o","o","o"],
["o","o","x","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","x","x","o","o","o","o"],
["o","o","x","o","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","x","o","x","o","o","o","o"],
["x","x","x","x","x","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","x","x","o","x","o","o","o","o"],
["x","o","o","o","o","x","x","x","o","o","x","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","x","x","o","o","x","o","o","o","o"],
["x","o","o","o","o","x","o","x","o","x","x","x","o","o","o","o","o","o","o","o","x","x","x","o","o","o","o","o","o","o","o","x","o","o","o","x","o","o","o","o"],
["x","o","o","o","o","x","o","x","o","o","x","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","x","x","o","o","o"],
["x","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","x","o","x","o","o","o","x","x","x","o","o","x","o","o","o","o","x","o","o","o"],
["x","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","x","x","o","x","x","x","x","x","x","x","o","x","x","x","x","x","o","o","o","x","o","o","o"],
["x","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","x","x","x","x","o","o","o","o","x","o","o","x","o","o","o","x","o","o","o","x","x","o","o"],
["x","o","o","o","o","x","o","x","o","x","x","x","x","o","o","o","o","x","o","o","x","o","o","o","o","x","o","o","x","o","o","o","x","o","o","o","o","x","o","o"],
["x","o","o","x","x","x","o","x","o","x","o","o","x","o","o","o","o","x","o","o","x","x","o","o","o","x","o","o","x","o","o","o","x","o","o","o","o","x","o","o"],
["x","o","o","x","o","x","o","x","o","x","o","o","x","o","o","o","o","x","o","o","o","x","o","o","o","x","o","o","x","x","x","x","x","o","o","o","o","x","o","o"],
["x","o","o","x","o","x","o","x","x","x","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","x","o","o","o","o","o","o","x","o","o","o","o","x","o","o"],
["x","o","o","x","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o"],
["x","o","o","x","o","x","o","o","o","o","o","o","x","o","o","o","o","x","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","x","o","o"],
["x","o","o","x","o","x","o","o","o","o","o","o","x","x","x","x","x","x","x","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","x","o","o"],
["x","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","x","x","x","o","o"],
["x","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o"],
["x","o","o","x","o","o","o","o","o","o","o","o","x","x","x","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","x","o"],
["x","o","o","x","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o"],
["x","o","x","x","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","x","x","o","o","o","o","x","o"],
["x","o","o","x","o","o","o","o","o","o","x","x","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","x","x","o","o","o","x","o"],
["x","o","o","x","o","o","o","o","o","o","x","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","x","o","o","o","x","o"],
["x","o","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","x","x","x","o","o","x","o","o","x","o","x","x","x","o"],
["x","o","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","x","o","o","x","o","o","x","o","x","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","x","o","o","x","o","o","x","x","x","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","x","o","o","x","o","o","o","o","o","o","o","o"],
["x","o","o","o","o","o","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","x","o","o","x","o","o","o","o","o","o","o","o"],
["x","o","o","o","o","o","o","o","o","o","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","x","o","o","x","o","o","o","o","o","o","o","o"],
["x","x","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","x","x","x","x","o","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","Z"]
);

##################################################################################################################################################################


@cp = @maze; # Mark-up the copy not the original
my $go = "x"; my $mark = "+"; # Characters in the maze
my $x; my $y; # Head point
my $xp; my $yp; # Previous point
my $temp;
my $DONE; my $SOLVED;
my $tm;
my $germ; my @branch;
my $j; my $i;

### find an entry to the maze first
for $j ( 0 .. $SZ ) { # Look at first row

    ### Here is an entry point
    if ( $cp[0][$j] eq $go ) {  # Enter maze
        last if ( $SOLVED eq "YES" );
        $DONE = "NO";
        $xentry =  $j; $yentry =  0;
        print "*** Entering Maze at: ($xentry,$yentry) ***\n";
        $x = $xentry; $y = $yentry;
        do {
            print "# Begin ############################################################\n";
            printarray();
            printvariables();
            $germ = "";
            $SOLVED = "NO";
            $xp = $x; $yp = $y;

            $cp[$y][$x] = "+"; # mark that we have been here before
            ### deja vu that strange feeling you get that you've been here before
            print "#2 marking: \$cp[$y][$x] with (+) symbol\n";

            my $xright = $x+1; my $yright = $y; my $xleft = $x-1; my $yleft = $y;
            my $xup = $x; my $yup =  $y+1; my $xdown = $x; my $ydown = $y-1;
            my $counter = 0;

            ### check below
            if ( $cp[$ydown][$xdown] eq $go ) {
                addbud($x,$y,$xdown,$ydown);
                $counter++;
            }
            ### check to the right
            if ( $cp[$yright][$xright] eq $go ) {
                addbud($x,$y,$xright,$yright);
                $counter++;
            }
            ### check to the left
            if ( $cp[$yleft][$xleft] eq $go ) {
                addbud($x,$y,$xleft,$yleft);
                $counter++;
            }
            ### check above
            if ( $cp[$yup][$xup] eq $go ) {
                addbud($x,$y,$xup,$yup);
                $counter++;
            }
            ### there yet?
            if ( $cp[$yup][$xup] eq $go && $yup eq $SZ ) {  # if yup is a go and the last
                $SOLVED = "YES";
                $DONE = "YES";
                $cp[$yup][$xup] = $mark; # if its there mark it
                #break;
            }
            ### not dead
            if ( $counter gt 0 ) {
                addbranch($germ);
                my $temp = pop @$germ;
                (my $chx, my $chy) = split(/\,/, $temp);
                print "After split: \$chx: $chx, \$chy: $chy\n";
                if ( $chx ne "" && $chy ne "" ) {
                    $x = $chx; $y = $chy;
                }
            }
            ### dead end
            if ( $counter eq 0 ) {
                print "DEAD END: $x,$y \n";
                my $tm = pop @branch; # pop the branch
                print "\@$tm = (@$tm)\n";
                until ( "@$tm" ne "" || "$#branch" eq "-1" ) {
                    $tm = pop @branch;
                }
                ### if the last element is not empty -- push back on the branch
                if ( "@$tm" ne "" ) {
                    push @branch, $tm;
                }
                ### pop the bud
                $temp = pop @$tm;
                (my $chx, my $chy) = split( /\,/, $temp);
                print "#Pop the bud: After split: \$chx: $chx, \$chy: $chy\n";
                if ( $chx ne "" && $chy ne "" ) {
                    $x = $chx; $y = $chy;
                }
                elsif ( $chx eq "" && $chy eq "" ) {
                    $DONE = "YES";
                }
                print "#19 PITSTOP: \$x:$x,\$y:$y\n";
            }    # end of dead end

            printvariables();
            printarray();  # uncomment this to see the maze
            print "# Sleeping #########################################################\n";
            #sleep 1;
        } while  ("$DONE" ne "YES" ); # End of do-while loop
    } # End of if
} # End of for


if ( $SOLVED eq "YES" ) {
    print "********** MAZE SOLVED **************************************************\n";
}
elsif ( $SOLVED eq "NO" ) {
    print "*****  MAZE NOT SOLVED **************************************************\n";
}

#printarray();  # uncomment this to see the maze
#### END main program
#
##########################################################
#
####    SUBROUTINES
sub addbud()
{
    print("Starting addbud... ");
    $germ = "G$_[0]$_[1]";
    if ( @$germ ) {
        push @$germ, "$_[2],$_[3]";
        print("\@$germ: @$germ\n")
    }
    else {
        @$germ = ( "$_[2],$_[3]" );
        print("\@$germ: @$germ\n")
    }
}
sub addbranch()
{
    print("Starting addbranch...\n");
    if ( @branch ) { # if one already exists
         push @branch, "$_[0]";
    }
    else {
        @branch = ( "$_[0]" );
    }
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

sub printvariables()
{
    print("************************************************************************
        \$x:$x,\$y:$y\t\$xentry:$xentry,\$yentry:$yentry\t\$xp:$xp,\$yp:$yp
        \$temp:$temp \$DONE:$DONE \$SOLVED:$SOLVED
        \$tm:$tm
        \$germ:$germ
        \@branch:\n@branch\n************************************************************************\n")
}
