const rl = require('readline-sync');
const colors = require('colors');
const title = require('./modules/title.js');
const Sms = require('./modules/sms.js');

title('Hosgeldiniz');

banner() {
	cat <<- EOF
		${ORANGE}
		${ORANGE}▀ ▀ ▀ ▀. ▀
		${ORANGE}▀.    ▀.  ▀
		${ORANGE}▀.    ▀.  ▀
		${ORANGE}▀.    ▀.  ▀
		${ORANGE}▀.    ▀.  ▀
		${ORANGE}▀ ▀ ▀ ▀.  ▀
	            ${RED}Version : ${__version__}

		${GREEN}[${WHITE}-${GREEN}]${CYAN} Tool Created by htr-tech (tahmid.rayat)${WHITE}
	EOF
}

let telefon = rl.question('Telefon Numarasi +90:' .red);
if (telefon.length != 10) {
    console.log('10 hanelı'.red);
    process.exit(1);
}
title('Numara: ' + telefon);

let miktar = rl.question("Kac aet sms ıstıyor sunuz ".red);
if(isNaN(miktar)) return console.log('Lutfen Bir Rakam Giriniz'.red) && process.exit(1);
if (miktar.length == 0) {
    console.log('Miktar Giriniz'.red);
    process.exit(1);
}
title(`Telefon: ${telefon} - Miktar: ${miktar}`);

console.log('Calısıyor'.rainbow);

Sms(telefon, miktar);
