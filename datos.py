import json

class Data_file:

    data_clientes = []
    data_pelicula = []

    def __init__(self):
        pass

    def data_readCliente(self):
        with open("data/clientes.json", "r") as file:
            data = json.load(file)
            for row in data['results']:
                self.data_clientes.append(row)

    def data_readPelicula(self):
        with open("data/pelicula.json", "r") as file:
            data = json.load(file)
            for row in data['results']:
                self.data_pelicula.append(row)


    def data_campoCliente(self,campocliente):
        list_cliente = []
        for row in self.data_clientes:
            campo = row[campocliente]
            if campo not in list_cliente:
                list_cliente.append(campo)
        return list_cliente

    def data_campoPelicula(self,campopelicula):
        list_pelicula = []
        for row in self.data_pelicula:
            campo = row[campopelicula]
            if campo not in list_pelicula:
                list_pelicula.append(campo)
        return list_pelicula


    def data_getClientes(self):
        return self.data_clientes

    def data_getPelis(self):
        return self.data_pelicula
