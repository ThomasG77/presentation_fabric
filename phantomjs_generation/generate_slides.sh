phantomjs phantomjs-revealjs-slide-capture.js http://localhost:8000/index.html
convert slide-* -resize 1860x2630 -units PixelsPerInch -density 150x150 -type TrueColor +antialias fabric_un_outil_pour_deployer_ses_projets_thomas_gratier.pdf
rm slide-*
