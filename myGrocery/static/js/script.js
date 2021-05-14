/* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
var dropdown = document.getElementsByClassName("dropdown-btn");
var i;
for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
  this.classList.toggle("active");
  var dropdownContent = this.nextElementSibling;
  if (dropdownContent.style.display === "block") {
  	dropdownContent.style.display = "none";
  } 
  else {
	  dropdownContent.style.display = "block";
	}
  });
}

// Category Update Script
function editCategory(id)
{
  nameEle = document.getElementById('cat_name_'+id);
  remarkEle = document.getElementById('cat_remark_'+id);
  editEle = document.getElementById('edit_action_'+id);
  nameVal = nameEle.textContent;
  remarkVal = remarkEle.textContent;
  appendHtmlName = `<input type="text" id="name_`+id+`" value="`+nameVal+`" required/><span class="text-danger js_valid" id="validation_msg_`+id+`"></span>`;
  appendHtmlRemark = `<input type="text" id="remark_`+id+`" value="`+remarkVal+`"/>`;
  appendTickBtn = `<a href="javascript:void(0)" title="Save" onclick="saveCategory('`+id+`')"><i class="fas fa-save text-success"></i></a> <a href="javascript:void(0)" title="Cancel" onclick="cancelCategory('`+id+`','`+nameVal+`','`+remarkVal+`')"><i class="fas fa-times-circle text-danger"></i></a>`;
  nameEle.innerHTML = appendHtmlName;
  remarkEle.innerHTML = appendHtmlRemark;
  editEle.innerHTML = appendTickBtn;
}
// Category Update Script

// Cancel Category Update Script
function cancelCategory(id,name,remark)
{
  nameEle = document.getElementById('cat_name_'+id);
  remarkEle = document.getElementById('cat_remark_'+id);
  editEle = document.getElementById('edit_action_'+id);
  appendTickBtn = `<a href="javascript:void(0)" title="Edit" onclick="editCategory('`+id+`')"><i class="fas fa-pencil-alt text-success"></i></a>`;
  nameEle.innerText = name;
  remarkEle.innerText = remark;
  editEle.innerHTML = appendTickBtn;
}
// Cancel Category Update Script

// Save Category Update Script
function saveCategory(id)
{
  nameInputEle = document.getElementById('name_'+id);
  remarkInputEle = document.getElementById('remark_'+id);
  if(nameInputEle.value == "")
  {
    document.getElementById('validation_msg_'+id).innerText = "Name field if required";
    return false;
  }
  const xhr = new XMLHttpRequest();
  xhr.onload = function()
  {
    console.log(this.response);
    nameEle = document.getElementById('cat_name_'+id);
    remarkEle = document.getElementById('cat_remark_'+id);
    editEle = document.getElementById('edit_action_'+id);
    appendTickBtn = `<a href="javascript:void(0)" title="Edit" onclick="editCategory('`+id+`')"><i class="fas fa-pencil-alt text-success"></i></a>`;
    nameEle.innerText = nameInputEle.value;
    remarkEle.innerText = remarkInputEle.value;
    editEle.innerHTML = appendTickBtn;
  };
  xhr.open("POST","http://127.0.0.1/projects/personal/myGrocery/category/update");
  xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  xhr.send("id="+id+"&name="+nameInputEle.value+"&remark="+remarkInputEle.value+"");
}
// Save Category Update Script

// var timePeriodInMs = 4000;
window.onload = function() {
 setTimeout(function() 
{ 
    document.getElementById("msg-flash").style.display = "none"; 
},3000);
};

//// Category Delete Script
//function deleteCategory(id)
//{
//  if(confirm('Do you want to DELETE this record ?'))
//  {
//    const xhr = new XMLHttpRequest();
//    xhr.onload = function()
//    {
//      if(this.response==id)
//      {
//        document.getElementById('category_tr_'+this.response).style.display="none";
//        return true;
//      }
//      alert("Opps!!! Sorry there is some problem.");
//    };
//    xhr.open("POST","http://127.0.0.1/projects/personal/myGrocery/category/delete");
//    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
//    xhr.send("id="+id+"");
//  }
//  else
//  {
//    return false;
//  }
//}


