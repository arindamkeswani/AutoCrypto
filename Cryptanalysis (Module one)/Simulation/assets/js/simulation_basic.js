A  = new Array (35);
			   Chars0 = "................................"; // 0-31
			   Chars1 = ' !"#$%&.()*.,-./0123456789:;<=>?'; //32-63
			   Chars2 = "@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_"; //64-95
			   Chars3 = "..abcdefghijklmnopqrstuvwxyz{|}~."; //96-127
			   Chars4 = "................................"; //128 - 159
			   Chars5 = "��������������������������������"; //160 - 191
			   Chars6 = "��������������������������������"; //192 - 223
			   Chars7 = "��������������������������������"; //224 - 255
			   all_Chars = Chars0+Chars1+Chars2+Chars3+Chars4+Chars5+Chars6+Chars7;
		   
		   function clear() {
			   document.gen_form.public_key.value ="";
			   document.gen_form.private_key.value= "";
			   document.myform.input.value="";
			   document.myform.encrypt_key.value = "";
			   document.myform.crypted.value="";
		   }
		   
		   function generate() {
			   today = new Date();
			   key1 = today.getTime()%256;
			   document.gen_form.public_key.value = key1;
			   document.gen_form.private_key.value= 256 - key1;
		   }
		   
				   
		   function encrypt() {
			
			   len = document.myform.input.value.length;
			   message = document.myform.input.value;
			   key = document.myform.encrypt_key.value;
		   
			   document.myform.crypted.value="";
			   for (n=0;n<len;n++) {
				A[n] =  message.charCodeAt(n);
					for (j=0;j<key;j++){
				   A[n] ++; 
					}
					//document.myform.crypted.value += " ";
				document.myform.crypted.value += A[n];
				   }
		   }
		   
		   function decrypt() {
			   
		   
			   key = document.decrypt_form.decrypt_key.value - 256;
			   len = document.myform.input.value.length;
			   document.decrypt_form.decrypted.value="";
				   for (i=0;i<len;i++) {
				   decrypt_value = (A[i]+key)%256;
				   document.decrypt_form.decrypted.value += all_Chars.charAt(decrypt_value);
			   }
		   }