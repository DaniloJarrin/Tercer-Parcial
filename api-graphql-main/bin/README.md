# api-graphql
La api está creada con SpringBoot, PostgreSQL.

## Probar la api
Ingresar a la dirección http://localhost:8080/graphiql
el puerto varía de acuerdo a su configuración

### Query
*Listar solo productos*

```
query{
  listarProductos{
    id,nombre,precio
	}
}
```

*Listar productos y categorias*
```
query{
  listarProductos{
    id,nombre,precio,categoria{
      name
    }
	}
}
```

### Mutation

*Actualizar un producto*
```
mutation{
  actualizarProducto(id:1,productoRequest:{
    nombre: "prueba de ingreso 22222",
    precio:200,
    stock:20,
    categoriaId:2
  }){
    	id, nombre
	}
}
```

*Guardar un producto*
```
mutation{
  guardarProducto(productoRequest:{
    nombre: "prueba de ingreso 2",
    precio:200,
    stock:20,
    categoriaId:2
  }){
    	id, nombre
	}
}
```