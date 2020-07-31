function display_on(targetName){
    document.getElementById(targetName).style.display = 'block';
}
function display_off(targetName){
    document.getElementById(targetName).style.display = 'none';
}
function display_control(value, className){
    if(value === "simul"){
        document.getElementsByClassName(className)[0].checked = false;
        display_off("form_textbook");
        display_on("form_simul");
        // required_control("simul", true);
        // required_control("textbook", false);
        
    }
    else if(value === "textbook"){
        document.getElementsByClassName(className)[1].checked = false;
        display_off("form_simul");
        display_on("form_textbook");
        // required_control("textbook", true);
        // required_control("simul", false);
        
    }
    else{
        display_off("form_simul");
        display_off("form_textbook");
    }

    var check_count = document.getElementsByClassName("form_common").length;
    for(var i=0; i<check_count; i++){
        document.getElementsByClassName("form_common")[i].style.display = "block";
    }
}
function display_change(value){
    if(value === "handmade"){
        display_on("form_handmade");
        display_off("form_problems");
    }
    else if(value === "problems"){
        display_off("form_handmade");
        display_on("form_problems");
    }

}