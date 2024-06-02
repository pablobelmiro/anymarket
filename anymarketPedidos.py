import json
import httpx
from datetime import datetime, timedelta, timezone

class tests:
    @staticmethod
    def test():
        return 'ok'

class errorAnymarket:
    msg = None
    statuscode = None
    def __init__(self, msg, statuscode):
        self.msg = msg
        self.statuscode = statuscode
        
    @staticmethod
    def throwError(msg, statuscode):
        if msg is not None and statuscode is not None:
            return f'Status code: {statuscode} \n message: {msg}'

class Pedido:
    token = None
    listOrders = {
            'orders': []
        }
    
    def __init__(self, token) -> None:
        self.token = token
        
    def _trataRetorno(self, params, response, listOrders):
        if response.status_code == 200: 
            data = {}
            responsedict = json.loads(response.text)
            print(f"totalPages: {responsedict['page']['totalPages']}")
            totalPaginas = responsedict['page']['totalPages']
            content = responsedict.get('content', None)
            if content is not None:
                data = {
                    'createdAfter': f'{params["createdAfter"]}',
                    'createdBefore': f'{params["createdBefore"]}',
                    'offset': f'{params["offset"]}',
                    'content': content
                }
                listOrders['orders'].append(data)
                return totalPaginas
            else:
                return None
        else:
            errorMsg = errorAnymarket.throwError(response.text, response.status_code)    
            print(errorMsg)

    def _requisicao(self, params, listOrders):
        print('================================')
        print(f'params: {params}')
        endpoint = 'http://api.anymarket.com.br/v2/orders'
        response = httpx.get(endpoint, headers={f'gumgaToken': token}, params=params, timeout=None)
        print(f'response: {response}')
        # print(f'response.text: {response.text}')
        
        totalPaginas = self._trataRetorno(params, response, listOrders)
        
        if totalPaginas is not None:
            return totalPaginas
        else:
            return
    
    @staticmethod
    def getPedidos(token, createdAfter=None, createdBefore=None, marketplaceId=None, offset=0, marketplace=None, status=None):
        pedido_instance = Pedido(token)
        params = {}
        
        params['Content-type'] = 'application/json'
        params['limit'] = '100'
        params['offset'] = f'{offset}'
        
        # Verificando componentes do params
        if marketplaceId is not None:
            params['marketplaceId'] = marketplaceId
            
        if marketplace is not None:
            params['marketplace'] = marketplace
            
        if status is not None:
            params['status'] = status
        
        # Verificando data inicial
        dataAtual = datetime.now().replace(hour=0, minute=0, second=0)
        fusoHorario = timezone(timedelta(hours=-23, minutes=-59))
        if createdAfter is not None:
            createdAfter = datetime.strptime(createdAfter, '%Y/%m/%d')
        else: 
            createdAfter = datetime.now()
            
        if createdBefore is not None:
            createdBefore = datetime.strptime(createdBefore, '%Y/%m/%d')
        else: 
            createdBefore = dataAtual - timedelta(days=7)
        
        # Iniciando dentro do loop de 7 dias
        for i in range(1, 7):
            createdAfter = dataAtual - timedelta(i)
            createdBefore = dataAtual - timedelta(i - 1)
            fusoHorario = timezone(timedelta(hours=-23, minutes=-59))

            # Formatar as datas conforme o padrão desejado
            createdAfterFormatted = createdAfter.replace(tzinfo=fusoHorario).strftime('%Y-%m-%dT00:00:00')
            createdBeforeFormatted = createdBefore.replace(tzinfo=fusoHorario).strftime('%Y-%m-%dT23:59:59')
        
            params['createdAfter'] = createdAfterFormatted
            params['createdBefore'] = createdBeforeFormatted
            
            
            totalPaginas = pedido_instance._requisicao(params, pedido_instance.listOrders)
            print(f'total paginas: {totalPaginas}')
            
            if totalPaginas > 1:
                # Verificando se possui mais páginas
                for _ in range(totalPaginas):
                    print(f'offset atual: {offset}')
                    offset += 100
                    params['offset'] = f'offset'
                    pedido_instance._requisicao(params, pedido_instance.listOrders)
        
        return pedido_instance.listOrders
