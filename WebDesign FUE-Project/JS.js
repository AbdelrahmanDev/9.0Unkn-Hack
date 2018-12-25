function random()
		{
			var randomPassword = document.getElementById("generate");
			var count;
			var word = '';
			var char;
			for(count = 0; count < 30; ++count)
			{
				
					char = String.fromCharCode(Random());
					word += char;
			}

			randomPassword.value = word;

		}
function Random(){

	for(var x = 0; x < 10; x++)
	{
		var rand = parseInt(Math.random() * 130);

		if((rand >= 64 && rand <= 90) || (rand >= 97 && rand <= 122) || (rand >= 48 && rand <= 57))
		{
			return rand;
		}
	}
}

function Equality()
{
	if((document.getElementById("pass").value) === (document.getElementById("rPass").value))
	{
		document.getElementById("checking").innerHTML = "Yes the passwords is tepecal";
		document.getElementById("checking").style.color = "#0F0";
		document.getElementById("checking").style.fontSize = "15px";
		document.getElementById("btn").disabled  = false;

	}
	else
	{
		document.getElementById("checking").innerHTML = "The Passwords is not tepecal";
		document.getElementById("checking").style.color = "#F00";
		document.getElementById("checking").style.fontSize = "15px";
		document.getElementById("btn").disabled  = true;
	}
}

