#!"C:\xampp\perl\bin\perl.exe"

BEGIN {

        push(@INC,'C:\xampp\perl\lib\CGI.pm');


}

use CGI;

$query = new CGI;

$user_name = "";

if ($query->param()) {

     $user_name = $query->param('user_name');
}


if ($user_name) {

     $file_name = $query->param('file_name');

}


print $query->header;

print $query->start_html('Cyber Market');

print<<"end_of_page";


<HTML>

<HEAD><TITLE> The Cyber Market </TITLE>


<SCRIPT LANGUAGE="JavaScript">

function GenerateFileName(user_name) {

     var time = new Date()

     var time1 = time.getMonth()

     var time2 = time.getDay()

     var time3 = time.getYear()

     var filename = user_name + time1 + time2 + time3 + ".ord"

     document.MarketForm.file_name.value = filename

}



function SubmitNow(category) {

	 var temp = document.MarketForm.user_name.value
	 var res = temp.split(" ").join("")

	 if (res == ""){
	 	
	 	alert('Please Enter your name')
	 	window.location.href = "http://localhost/osl/Project1/market.cgi?"
	 }

	else {

     var suserfile = "user_name=" + document.MarketForm.user_name.value

     suserfile = suserfile + "&file_name=" + document.MarketForm.file_name.value

     if (category == "fruit") { window.location.href = "http://localhost/osl/project1/fruit.cgi?" + suserfile }

     else { window.location.href = "http://localhost/osl/project1/veggies.cgi?" + suserfile }

     }

}


</SCRIPT>


</HEAD>

<BODY>
<CENTER>
 
<div style = "background-color : #3486eb; height : 100px; valign">
<br><H1> Welcome to the Cyber Market </H1> 
</div>


<hr>

<div style = "background-color : lightblue; height : 250px; width : 400px">
<br>
<H3> Please enter your name </H3>

<p> <FORM name="MarketForm">

<p> Your Name: <INPUT TYPE="text" size=30 name=user_name value="$user_name" onChange="GenerateFileName(this.value)">

<INPUT TYPE="hidden" name="file_name" value=$file_name>

<br><br>

<H3> Please select your choice </H3>

<p align = "CENTER"> Fruit:<INPUT TYPE="radio" name="category" onClick="SubmitNow('fruit')">

<p align = "CENter"> Veggies:<INPUT TYPE="radio" name="category" onClick="SubmitNow('veggies')">

</div>

</CENTER>
</BODY>

end_of_page



print $query->end_html;



exit(0);
