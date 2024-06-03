#API Anymarket


#Installation
To install this library, use pip:

`pip install Anymarket`

#How to import
`from Anymarket import *|<modules>`
##Modules
    * Pedido

###github project
https://github.com/pablobelmiro/anymarket

#Usage
Below is a description of the static methods provided by the library. These methods allow for easy interaction with the Anymarket API without the need to instantiate the classes.
tests Class: 
##`tests.test()`

#Pedido Class
##`getPedidos(token, createdAfter=None, createdBefore=None, marketplaceId=None, offset=0, marketplace=None, status=None, days=7)`
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
Retrieves a specific order by its ID.

    * token: Your Anymarket API token.
    * idOrder: ID of the order to retrieve.

##`getXmlNfe(token, idOrder, type='sale')`
Retrieves the XML of a specific invoice (NFE) for an order.

    * token: Your Anymarket API token.
    * idOrder: ID of the order.
    * type: Type of the NFE (default is 'sale').

##`postOrder(token, payload=None)`
Creates a new order with the given payload.

    * token: Your Anymarket API token.
    * payload: Dictionary containing the order data.

##`putOrderPago(token, idOrder=0)`
Marks an order as paid.

    * token: Your Anymarket API token.
    * idOrder: ID of the order to mark as paid.

##`Pedido.putOrderFaturado(token, idOrder=0, payload=None)`
Marks an order as invoiced.

    * token: Your Anymarket API token.
    * idOrder: ID of the order to mark as invoiced.
    * payload: Dictionary containing the invoicing data.

##`putOrderEmTransito(token, idOrder=0, payload=None)`
Marks an order as in transit.

    * token: Your Anymarket API token.
    * idOrder: ID of the order to mark as in transit.
    * payload: Dictionary containing the transit data.

##`putOrderConcluido(token, idOrder=0, payload=None)`
Marks an order as completed.

    * token: Your Anymarket API token.
    * idOrder: ID of the order to mark as completed.
    * payload: Dictionary containing the completion data.

##`putOrderCancelado(token, idOrder=0, cancelDescription=None)`
Cancels an order with the given description.

    * token: Your Anymarket API token.
    * idOrder: ID of the order to cancel.
    * cancelDescription: Description for the cancellation.

##`ordersPutEnviaXml(token, idOrder=0, xml=None)`
Sends the XML of an NFE for an order.

    * token: Your Anymarket API token.
    * idOrder: ID of the order.
    * xml: XML data to send.

##`ordersPostfiscalDocument(token, idOrder=0, fiscalDocument=None)`
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
