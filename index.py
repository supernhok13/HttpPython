from HttpSmartApiService import HttpSmartApiService
import pprint

qr = {"qrcode": 'data:image/png;base64,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'}
result = HttpSmartApiService.postApi("api/qrcode/authen",qr)

pprint.pprint(result)