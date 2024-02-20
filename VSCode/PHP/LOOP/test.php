<?php
	if ($_POST) {

		$tots = array(0,0,0,0,0);

		for($tr=1;$tr<=$_POST['rw'];$tr++){


			// soma horizontal

			$totals = array(
				rand(5,1000),
				rand(5,1000),
				rand(5,1000),
				rand(5,1000)
			);

			

			echo
			'
			<tr>
				<td>Nome-'.$tr.'</td>
				<td>'.$totals[0].'</td>
				<td>'.$totals[1].'</td>
				<td>'.$totals[2].'</td>
				<td>'.$totals[3].'</td>
				<td>'.$totL.'</td>
			</tr>
			';

			echo"";

			
		}


		
	}