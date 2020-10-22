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

print $query->start_html('Cyber Market-fruits');

print<<"end_of_page";

<CENTER>

<div style = "background-color : #34ebd2; height : 120px">
<br>
<H1>Cyber Market - Fruits</H1>

</div>

<hr>

<div style = "background-color : #ebb434; width : 800px">

<FORM name="fruit" ACTION="http://localhost/osl/project1/process_order.cgi">

<TABLE width=600 cellpadding=5

<STRONG>

<tr>
<td><b>Quantity</b></td>
<td><b>Item </b></td>
<td><b>Total Rupees </b>
</td>
</tr>

</strong>

<p>

<INPUT TYPE="hidden" name="user_name" value=$user_name>

<INPUT TYPE="hidden" name="file_name" value=$file_name>

<tr><td>

<INPUT TYPE="number" min = "0" name="apple_qty" size=5 onChange="document.fruit.apple_total.value=parseFloat(this.value) * .80">

</td><td>

Apples - .80 per kg

</td><td>

<INPUT TYPE="text" name="apple_total" size=10 readonly> 

</td><tr><td>

<INPUT TYPE="number" min = "0" name="grapes_qty" size=5 onChange="document.fruit.grapes_total.value=parseFloat(this.value) * 1.50">

</td><td>

Green Grapes - 1.50 per kg

</td><td>

<INPUT TYPE="text" name="grapes_total" size=10 readonly>

</td><tr><td>

<INPUT TYPE="number" min = "0" name="pears_qty" size=5 onChange="document.fruit.pears_total.value=parseFloat(this.value) * 1.80">

</td><td>

Pears - 1.80 per kg

</td><td>

<INPUT TYPE="text" name="pears_total" size=10 readonly>

</td><tr><td>

<INPUT TYPE="number" min = "0" name="peaches_qty" size=5 onChange="document.fruit.peaches_total.value=parseFloat(this.value) * 1.80">

</td><td>

Peaches - 1.80 per kg

</td><td>

<INPUT TYPE="text" name="peaches_total" size=10 readonly>

</td><tr><td>

<INPUT TYPE="number" min = "0" name="pineapple_qty" size=5 onChange="document.fruit.pineapple_total.value=parseFloat(this.value) * 2.0">

</td><td>

Pineapple - 2.00 per kg

</td><td>

<INPUT TYPE="text" name="pineapple_total" size=10 readonly>

</td></tr>

<tr><td> </td><td>

<INPUT TYPE="submit" value="Send Order">

</td>
</tr>

</table>

</div>

</CENTER>

end_of_page

print $query->end_html;



exit(0);