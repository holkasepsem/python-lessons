
# Poznámky

## Základní příkazy v příkazové řádce

cd (change directory)

    cd
    cd {tilda} 
    cd {tilda}/{dir_name}

ls (list)

    ls      vypíše seznam souborů a složek v aktuálním adresáři
    ls -l   podrobný výpis
    ls -a   ukaž i skryté soubory a adresáře

pwd (print working directory)

    pwd    ukáže kde právě jsem

brew	

rm (remove)	smazání souboru/adresáře

whoami 

    whoami    ukáže kdo jsem, tedy aktuálně přihlášený uživatel

sort 

    sort    řadí výstup 

Načíst soubor s nastavením
        
        source tilda/.bashrc

mkdir (make direcotry)
    
    mkdir {dir_name}	vytvoří nový adresář


## Instalace nástroje `git` 

    sudo apt-get install git 
    brew install git

### Základní příkazy programu `git`

    git clone {url}	naklonování repozitáře

    git init		vytvoří nový repozitář

	git commit -m  "Zpráva"

	git commit		dokončení sloučením

	git push / git push origin master	uložení repozitáře

	git pull / git pull origin master	aktualizace lokální kopie

	git fetch		

	git status		vypíše seznam změn


## PEP8 (úprava dokumentů v Pythonu)

