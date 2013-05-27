// JavaScript Document



$(document).ready(function() {
 var watermark = 'PASTE THE FASTA SEQUENCES HERE';
 $('#inputTextboxId').blur(function(){
  if ($(this).val().length == 0)
    $(this).val(watermark).addClass('watermark');
 }).focus(function(){
  if ($(this).val() == watermark)
    $(this).val('').removeClass('watermark');
 }).val(watermark).addClass('watermark');
});




//close button on sequence element div

$(".sqc_element").click(function(){
	
	
	
	$(this).attr("type","to_delete");
	
	
					});


$(".close").click(function(event) {
  event.preventDefault();
  $('div[type="to_delete"]').remove();
  
});



// When enter in inputTextboxId
$("#inputTextboxId").click(function(){
	$("#inputTextboxId").attr("text-align","left");
});


//to erase element (it closes the closest div) ** can be deleted if the close function is needed just for and specific element. (the function  above can b used)

/*$(".close").click(function(event) {
  event.preventDefault();
  $(this).closest('div').remove();
});

*/




var EditID="";



$(".new_sqc_element").click(function(){
									 
					var EditID="#"+$(this).attr("id");
					$("#edit_accept_btn").attr("type",EditID);
					
									 });


$("#edit_accept_btn").click(function(){
				
				var EditID=$("#edit_accept_btn").attr("type");
				var UserDataNumber=EditID.substr(-1);
				$(EditID).html('<div class="new_element_insert"><p>User&lsquo;s data</p></div>');
				
				
					
										 					
								
									 });







