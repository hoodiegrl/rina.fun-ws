		var title1 = '*. rina’s fun place .*'; 
		var title2 = '.* rina’s fun place *.';
		var rotate = 300;
		step = 0
		function go() {
			step++
			if (step == 3) {
				step = 1
			}
			if (step == 1) {
				document.title = title1
			}
			if (step == 2) {
				document.title = title2
			}
			setTimeout("go()", rotate	);
		}
		go();