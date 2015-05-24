var cvs, c;

var usMap = new Image();

var listOfRegions;
var listOfStatistics;

function start() {
	cvs = document.getElementById("cvs");
	c = cvs.getContext("2d");
	getListOfRegions();
	usMap.src = "usmap.png"
}




/*
Sends a request to the server for a list of valid regions.
*/
function getListOfRegions() {
	ajax("requestType=getListOfRegions");
}

/*
Stores the list of regions given by the server and calls getListOfStatistics().
*/
function getListOfRegions_handleResponse(response) {
	response.splice(0, 1);
	listOfRegions = response;
	getListOfStatistics();
}

/*
Send a request to the server for a list of valid statistic names.
*/
function getListOfStatistics() {
	ajax("requestType=getListOfStatistics");
}

/*
Stores the list of statistics given by the server
and calls setFormContents().
*/
function getListOfStatistics_handleResponse(response) {
	listOfStatistics = response;
	setFormContents();
}

/*
Edits the input-form to reflect user-choices and server data
*/
function setFormContents() {
	var statValue, summaryValue, stateValue;
	var singleyearValue, startyearValue, endyearValue;

	// For each form-object, we check whether it exists
	// before we check its value to prevent run-time errors
	if(document.getElementById("statistic")) {
		statValue = document.getElementById("statistic").value;
	}
	if(document.getElementById("state map")) {
		if(document.getElementById("state map").checked) {
			summaryValue = "state map";
		}
	}
	if(document.getElementById("bar chart")) {
		if(document.getElementById("bar chart").checked) {
			summaryValue = "bar chart";
		}
	}
	if(document.getElementById("line graph")) {
		if(document.getElementById("line graph").checked) {
			summaryValue = "line graph";
		}
	}
	if(document.getElementById("stateSelector")) {
		stateValue = document.getElementById("stateSelector").value;
	}
	if(document.getElementById("singleyear")) {
		singleyearValue = document.getElementById("singleyear").value;
	}
	if(document.getElementById("startyear")) {
		startyearValue = document.getElementById("startyear").value;
	}
	if(document.getElementById("endyear")) {
		endyearValue = document.getElementById("endyear").value;
	}

	if(!summaryValue) {
		// set to default if it hasn't been given a value by the user
		summaryValue = "state map";
	}

	var showFiftyStates = false;
	var showSingleYear = true;
	if(summaryValue == "line graph") {
		showFiftyStates = true;
		showSingleYear = false;
	}

	// construct the dropdown select element to let user select a statistic
	var newHTML = "<select id=\"statistic\" name=\"statistic\" \
		onchange=\"formChanged();\">";
	for(var i=0; i<listOfStatistics.length; i++) {
		newHTML += "<option value=\"" + listOfStatistics[i] + "\">"
			+ listOfStatistics[i] + "</option>";
	}
	newHTML += "</select>"
	document.getElementById("statisticSelect").innerHTML = newHTML;


	// construct the radio buttons for the user
	// to select how s(he) wants the data displayed
	newHTML = "<input type=\"radio\" id=\"state map\" name=\"summary\" \
		value=\"state map\" onchange=\"formChanged();\"> State Map <br> \
		<input type=\"radio\" id=\"bar chart\" name=\"summary\" \
		value=\"bar chart\" onchange=\"formChanged();\"> \
		Multi-State Bar Chart<br> <input type=\"radio\" \
		id=\"line graph\" name=\"summary\" value=\"line graph\" \
		onchange=\"formChanged();\"> Single Region Over Time";
	document.getElementById("summarySelect").innerHTML = newHTML;


	// If appropriate, create a dropdown select element
	// for the user to choose a state
	if(showFiftyStates) {
		newHTML = "<select id=\"stateSelector\" name=\"stateSelector\" \
		onchange=\"formChanged();\">";
		for(var i=0; i<listOfRegions.length; i++) {
			newHTML += "<option value=\"" + listOfRegions[i] + "\">"
				+ listOfRegions[i] + "</option>";
		}
		newHTML += "</select>"
		document.getElementById("stateSelect").innerHTML = newHTML;
	}
	else {
		document.getElementById("stateSelect").innerHTML = "";
	}
	


	// If we are looking only at one year, display one textbox,
	// otherwise display two textboxes
	if(showSingleYear) {
		newHTML = "Year: <input type=\"text\"id=\"singleyear\" \
		name=\"singleyear\" placeholder=\"{singleyear_hint} \
		\"value=\"2015\" maxlength=\"4\" size=\"4\" \
		onkeyup=\"formChanged(true);\">";
	}
	else {
		newHTML = "Year Range:<input type=\"text\" id=\"startyear\" \
		name=\"startyear\" value=\"1776\"placeholder=\"{startyear_hint}\" \
		maxlength=\"4\" size=\"4\" onkeyup=\"formChanged(true);\">to \
		<input type=\"text\" id=\"endyear\" name=\"endyear\" value=\"2015\" \
		placeholder=\"{endyear_hint}\" maxlength=\"4\" size=\"4\" \
		onkeyup=\"formChanged(true);\">";
	}
	document.getElementById("yearSelect").innerHTML = newHTML;

	// give each new form element the value of its old predecessor
	document.getElementById("statistic").value = statValue;
	document.getElementById(summaryValue).checked = true;
	if(singleyearValue && document.getElementById("singleyear")) {
		document.getElementById("singleyear").value = singleyearValue;
	}
	if(endyearValue && document.getElementById("endyear")) {
		document.getElementById("endyear").value = endyearValue;
	}
	if(startyearValue && document.getElementById("startyear")) {
		document.getElementById("startyear").value = startyearValue;
	}

	if(document.getElementById("stateSelector")) {
		document.getElementById("stateSelector").value = stateValue;
	}
	
}

/*
This function takes the values of the user's form
and converts them into a standard POST format:

name0=value0&name1=value1&name2=value2...
*/
function generateRequestString() {
	var rtn = "requestType=getData";

	var obj = document.getElementById("statistic");
	if(obj)
		rtn += "&statistic=" + obj.value;
	else
		rtn += "&statistic=NA"

	obj = document.getElementById("myForm");
	if(obj) {
		for(var i=0; i<obj.length; i++) {
			if(obj[i].checked) {
				rtn += "&summary=" + obj[i].value;
				break;
			}
		}
	}
	else
		rtn += "&summary=NA"

	obj = document.getElementById("stateSelector");
	if(obj)
		rtn += "&state=" + obj.value;
	else
		rtn += "&state=NA"

	obj = document.getElementById("startyear");
	if(obj)
		rtn += "&startyear=" + obj.value;
	else
		rtn += "&startyear=NA"

	obj = document.getElementById("endyear");
	if(obj)
		rtn += "&endyear=" + obj.value;
	else
		rtn += "&endyear=NA"

	obj = document.getElementById("singleyear");
	if(obj)
		rtn += "&singleyear=" + obj.value;
	else
		rtn += "&singleyear=NA"

	return rtn;
}

/*
This function is called when the form is changed by the user.
It begins two processes:
	(1) editing the form in response to user input
	(2) getting relevant information from the server.
*/
function formChanged(didTextBoxChange) {
	if(didTextBoxChange) {
		// do nothing
	}
	else {
		setFormContents();
	}
	var requestString = generateRequestString();
	ajax(requestString)
}

/*
Appends requestString to "webapp.py?", thereby calling the webapp script.
When a reponse is received,
it is passed as a parameter to parseServerResponse().
*/
function ajax(requestString) {
	if(window.XMLHttpRequest)
	{
		ajaxObj = new XMLHttpRequest();
	}
	else
	{
		ajaxObj = new ActiveXObject("Microsoft.XMLHTTP");
	}
	
	ajaxObj.onreadystatechange = function()
	{
		if(ajaxObj.readyState==4)
		{
			parseServerResponse(ajaxObj.responseText);
		}
	}
	ajaxObj.open("GET","webapp.py?"+requestString,true);
	ajaxObj.send();
}

/*
Separates the server's response into
	(1) a literal repetition of the client's request
	(2) data responding to the request in csv-format
It then calls dealWithServerResponse,
which sends this parsed data to the appropriate drawing method.
*/
function parseServerResponse(serverResponse) {
	// removes a "\n" character from the beginning
	serverResponse = serverResponse.substr(1);
	var responseArr = serverResponse.split(/\r\n/g);
	var originalRequest = responseArr[0];
	originalRequest = originalRequest.split(/&/g);
	var originalRequestDictionary = new Array();
	for(var i=0; i<originalRequest.length; i++) {
		var spitValues = originalRequest[i].split("=");
		originalRequestDictionary[spitValues[0]] = spitValues[1];
	}
	responseArr.splice(0,1)
	var response = responseArr;
	for(var i=0; i<response.length; i++) {
		response[i] = response[i].split(/,/g);
	}
	dealWithServerResponse(originalRequestDictionary, response);
}

/*
Decides which function to pass the server response from,
after this response is parsed by parseServerResponse().
*/
function dealWithServerResponse(request, response) {
	var csvText = "";
	for(var i=0; i<response.length; i++) {
		 csvText += response[i] + "\n";
	}
	document.getElementById("csv_data").value = 
		csvText.substr(1, csvText.length-3);
	
	if(request["requestType"] == "getListOfRegions") {
		getListOfRegions_handleResponse(response);
	}
	else if(request["requestType"] == "getListOfStatistics") {
		getListOfStatistics_handleResponse(response);
	}
	else if(request["requestType"] == "getData") {
		if(response.length < 2) {
			// do nothing - form isn't done being filled in
			return;
		}
		else if(request["summary"] == "state map") {
			drawColorMap(request, response);
			connectLinkToCanvas();
		}
		else if(request["summary"] == "bar chart") {
			drawBarChart(request, response);
			connectLinkToCanvas();
		}
		else if(request["summary"] == "line graph") {
			drawLineGraph(request, response);
			connectLinkToCanvas();
		}
		else {
			alert("Server Error (request summary invalid - "
				+ request["summary"] + ")");
		}
	}
	else {
		alert("Server Error (requestType not correctly sent back)"
			+ "{" + request + "}{" + response + "}");
	}
}

function connectLinkToCanvas() {
	var linkElement = document.getElementById("linkToDownloadCanvas");
    linkElement.href = document.getElementById("cvs").toDataURL();
}
