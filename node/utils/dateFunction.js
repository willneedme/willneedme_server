const getDateStr = (myDate) =>{
	let year = myDate.getFullYear();
	let month = (myDate.getMonth() + 1);
	let day = myDate.getDate();
    let hour = myDate.getHours();
    let minute = myDate.getMinutes();
    let seconds = myDate.getSeconds();
    let milliseconds = myDate.getMilliseconds()
	
	month = (month < 10) ? "0" + String(month) : month;
	day = (day < 10) ? "0" + String(day) : day;
	
	return  year + '-' + month + '-' + day + " " + hour + ":" + minute + ":" + seconds +"." + milliseconds;
}
const week = () => {
  var d = new Date();
  var dayOfMonth = d.getDate();
  d.setDate(dayOfMonth);
  return getDateStr(d);
}

module.exports = {
  week
}