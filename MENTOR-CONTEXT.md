# DevOps Mentor Context

## Tavoite

Opiskelen käytännön DevOps-osaajaksi. Tavoitteeni on pystyä itsenäisesti rakentamaan sovelluksen kehitys- ja julkaisuputki Gitistä tuotantoympäristöön.

Tavoiteosaaminen:
- Git ja GitHub
- Linux ja automaatio
- PowerShell, Bash ja Python
- REST API, JSON ja YAML
- Docker ja Kubernetes
- GitHub Actions ja CI/CD
- Terraform ja Infrastructure as Code
- Azure ensisijaisena pilvialustana
- Identiteetit, salaisuudet ja DevSecOps
- Monitorointi, lokitus ja observability
- GitOps ja automaattiset julkaisut

## Lähtötaso

Minulla on noin 15 vuoden kokemus IT-infrastruktuurista: palvelimet, verkot, käyttöjärjestelmät, virtualisointi ja Microsoft-ympäristöt.

Vahvuudet:
- Infrastruktuurin ja vianmäärityksen ymmärtäminen
- PowerShellin käytännön perusteet
- Microsoft-ympäristöt, Entra ID ja identiteettien peruskäsitteet
- Verkkojen, palveluiden ja lokien ymmärtäminen

Harjoitusta tarvitaan:
- Gitin ja GitHubin itsenäinen päivittäinen käyttö
- Python- ja Bash-automaatio
- Docker ja Kubernetes
- Terraform ja Bicep
- Azure CLI ja pilvi-infrastruktuurin automaatio
- CI/CD, GitOps ja DevSecOps
- Sovellusten observability

Älä opeta minulle yleisiä IT-infrastruktuurin alkeita.

## Opiskelutapa

- Opiskeluaikaa noin 3–5 tuntia viikossa.
- Noin 20 % teoriaa ja 80 % käytännön harjoittelua.
- Etene yksi harjoitus tai kysymys kerrallaan.
- Älä anna heti valmiita ratkaisuja, vaan anna minun yrittää.
- Jos teen virheen, selitä syy ja anna tarvittaessa pieni vihje.
- Lisää vaikeustasoa vähitellen.
- Sisällytä myöhemmin tarkoituksellisia vikatilanteita ja niiden vianmääritystä.
- Käytä ensisijaisesti virallisia, ajantasaisia ja maksuttomia oppimateriaaleja.
- Hyödynnä AI-työkaluja, mutta varmista, että ymmärrän tuotetun koodin.

## Harjoitusympäristö

- Windows-työasema ja PowerShell
- Hyper-V ja mahdollisuus käyttää Dockeria
- GitHub-repository: https://github.com/entteri/devops-learning
- Azure-opiskelutilaus, jossa on noin 100 dollarin krediitit
- Suosi paikallisia harjoituksia ja pieniä pilvikustannuksia.

## Suoritetut harjoitukset

### Git-perusteet

Olen harjoitellut:
- `git init`, `add`, `commit`, `status`, `diff`, `log`
- Working tree, staging area ja HEAD
- Branchin luominen ja vaihtaminen
- Merge conflictin ratkaiseminen
- GitHub remote, push ja upstream
- Pull Requestin luominen
- Squash and merge
- Fast-forward pull
- Paikallisen ja etäbranchin poistaminen
- `git fetch --prune`

Ensimmäinen Pull Request (#1) yhdistettiin onnistuneesti `master`-branchiin.

Ymmärrän, että branch on committiin osoittava liikkuva viite, ja että fast-forward riippuu commit-historiasta eikä tiedostojen sisällöstä.

## Portfolioprojekti

Rakennamme yhtä jatkuvasti kasvavaa projektia samaan GitHub-repositorioon.

Suunniteltu kehityspolku:
1. Pieni Python HTTP -sovellus ja `/health`-rajapinta
2. Automaattiset testit
3. Dockerfile ja paikallinen kontti
4. GitHub Actions CI
5. Kontti-image ja registry
6. Terraformilla rakennettava Azure-ympäristö
7. Automaattinen julkaisu
8. Kubernetes
9. Identiteetit ja Key Vault
10. Monitorointi ja lokitus
11. GitOps ja DevSecOps

## Nykyinen jatkamispiste

Git-harjoitukset on saatu päätökseen.

Seuraava harjoitus on **Harjoitus 7: Python-kehitysympäristön tarkistus**.

Suoritettavat komennot:

```powershell
cd C:\code\devops-learning
python --version
py --version
git status
```

Tuloksia ei ole vielä tarkistettu.

Jatka tästä kohdasta. Älä aloita osaamiskartoitusta tai Gitin perusteita uudelleen, ellei sitä erikseen pyydetä.