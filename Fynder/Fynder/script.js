function slice_text(){
    var mail =  document.getElementById("mail").value; 
    var sliced_mail = mail.substring(
        mail.lastIndexOf("@") +1,
        mail.lastIndexOf(".")
    );

    var sliced_mail= sliced_mail + " " + "college";
    console.log(sliced_mail)
}