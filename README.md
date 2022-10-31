# FrakkComm kommunikáció

> **_Disclaimer:_** If you have to ask what this is, it's not for you. Trust me.

## v1.0 specifikáció

TCP alapú kommunikáció

Komponensek:

- Byte 1, Kezdő:
  - Blockmarker
  - Értéke mindig `0x55`
- Byte 2, Hossz:
  - Az adatcsomag hossza byteban kifejezve
- Byte 2, Címzett:
  - Milyen eszközt címez meg
  - `0xFF` mindenkit megcímez (?)
- Byte 3, Feladó:
  - Nincs használva itt, `0x00` egyelőre jó
- Byte 4, Üzenet ID:
  - Az üzenet azonosítója
  - `0xF4` működik ha ez nem fontos
- Byte 5, Parancs:
  - ???
  - `0x56` működik, többit nem tudjuk még
- Byte 6-8, Adat:
  - adat csomag amit küldeni kell
  - Lámpák esetén:
    - Byte 1: Lámpa ID
    - Byte 2: szín
      - 64 fehér esetén
      - 128 kék esetén,
      - 64+128 mindkettő szín esetén
    - Byte 3: Fényerő
- Byte 9, Checksum

> **Fontos**: Minden bytenál ha az érték 0x55, akkor meg kell duplázni.

## Package build

A Python kód lefordítása:

### Előfeltételek

- Python 3, pip
- `pip install build`
- `pip install wheel`
- `pip install pytest`

### Lefordítás

```sh
python3 -m build
```

A lefordított package pedig a `./dist` mappában van, a `*.whl` file ami általában kell.

Ha ezt a helyi verziót akarjuk felinstallálni akkor csak ennyit kell futattni: `pip install .\dist\frakkcomm-1.0.0-py3-none-any.whl`

Ehhez nem kell PyPI-ra publisholni, viszont a file-nak így lokálisan elérhetőnek kell lennie. Home Assistant-nál ez pl kicsit macerás, szóval PyPI-ra érdemes publisholni általában.

### PyPI publish és install

GitHub Actions-t használva automatikusan tudunk PyPI-ra publisholni.

Először növeld meg a verziószámot a `pyproject.toml` fájlban [Semver](https://semver.org/)-t használva (pl. `1.0.1`),

Utána push-olj a main branch-re, várd meg amíg minden teszt lefut rendesen. Ha minden lefutott, akkor csinálj egy új taget a main-ből a `vX.X.X` (pl. `v1.0.1`) formátumban:

```sh
git tag v1.0.1
git push --origin tags
```

Ez automatikusan buildel egy új package-et, és felrakja PyPi-ra: <https://pypi.org/project/frakkcomm/>

Ezután fel lehet installálni a `pip install frakkcomm` paranccsal bárhova.

### Tesztelés

Pytest-et használva könnyen lehet tesztelni a kódot.

```sh
python3 -m pytest tests
```
