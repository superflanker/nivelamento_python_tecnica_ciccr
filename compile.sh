
cd apresentações/modulo_01/
pdflatex -synctex=1 -interaction=nonstopmode  --shell-escape "modulo_01".tex
cp modulo_01.pdf ../../nivelamento/apresentacao_modulo_01.pdf

cd ../../apostilas/modulo_01
pdflatex -synctex=1 -interaction=nonstopmode  --shell-escape "modulo_01".tex
cp modulo_01.pdf ../../nivelamento/apostilas/apostila_modulo_01.pdf
