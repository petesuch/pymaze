#!/usr/bin/perl

#   addbud and addbranch subroutines examined for testing and understanding
#

$germ="";

addbud(1,2,3,4);
print "4.1\t: $germ\n";
print "4.2\t: @$germ[0]\n";
print "4.3\t: @$germ[1]\n";

addbud(5,6,7,8);
print "5.1\t: $germ\n";
print "5.2\t: @$germ[0]\n";
print "5.3\t: @$germ[1]\n";

addbud(9,10,11,12);
print "6.1\t: $germ\n";
print "6.2\t: @$germ[0]\n";
print "6.3\t: @$germ[1]\n";

addbud(13,14,15,16);
print "7.1\t: $germ\n";
print "7.2\t: @$germ[0]\n";
print "7.3\t: @$germ[1]\n";

print "8.1\t: Array $germ contains the following points: (@$germ)\n";
print "8.2\t: The value of $germ\t: (@$germ)\n";
my $temp = pop @$germ;
my ($xnew, $ynew) = split(/\,/, $temp);
print "8.3\t: Array $germ contains the following points: (@$germ)\n";

print "Array $germ contains the following points: (@$germ)\n";
my $temp = pop @$germ;
my ($xnew, $ynew) = split(/\,/, $temp);
print "Array $germ contains the following points: (@$germ)\n";
print "The value of $germ:(@$germ)\n";



sub addbud()
{
    $germ= "G$_[0]$_[1]";
        print "1\t: $germ\n";
    if ( @$germ) {
        push @$germ, "$_[2],$_[3]";
        print "2\t: $germ\n";
    }
    else {
        @$germ= ( "$_[2],$_[3]" );
        print "3\t: $germ\n";
    }
}
