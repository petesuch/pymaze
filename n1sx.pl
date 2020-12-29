#!/usr/bin/perl

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

my $temp = pop @$germ;
my ($xnew, $ynew) = split(/\,/, $temp);

addbranch($germ);
addbud($x,$y,$x,$ydown);
addbud($x,$y,$xright,$y);

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
#
## dead end
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

