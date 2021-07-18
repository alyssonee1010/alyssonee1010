//SIGN IN AND SIGN UP

const signinform = document.getElementById("signinform") //HIDDEN FORMS
signinform.style.display="none"
const signupform = document.getElementById("signupform")
signupform.style.display="none"
const todoform = document.getElementById("todoform")
todoform.style.display="none"


const signup= document.getElementById("signup");   //BUTTOMS SIGN UP || SIGN IN
const signin= document.getElementById("signin");
const submit = document.getElementById("submitbuttom");  //CHECK || SUBMIT
const check =  document.getElementById("check");


let fname = document.getElementById("firstname");   // FORM ELEMENTS SIGNING UP
let lname = document.getElementById("lastname");
let email = document.getElementById("email");
let password = document.getElementById("password");

let checkname = document.getElementById('fname');  //FORM ELEMENTS SIGNING IN 
let checklname = document.getElementById('lname');
let checkemail = document.getElementById('mail');
let checkpassword = document.getElementById('pass');


signup.addEventListener("click", signupfunction);    // EVENT LISTENER CLICK
submit.addEventListener("click", submition);
signin.addEventListener("click", signinfunction);
check.addEventListener("click", checkfunction)


fname.addEventListener("keydown", blocksb);  //SPACE BAR BLOCK
lname.addEventListener("keydown", blocksb);
email.addEventListener("keydown", blocksb);
password.addEventListener("keydown", blocksb);

function signupfunction (e) {             //SIGN UP CLICK FUNCTION
	signupform.style.display="block";
	signup.style.display="none";
	signinform.style.display = "none"
	signin.style.display="block"
}
var data = [];
function submition (e) {                        //SUBMITION FUNCTION
	e.preventDefault()
	var letters = /^[A-Za-z]+$/;
	if((fname.value.match(letters)) && (lname.value.match(letters))){
		if ((fname.value) && (lname.value) && (email.value) && (password.value)){
			if(document.getElementById("acceptterms").checked === true){
        			signinform.style.display="none";
				signupform.style.display="none";
				return
			}}}
	else { 
		alert("you should only characters in name and last name")
		alert("Read our 'Terms of Use' to proceed please.");
        		return false;
	}}

 let parsedData = JSON.parse(localStorage.getItem("Sign Up"));
        
       
localStorage.setItem("Sign Up",JSON.stringify(parsedData));

let signupInfo = {
        FirstName : document.getElementById("firstname").value,
        LastName: document.getElementById("lastname").value,
        Email: document.getElementById("email").value,
        Password: document.getElementById("password").value
    }
    
// Checking If there is an array already. If not - we create a new one, If exists, we just add new values to it.

let suInfo = !!localStorage.getItem('Sign Up') ? JSON.parse(localStorage.getItem('Sign Up')) : [];

suInfo.push(signupInfo);

//saving items in LOCAL STORAGE:

localStorage.setItem('Sign Up', JSON.stringify(suInfo));

console.log(localStorage)

      
function signinfunction(e) {                      //SIGN IN CLICK FUNCTION
	e.preventDefault()
	signinform.style.display="block";
	signin.style.display="none";
	signupform.style.display="none";
	signup.style.display= "block";
}

function checkfunction() {                   //CHECK SIGN IN FUNCTION
	if ((localStorage.getItem("Name") == checkname.value) && (localStorage.getItem("Last Name") == checklname.value) && (localStorage.getItem("E-Mail") == checkemail.value) &&(localStorage.getItem("Password") == checkpassword.value)){
		signup.style.display="none";
		signin.style.display="none";
		todoform.style.display="block";
		signupform.style.display="none";
		signinform.style.display="none";
	}
	else{
		alert("You putted the wrong Value")

	} return 
}

function blocksb(e) {                  //BLOCKING SPACE BAR TO SIGN UP
	if (e.key === " "){
		e.preventDefault();
	}
}

localStorage.setItem("Name", fname.value)            
localStorage.setItem("Last Name",lname.value);
localStorage.setItem("E-Mail",email.value);
localStorage.setItem("Password",password.value);

// TO DO LIST -------------------------------------------------------------------------------------------------------------------

const createtask = document.getElementById("createtask");
const edittask = document.getElementById("edittask");
const removetask = document.getElementById("removetask")


const taskelement = document.getElementById("elements")

createtask.addEventListener("click", creating);






function creating(e){
	let element = document.createElement("input");
	element.type = "text";
	taskelement.appendChild(element);
	checker()
}
function checker(){
	let i = 1;
	if (taskelement.childNodes[i]){
		i ++;
	   let element = document.createElement("input");
	   element.type = "checkbox";
	   taskelement.appendChild(element);}
	}