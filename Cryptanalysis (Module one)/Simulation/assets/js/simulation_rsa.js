

function get_prime()
{
    var primes;
    primes =[ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,

    73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,  137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,

    241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397 ];

    return (primes[Math.floor(Math.random() * primes.length)]);
}

function rsa1_generate() {
    document.rsa_form1.p_primenumber.value = get_prime();
    document.rsa_form1.q_primenumber.value = get_prime();
}

function gcd(a,h){
    var temp;
    while(1){
        temp = a % h;
        
        if(temp == 0){
            return h;
        }
        a = h;
        h = temp;
    }
}



function rsa2_generate() {
    document.rsa_form2.n_p_multiply_q.value = document.rsa_form1.p_primenumber.value * document.rsa_form1.q_primenumber.value;
    document.rsa_form2.phi.value = (document.rsa_form1.p_primenumber.value - 1) * (document.rsa_form1.q_primenumber.value - 1 );
    var e = 2;
    while (e < document.rsa_form2.phi.value) 
    { 
        if (gcd(e, document.rsa_form2.phi.value)==1) 
            break; 
        else
            e++; 
    } 
    document.rsa_form2.e_random.value = e;
}



function rsa3_generate() {
    var d1 = 1 /  document.rsa_form2.e_random.value;
    var d = d1 % document.rsa_form2.phi.value
    document.rsa_form3.d_mod.value = d;
    document.rsa_form3.publickey.value = `(${document.rsa_form2.n_p_multiply_q.value},${document.rsa_form2.e_random.value})`;
    document.rsa_form3.privatekey.value = `(${document.rsa_form2.n_p_multiply_q.value},${document.rsa_form3.d_mod.value})`;
}

function rsa4_generate() {
    var message = document.rsa_form4.message.value;
    console.log("message ",message)
    var c = Math.pow(message,document.rsa_form2.e_random.value);
    var m = Math.pow(c,document.rsa_form3.d_mod.value);
    c = c % document.rsa_form2.n_p_multiply_q.value;
    m = m % document.rsa_form2.n_p_multiply_q.value;
    document.rsa_form4.encrypt.value = Math.round(c);
    document.rsa_form4.decrypt.value = Math.round(m);
    
}
