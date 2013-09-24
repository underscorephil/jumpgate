import json
import falcon

from core import api


class SLComputeV2Limits(object):
    def on_get(self, req, resp, tenant_id):
        client = api.config['sl_client']

        account = client['Account'].getObject(
            mask='mask[hourlyVirtualGuestCount]')

        # TODO - This shouldn't be hardcoded
        limits = {
            'absolute': {
                'maxImageMeta': 128,
                'maxPersonality': 5,
                'maxPersonalitySize': 10240,
                'maxSecurityGroupRules': 999999,
                'maxSecurityGroups': 999999,
                'maxServerMeta': 999999,
                'maxTotalCores': 999999,
                'maxTotalFloatingIps': 999999,
                'maxTotalInstances': 999999,
                'maxTotalKeypairs': 999999,
                'maxTotalRAMSize': 999999999,
                'totalInstancesUsed': account['hourlyVirtualGuestCount'],
                'totalCoresUsed': 0,
                'totalRAMUsed': 0,
            }
        }

        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'limits': limits})