function onrequest(s) {
	if(s!=-1)
		riga[s]=1;
	var r="";
	for(var i=0;i<37;i++) {
		r=r+riga[i]+" ";
	}
    $.post("file.php", {riga: r});
    if(s>=17 && s<=36)
		riga[s]=0;
    return false;
}
