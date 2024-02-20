<?php
		$tots = array(0,0,0,0,0);
	if ($_POST) {

		
		for($tr=1;$tr<=$_POST['rw'];$tr++){
			

			// soma horizontal

			$totals = array(
				rand(5,1000),
				rand(5,1000),
				rand(5,1000),
				rand(5,1000)
			);

			// soma vertical

			$tots[0]=$tots[0]+$totals[0];
			$tots[1]=$tots[1]+$totals[1];
			$tots[2]=$tots[2]+$totals[2];
			$tots[3]=$tots[3]+$totals[3];

			// soma total

			$totL = $totals[0] + $totals[1] + $totals[2] + $totals[3];
			$tots[4]=$tots[4]+$totL;
			

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

		}


		
	}