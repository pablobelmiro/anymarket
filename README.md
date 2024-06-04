#API Anymarket


#Installation
To install this library, use pip:

`pip install Anymarket`

#How to import
Example:
`from anymarket import *|<modules>`

#Modules
    * Pedido

###github project
https://github.com/pablobelmiro/anymarket

#Usage
Below is a description of the static methods provided by the library. These methods allow for easy interaction with the Anymarket API without the need to instantiate the classes.
tests Class: 
##`tests.test()`

#Pedido Class
##`getPedidos(token, createdAfter=None, createdBefore=None, marketplaceId=None, offset=0, marketplace=None, status=None, days=7)`
##Example:
`from anymarket import Pedido
token = "your-token"
dictOrders = Pedido.getPedidos(token)`


Retrieves a list of orders from Anymarket within the specified date range and other optional parameters.

    * token: Your Anymarket API token.
    * createdAfter: Start date for retrieving orders (format: 'YYYY/MM/DD').
    * createdBefore: End date for retrieving orders (format: 'YYYY/MM/DD').
    * marketplaceId: ID of the marketplace.
    * offset: Offset for pagination.
    * marketplace: Name of the marketplace.
    * status: Status of the orders.
    * days: Number of days to retrieve orders for.

##`getPedido(token, idOrder)`
##Example:
`from anymarket import Pedido
token = "your-token"
dictOrder = Pedido.getPedido(token, idOrder=1234)`

Retrieves a specific order by its ID.

    * token: Your Anymarket API token.
    * idOrder: ID of the order to retrieve.

##`getXmlNfe(token, idOrder, type='sale')`
##Example:
`from anymarket import Pedido
token = "your-token"
dictOrder = Pedido.getXmlNfe(token, idOrder=1234, type='sale')`
#param type is OPTIONAL

Retrieves the XML of a specific invoice (NFE) for an order.

    * token: Your Anymarket API token.
    * idOrder: ID of the order.
    * type: OPTIONAL Type of the NFE (default is 'sale').

##`postOrder(token, payload=None)`
##Example:
`from anymarket import Pedido
token = "your-token"
payload = {}
dictOrder = Pedido.postOrder(token, payload=payload)`
###Payload documentation: https://developers.anymarket.com.br/api/v2/8cfa11486184a-orders


Creates a new order with the given payload.

    * token: Your Anymarket API token.
    * payload: Dictionary containing the order data.

##`putOrderPago(token, idOrder=0)`
##Example:
`from anymarket import Pedido
token = "your-token"
dictOrder = Pedido.putOrderPago(token, idOrder=1234)`

Marks an order as paid.

    * token: Your Anymarket API token.
    * idOrder: ID of the order to mark as paid.

##`Pedido.putOrderFaturado(token, idOrder=0, payload=None)`
##Example:
`from anymarket import Pedido
token = "your-token"
payload = {}
dictOrder = Pedido.putOrderFaturado(token, idOrder=1234, payload=payload)`
###Payload documentation: https://developers.anymarket.com.br/api/v2/40f4fe2a8d1a6-orders-id-faturado

Marks an order as invoiced.

    * token: Your Anymarket API token.
    * idOrder: ID of the order to mark as invoiced.
    * payload: Dictionary containing the invoicing data.

##`putOrderEmTransito(token, idOrder=0, payload=None)`
##Example:
`from anymarket import Pedido
token = "your-token"
payload = {}
dictOrder = Pedido.putOrderEmTransito(token, idOrder=1234, payload=payload)`
###Payload documentation: https://developers.anymarket.com.br/api/v2/79a198e2f0b5b-orders-id-enviado-em-transito

Marks an order as in transit.

    * token: Your Anymarket API token.
    * idOrder: ID of the order to mark as in transit.
    * payload: Dictionary containing the transit data.

##`putOrderConcluido(token, idOrder=0, payload=None)`
##Example:
`from anymarket import Pedido
token = "your-token"
payload = {}
dictOrder = Pedido.putOrderConcluido(token, idOrder=1234, payload=payload)`
###Payload documentation: https://developers.anymarket.com.br/api/v2/e8078db411b0d-orders-id-concluido


Marks an order as completed.

    * token: Your Anymarket API token.
    * idOrder: ID of the order to mark as completed.
    * payload: Dictionary containing the completion data.

##`putOrderCancelado(token, idOrder=0, cancelDescription=None)`
##Example:
`from anymarket import Pedido
token = "your-token"
description = 'canceled'
dictOrder = Pedido.putOrderCancelado(token, idOrder=1234, cancelDescription=description)`
###Payload documentation: https://developers.anymarket.com.br/api/v2/b34a24800a053-orders-id-cancelado

Cancels an order with the given description.

    * token: Your Anymarket API token.
    * idOrder: ID of the order to cancel.
    * cancelDescription: Description for the cancellation.

##`ordersPutEnviaXml(token, idOrder=0, xml=None)`
##Example:
`from anymarket import Pedido
token = "your-token"
xml = ''
dictOrder = Pedido.ordersPutEnviaXml(token, idOrder=1234, xml=xml)`
###Payload documentation: https://developers.anymarket.com.br/api/v2/54b16092d1776-orders-id-nfe

Sends the XML of an NFE for an order.

    * token: Your Anymarket API token.
    * idOrder: ID of the order.
    * xml: XML data to send.

##`ordersPostfiscalDocument(token, idOrder=0, fiscalDocument=None)`
##Example:
`from anymarket import Pedido
token = "your-token"
file = ''
dictOrder = Pedido.ordersPostfiscalDocument(token, idOrder=1234, fiscalDocument=file)`
###boundary=---011000010111000001101001
###Payload documentation: https://developers.anymarket.com.br/api/v2/q4xx466onjupg-orders-id-fiscal-document

Posts a fiscal document for an order.

    * token: Your Anymarket API token.
    * idOrder: ID of the order.
    * fiscalDocument: Fiscal document data to send.

#License
This project is licensed under the MIT License. See the LICENSE file for details.

#Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.

Contact
For any issues or inquiries, please contact [dev.pablobelmiro@gmail.com].
