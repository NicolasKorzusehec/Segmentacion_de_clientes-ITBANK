# Segmentacion_de_clientes
Esta es una aplicación propuesta por la escuela de innovación del ITBA en el SPRINT 5 de su curso de desarrollador fullstack.
ITBANK tiene distintos tipos de clientes y distintos tipos de cuentas que le puede dar a cada uno. Adicionalmente los clientes pueden tener distintos tipos de tarjetas de crédito y operaciones permitidas según su perfil asociado.

## Table of contents

  - [Objetivo](#objetivo)
    - [Detalles del desafio](#detalles-del-desafio)
      - Tipos de Clientes
      - Tipos de Cuentas
  - [Requerimientos especificos](#requerimientos-especificos)
  - [Aclaraciones y acotaciones](#aclaraciones-y-acotaciones)
  - [Links](#links)
  - [Autores](#autores)

## Objetivo


## Detalles del desafio
### Tipos de clientes
- `Classic`
  - Tiene solamente `una` tarjeta de débito que se crea junto con el cliente.
  - Solo tiene `una caja ahorro` en pesos creada cuando se dio de alta el cliente.
  - Como `no tiene` cuenta en dólares, no puede comprar y vender dólares.
  - Solo se le permite retirar hasta un máximo de `$10.000 diarios` por cajero.
  - `No tienen` acceso a tarjetas de crédito, ni chequeras.
  - La comisión por transferencias hechas es de `1%`.
  - No puede recibir transferencias `mayores a $150.000` sin previo aviso.

- `Gold`
  - Tiene `una` tarjeta de débito que se crea con el cliente.
  - Tiene `una cuenta corriente` con un descubierto de `$10.000`. Hay que tener presente que como tiene cuenta corriente el saldo en la cuenta podría ser negativo y `hasta -$10.000` si tiene cupo diario para la operación que se quiera realizar.
  - Tiene `una` caja de ahorro en dólares, por lo que puede comprar dólares.
  - Puede tener solo `una` tarjeta de crédito.
  - Las extracciones de efectivo tienen un máximo de `$20.000 por día`.
  - `Pueden` tener una chequera.
  - La comisión por transferencias hechas es de `0,5%`.
  - No puede recibir transferencias `mayores a $500.000` sin previo aviso.

- `Black`
  - Los clientes Black tienen una `caja de ahorro en pesos`, `cuenta corriente en pesos`, y una `caja de ahorro en dólares`.
  - Pueden tener un descubierto en su cuenta corriente de `hasta $10.000`.
  - Pueden tener hasta `5` tarjetas de crédito.
  - Pueden extraer `hasta $100.000 por día.`
  - Pueden tener hasta `dos` chequeras.
  - No se aplican comisiones a las transferencias.
  - Pueden recibir transferencias por cualquier monto sin previa autorización.

### Tipos de cuentas
  - Caja de ahorro en pesos
  - Caja de ahorro en dólares
  - Cuenta Corriente


## Requerimientos especificos


## Aclaraciones y acotaciones


## Links
- Solution URL: (https://github.com/NicolasKorzusehec/Segmentacion_de_clientes)
- Live Site URL: (https://nicolaskorzusehec.github.io/Segmentacion_de_clientes/)

## Autores
#### Korzusehec, Nicolás
- GitHub - [@NicolasKorzusehec](https://github.com/NicolasKorzusehec)
- LinkedIn - [Nicolás Korzusehec](https://www.linkedin.com/in/nicol%C3%A1s-korzusehec/)

#### Upstein, Elias Román
- GitHub - [@EliasUpstein](https://github.com/EliasUpstein)
- LinkedIn - [/]()

#### Ledesma, Juan Ignacio
- GitHub - [@juanignacio97](https://github.com/juanignacio97)
- LinkedIn - [Juan Ignacio Ledesma](https://www.linkedin.com/in/juanignacioledesma/)

#### Molinas, Nicolás 
- GitHub - [@NicolasGabM](https://github.com/NicolasGabM)
- LinkedIn - [Nicolas Gabriel Molinas](https://www.linkedin.com/in/nicolas-gabriel-molinas-20802a216/)

#### Magliotto, Ena Sofía 
- GitHub - [@SofiaEna](https://github.com/SofiaEna)
- LinkedIn - [/]()
