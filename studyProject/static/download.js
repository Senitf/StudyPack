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
//this.options[this.selectedIndex].value
function add_download_list(idvalue){
    var target = document.getElementById(idvalue);
    return target.options[target.selectedIndex].value;
}
function add_download_simul(){
    var check_count = document.getElementsByClassName("text_number").length;
    var count=0;
    var textnumber = new Array();
    for(var i=0; i<check_count; i++){
        if(document.getElementsByClassName("text_number")[i].checked){
            textnumber[count] = document.getElementsByClassName("text_number")[i].value;
            count++;
        }
    }
    
    
    var index_file=1;
    for(var i=0; i<count; i++){
        var newTR = document.createElement("tr");
        var td = `${add_download_list("simul_year")}`;
        td = `${td}_${add_download_list("simul_month")}`;
        td = `${td}_${add_download_list("simul_grade")}`;

        var common_category = document.getElementById("common_category");
        if(common_category.options[common_category.selectedIndex].value == "handmade"){
            td = `${td}_handmade_${textnumber[i]}_${textnumber[i]}`;
        }
        else{
            
        }

        newTR.innerHTML = `<td class="file_order">${index_file}</td> <td>${td}</td> <td><input type="checkbox" onchange="handdle_checkbox_change(this);" class="download_file_list" /></td>`;
        var p = document.getElementById("file_table");
        p.appendChild(newTR);
        index_file++;
        td="";
    }
}