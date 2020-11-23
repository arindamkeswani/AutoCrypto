function xorConvert (text, key) {
    var kL = key.length;

    return Array.prototype
        .slice.call(text)
        .map(function (c, index) {
            return String.fromCharCode(c.charCodeAt(0) ^ key[index % kL].charCodeAt(0));
        }).join('');
}

function xor_generate1(){
    var message = document.xor_form1.msg.value;
    document.xor_form1.msg.value = message;
    var key = document.xor_form1.secret_key.value;
    document.xor_form1.secret_key.value = key;
    document.xor_form1.enc.value = xorConvert(message,key);
}

function xor_generate2(){
    var secret = document.xor_form2.sec.value;
    document.xor_form2.sec.value = secret;
    document.xor_form2.dec.value = xorConvert(document.xor_form1.enc.value,secret);
}

