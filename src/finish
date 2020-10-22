#!"C:\xampp\perl\bin\perl.exe"


BEGIN {

   push(@INC,'C:\xampp\perl\lib\CGI.pm');

}


use CGI;

$query = new CGI;


if ($query->param()) {

     $user_name = $query->param('user_name');

     $file_name = $query->param('file_name');

}

print $query->header;

print $query->start_html('Confirm Final Order');

print "<CENTER><div style = 'background-color : #a5ff75; height : 130px'><br><h1>Finalizing order for " . $user_name . "</h1><br></div></CENTER>";

print "<p><hr><CENTER><h2> Following are the items and total value for each </h2><p> </CENTER>";

open(USER_FILE, "< " . $file_name) || die "Could not open order file.";


print "<CENTER><div style = 'background-color : #6ac6f7; width : 600px; height : 300px'><TABLE width=300 border=2>";

$total = 0;

foreach $line(<USER_FILE>) {

     @order_line = split(/:/,$line);

     print "<tr>";

     foreach $elem (@order_line) {

          ($object,$value) = split(/=/,$elem);

           $total += $value;

          if ($value <= 0) { last; }

          print "<td bgcolor = yellow>" . $object . "</td><td bgcolor = yellow>";

          printf "%7.2f", $value , "Ruppes";

          print "</td></tr>";

     }
}

print "</TABLE><p>";

print "<b>Total amount for " . $user_name . " to pay is : $total Ruppes </b></CENTER></div><p>";


close(USER_FILE);

unlink($file_name);

print "<p><hr><CENTER><h3>Thanks for your order</h3></CENTER>";

print $query->end_html;



exit(0);