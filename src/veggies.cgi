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

print $query->start_html('Cyber Market-Veggies');

print<<"end_of_page";


<CENTER>

<div style = "background-color : #34ebd2; height : 120px">
<br>
<H1>Cyber Market - Vegetables</H1>

</div>


<hr>

<div style = "background-color : #ebb434; width : 800px">

<FORM name="veggies" ACTION="http://localhost/osl/project1/process_order.cgi">

<TABLE width=600 cellpadding=5

<STRONG>

<tr>
<td> <b>Quantity</b></td>
<td><b>Item</b></td>
<td><b>Total Rupees</b></td>
</tr>
</strong>

<p>

<INPUT TYPE="hidden" name="user_name" value=$user_name>

<INPUT TYPE="hidden" name="file_name" value=$file_name>

<tr><td>

<INPUT TYPE="number" min = "0" name="carrot_qty" size=5 onChange="document.veggies.carrot_total.value=parseFloat(this.value) * 1.10">

</td>
<td>

Carrots - 1.10 per kg

</td>
<td>

<right><INPUT TYPE="text" name="carrot_total" size=10 readonly></right>

</td>

<tr>
<td>

<INPUT TYPE="number" min = "0" name="tomatoes_qty" size=5 onChange="document.veggies.tomato_total.value=parseFloat(this.value) * .90">

</td>
<td>

Tomatoes - .90 per kg

</td>
<td>

<INPUT TYPE="text" name="tomato_total" size=10 readonly>

</td>

<tr>
<td>

<INPUT TYPE="number" min = "0" name="potato_qty" size=5 onChange="document.veggies.potato_total.value=parseFloat(this.value) * 1.50">

</td>
<td>

Potatoes - 1.50 per kg

</td>
<td>

<INPUT TYPE="text" name="potato_total" size=10 readonly>

</td>
<tr>
<td>

<INPUT TYPE="number" min = "0" name="corn_qty" size=5 onChange="document.veggies.corn_total.value=parseFloat(this.value) * .25">

</td>
<td>

Corn - .25 per kg

</td>
<td>

<INPUT TYPE="text" min = "0" name="corn_total" size=10 readonly>

</td>
<tr>
<td>

<INPUT TYPE="number" name="beans_qty" size=5 onChange="document.veggies.beans_total.value=parseFloat(this.value) * 2.0">

</td>
<td>

Green Beans - 2.00 per kg

</td>
<td>

<INPUT TYPE="text" name="beans_total" size=10 readonly>

</td>
</tr>

<tr>
<td> 
</td>

<td>

<INPUT TYPE="submit" value="Send Order">

</td>
</tr>

</table>

</div>

</CENTER>

end_of_page



print $query->end_html;



exit(0);
