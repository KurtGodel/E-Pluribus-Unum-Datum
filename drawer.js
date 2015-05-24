var fontSize = 12;
var colorScale = new Image();
colorScale.src = "color scale.png";

/*
Draws a colored map of the 50 states
when given the original request in dictionary form
and the received data in csv form.
*/
function drawColorMap(request, receivedData) {
	var buffer = document.createElement("canvas");
	buffer.width = usMap.width;
	buffer.height = usMap.height;

	var washingtonDC = receivedData[9];
	receivedData.splice(9, 1);
	receivedData.push(washingtonDC);

	var min = 1e9999;
	var max = -1e9999;
	for(var i=1; i<receivedData.length; i++) {
		if(parseFloat(receivedData[i][2]) > max) {
			max = parseFloat(receivedData[i][2]);
		}
		else if(parseFloat(receivedData[i][2]) < min) {
			min = parseFloat(receivedData[i][2]);
		}
	}

	var context = buffer.getContext("2d");
	context.drawImage(usMap, 0, 0);
	var imgData = context.getImageData(0, 0, buffer.width, buffer.height);

	for(var i=0; i<imgData.data.length; i+=4) {
		var state = Math.round(imgData.data[i]/5);
		if(state == 0) {
			// background
			imgData.data[i] = 255;
			imgData.data[i+1] = 255;
			imgData.data[i+2] = 255;
			imgData.data[i+3] = 0;
		}
		else {
			// a state
			var value = parseFloat(receivedData[state][2]);
			value = (value-min)/(max-min);
			if(value > 0.5) {
				imgData.data[i] = 255;
				imgData.data[i+1] = 0;
				imgData.data[i+2] = Math.floor(255 - 255*2*(2*value-1));
			}
			else {
				imgData.data[i] = Math.floor(510*value);
				imgData.data[i+1] = 0;
				imgData.data[i+2] = 255;
			}
		}
	}
	c.putImageData(imgData, 0, 0);

	// EX: Populaiton (1989)
	var titleStr = receivedData[0][2];
	titleStr += " (" + receivedData[1][1] + ")";
	c.font = "24px Arial";
	fontSize = 24;
	drawLabel(titleStr, cvs.width*0.6, 50);
	c.font = "12px Arial";
	fontSize = 12;

	c.drawImage(colorScale, 270, 564, 450, 30);
	drawLabel(min, 270, 560);
	drawLabel(max, 720, 560);
}

/*
Draws a bar chart when given the original request in dictionary form
and the received data in csv form.
*/
function drawBarChart(request, receivedData) {
	for(var i=1; i<receivedData.length; i++) {
		for(var j=1; j<receivedData[i].length; j++) {
			receivedData[i][j] = parseFloat(receivedData[i][j]);
		}
	}

	var maxValue = -1e1000;
	for(var i=1; i<receivedData.length; i++) {
		if(receivedData[i][2] > maxValue) {
			maxValue = receivedData[i][2];
		}
	}

	cvs.width = cvs.width;

	var w = cvs.width;
	var h = cvs.height;

	// EX: "Population (1989)"
	var titleStr = "";
	titleStr += receivedData[0][2];
	titleStr += " (" + receivedData[1][1] + ")";
	c.font = "24px Arial";
	fontSize = 24;
	drawLabel(titleStr, w/2, 50);
	c.font = "12px Arial";
	fontSize = 12;

	c.lineWidth = 4;
	drawArrow(50, h-140, 50, 100);
	drawArrow(48, h-140, w-20, h-140);
	for(var i=1; i<listOfRegions.length; i++) {
		drawLabel(receivedData[i][0], i/50*(w-110)+50, h-130, Math.PI/2);
	}
	var y = 0;
	for(var i=1; i<listOfRegions.length; i++) {
		y = receivedData[i][2]/maxValue;
		c.fillRect(i/50*(w-110)+50 - (w-110)/50/4, h-140-(h-280)*y,
			(w-110)/50/2, (h-280)*y);
	}

	c.beginPath();
	c.moveTo(45, 140);
	c.lineTo(55, 140);
	c.stroke();
	c.fillText(numberToString(maxValue), 0, 140);
}

/*
Draws a line graph when given the original request in dictionary form
and the received data in csv form.
*/
function drawLineGraph(request, receivedData) {
	if(receivedData.length == 1) {
		// error occured - probably the form isn't completely filled in
		return;
	}
	var minYear = 1e1000;
	var maxYear = -1e1000;
	var maxValue = -1e1000;
	var minI = -1;
	var maxI = -1;

	for(var i=1; i<receivedData.length; i++) {
		if(parseFloat(receivedData[i][2]) > maxValue) {
			maxValue = parseFloat(receivedData[i][2]);
		}
		if(parseFloat(receivedData[i][2]) != 0 &&
			parseFloat(receivedData[i][1]) < minYear) {
			minYear = parseFloat(receivedData[i][1]);
			minI = i;
		}
		if(parseFloat(receivedData[i][2]) != 0 &&
			parseFloat(receivedData[i][1]) > maxYear) {
			maxYear = parseFloat(receivedData[i][1]);
			maxI = i;
		}
	}

	cvs.width = cvs.width;

	var w = cvs.width;
	var h = cvs.height;

	c.font = "24px Arial";
	fontSize = 24;
	// EX: "Population of Nebraska (1972 - 2012)"
	var titleStr = "";
	titleStr += receivedData[0][2];
	titleStr += " of " + request["state"];
	titleStr += " (" + minYear + " - " + maxYear + ")";
	drawLabel(titleStr, w/2, 50);
	c.font = "12px Arial";
	fontSize = 12;

	c.beginPath();
	c.moveTo(45, 150);
	c.lineTo(55, 150);
	c.stroke();
	c.fillText(numberToString(maxValue), 0, 156);

	c.lineWidth = 4;
	drawArrow(50, h-50, 50, 100);
	drawArrow(48, h-50, w-20, h-50);

	c.beginPath();
	var x = 0;
	var y = parseFloat(receivedData[minI][2])/maxValue;
	c.moveTo((w-100)*x+50, (h-200) * (1-y) + 150);
	for(var i=minI+1; i<=maxI; i++) {
		x = (parseFloat(receivedData[i][1])-minYear)/(maxYear-minYear);
		y = parseFloat(receivedData[i][2])/maxValue;
		c.lineTo((w-100)*x+50, (h-200) * (1-y) + 150);
	}
	c.stroke();

	if(minYear != maxYear) {
		for(var i=minYear; i<=maxYear; i+=10) {
			var t = Math.floor(i/10)*10;
			x = (t-minYear)/(maxYear-minYear);
			drawLabel(t, (w-100)*x+50, h-40, Math.PI/2);
		}

		c.beginPath();
		for(var i=minYear; i<=maxYear; i+=10) {
			var t = Math.floor(i/10)*10;
			x = (t-minYear)/(maxYear-minYear);
			c.moveTo((w-100)*x+50, h-45);
			c.lineTo((w-100)*x+50, h-55);
		}
	}
}

/*
This function converts the inputed number into a string of limited length.
*/
function numberToString(x) {
	if(x < 1) {
		return Math.round(1000*x)/1000+"";
	}
	else if(x < 10) {
		return Math.round(100*x)/100+"";
	}
	else if(x < 100) {
		return Math.round(10*x)/10+"";
	}
	else if(x < 1000) {
		return Math.round(x)+"";
	}
	else {
		var e = Math.floor(Math.log(x)/Math.log(10));
		x /= Math.pow(10,e);
		return Math.round(100*x)/100 + "e"+e;
	}
}

/*
This function draws an arrow from (x1,y1) to (x2,y2).
*/
function drawArrow(x1, y1, x2, y2) {
	var scale = 3*Math.sqrt(c.lineWidth);

	var deltaX = x2-x1;
	var deltaY = y2-y1;
	var oldLen = Math.sqrt(deltaX*deltaX+deltaY*deltaY);
	var angle = 0.523598776;
	deltaX *= scale/oldLen*3;
	deltaY *= scale/oldLen*3;

	// draw head
	c.beginPath();
	c.moveTo(x2,y2);
	c.lineTo(x2-Math.sin(angle)*deltaY-Math.cos(angle)*deltaX,y2+
		Math.sin(angle)*deltaX-Math.cos(angle)*deltaY);
	c.lineTo(x2+Math.sin(angle)*deltaY-Math.cos(angle)*deltaX,y2-
		Math.sin(angle)*deltaX-Math.cos(angle)*deltaY);
	c.fill();

	// draw line
	c.beginPath();
	c.moveTo(x1,y1);
	c.lineTo(x2 - Math.cos(angle)*deltaX,y2 - Math.cos(angle)*deltaY);
	c.stroke();
}

/*
Draws a string (str) centered on (x,y) with an optional rotation
*/
function drawLabel(str, x, y, angle) {
	if(angle == undefined || angle == 0) {
		c.fillText(str, x-c.measureText(str).width/2, y+fontSize/4);
	}
	else {
		c.translate(x,y);
		c.rotate(angle);
		c.fillText(str,0,fontSize/4);
		c.rotate(-1*angle);
		c.translate(-1*x,-1*y);
	}
}
