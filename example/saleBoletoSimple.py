#-*- coding: utf-8 -*-s

import sys
sys.path.insert(0, "./")

from cieloApi3 import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant(settings.MERCHANT_ID, settings.MERCHANT_KEY)

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('333')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Comprador Teste')

# Crie uma instância de Payment informando o valor do pagamento
sale.payment = Payment(15700)
sale.payment.type = PAYMENTTYPE_BOLETO

sale.payment.provider = PROVIDER_BRADESCO

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print ('----------------------response_create_sale----------------------')
print (json.dumps(response_create_sale, indent=2))
print ('----------------------response_create_sale----------------------')

# Com a venda criada na Cielo, já temos o ID do pagamento, TID e demais
# dados retornados pela Cielo
payment_id = sale.payment.payment_id

# Com o ID do pagamento, podemos fazer uma consulta do pagamento
response_get_sale = cielo_ecommerce.get_sale(payment_id)
print ('----------------------response_get_sale----------------------')
print (json.dumps(response_get_sale, indent=2))
print ('----------------------response_get_sale----------------------')

print ('\r\nLink Boleto:', sale.payment.url, '\r\n')
