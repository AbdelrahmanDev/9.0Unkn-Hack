<?php 

?>
	<html>

		<head> <title> Rent A Killer </title> </head>

		<body> 
			<form>
			<input type="text" placeholder="Username!!"><br>
			<input type="password" placeholder="Password!!"><br>
			<div>
				<p>Wanna Random Password??!</p>
				<script type="text/javascript">
					function Rand()
					{
					var theCode = '';

					for (var i = 1; i <= 16; i++) {
						var random = Math.ceil(Math.random() * 100 + 30);
						while(random > 126 || random <= 32)
						{
							if(random <= 32)
								random + 20;
							else if(random > 126)
								random = 38;
						}
						console.log(random);
						theCode += String.fromCharCode(random);
					}
						console.log(theCode);

					document.getElementById('randomInput').value = theCode;
					}
				</script>
				<input type="text" id = "randomInput">
				<button onclick="Rand()">Click For Random Password</button>
			</div>
			<input type="submit" name="submit">
			</form>
		</body>
	</html>
