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

print $query->start_html('Confirm Order');


$person = "user_name=" . $user_name;

$person = $person . "&file_name=" . $file_name;

&process_order($query, $file_name);



print<<"end_of_page";

<CENTER>

<div style = "background-color : #f75c7b; height : 230px">

<H1> Confirming order for $user_name </H1>
<br>

<H2> To continue ordering go <a href='http://localhost/osl/project1/market.cgi?$person'> Click Here </a></H2>

<br>

<H2> To finish go <a href='http://localhost/osl/project1/finish.cgi?$person'> Click Here </a></H2>  

<div>

</CENTER>

end_of_page


sub process_order {

     local($query, $file_name)=@_;

     @fruits = (apple_total,grapes_total,pears_total, peaches_total,pineapple_total);

     @veggies= (carrot_total, tomato_total,potato_total, corn_total,beans_total);

     $name=$query->param('user_name');

     $output_string = "";

     @named_param = $query->param;

     if ($query->param()) {

          foreach $param_name (@fruits) {

              $val = $query->param($param_name);

               if ($val) { $output_string = $output_string . $param_name . "=" . $val . ":"; }

          }

          foreach $param_name (@veggies) {

               $val = $query->param($param_name);

               if ($val) { $output_string = $output_string . $param_name . "=" . $val . ":"; }
          }
          
     }

     open(USER_FILE, ">> " . $file_name) || die "Could not process request";

     $output_string = $output_string . "\n";

     print USER_FILE $output_string;

     close(USER_FILE);

}


print $query->end_html;



exit(0);