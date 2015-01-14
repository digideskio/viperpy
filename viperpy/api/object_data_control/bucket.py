# Standard lib imports
# None

# Third party imports
# None

# Project level imports
# None


class Bucket():

    def __init__(self, connection):
        """
        Initialize a new instance
        """
        self.conn = connection

    def get_buckets(self, namespace):
        """
        List of buckets associated with the namespace

        Required role(s):

        SYSTEM_ADMIN
        TENANT_ADMIN
        RESTRICTED_SYSTEM_ADMIN

        Example JSON result from the API:

        {
            "object_bucket": [
                {
                    "remote": "None",
                    "name": "bucket1",
                    "tags": [],
                    "global": "None",
                    "vdc": "None",
                    "inactive": "False",
                    "id": "namespace1.bucket1"
                },
                {
                    "remote": "None",
                    "name": "bucket2",
                    "tags": [],
                    "global": "None",
                    "vdc": "None",
                    "inactive": "False",
                    "id": "namespace1.bucket2"
                }
            ]
        }

        List of buckets associated with the namespace

        :param namespace: The namespace to query for buckets
        """
        return self.conn.get(url='object/bucket/{0}'.format(namespace))

    def get_bucket_retention(self, bucket_name):
        """
        Returns default retention period for bucket

        Example JSON result from the API:

        {
            "period": -2
        }

        :param bucket_name: The bucket name to fetch the retention period
        """
        return self.conn.get(
            url='object/bucket/{0}/retention'.format(bucket_name))

    def update_bucket_owner(self, namespace, new_owner, bucket_name):
        """
        Update Owner for a bucket

        Example JSON result from the API:

        There is no response body for this call

        :param namespace: The namespace
        :param new_owner: New Owner must be a valid user
        :param bucket_name: Name of the bucket
        """
        payload = {
            "namespace": namespace,
            "new_owner": new_owner
        }

        return self.conn.post(
            url='object/bucket/{0}/owner'.format(bucket_name),
            json_payload=payload)

    def update_bucket_retention(self, period, bucket_name):
        """
        Sets or updates default retention setting for bucket

        Example JSON result from the API:

        TODO: Add JSON sample

        :param period: Default retention period in seconds
        :param bucket_name: Name of the bucket
        """
        payload = {
            "period": period
        }

        return self.conn.put(
            url='object/bucket/{0}/retention'.format(bucket_name),
            json_payload=payload)

    def create_bucket(self, name, vpool, namespace, filesystem_enabled,
                      project=None, head_type=None):
        """
        Create a bucket

        Required role(s):

        This call has no restrictions

        Example JSON result from the API:

        {
            "name": "bobsbucket",
            "id": "namespace1.bobsbucket",
            "inactive": "false",
            "global": None,
            "remote": None,
            "vdc": None,
            "tags": []
        }

        :param name: Name of the bucket
        :param project: Project ID for the bucket
        :param vpool: vpool ID for the bucket
        :param filesystem_enabled: flag indicating whether file-system is
            enabled for this bucket
        :param head_type: HeadType indicates the object head type that is
            allowed to access the bucket. If the bucket has FS-Enabled,
            then the FS heads are implicitly allowed to access this bucket 
        :param namespace: namespace associated with the user/tenant that is
            allowed to access the bucket    
        """

        payload = {
            "name": name,
            "project": project,
            "vpool": vpool,
            "filesystem_enabled": filesystem_enabled,
            "head_type": head_type,
            "namespace": namespace
        }

        return self.conn.post(url='object/bucket',
                              json_payload=payload)

    def get_bucket_lock(self, bucket_name, namespace=None):
        """
        Get bucket lock status

        Required role(s):

        SYSTEM_ADMIN
        TENANT_ADMIN
        RESTRICTED_SYSTEM_ADMIN

        Example JSON result from the API:

        TODO: Add JSON sample

        :param bucket_name: Example: bobsbucket
        :param namespace: Example: namespace1 (optional)
        """

        if namespace:
            return self.conn.get(
                url='object/bucket/{0}/{1}/lock'.format(
                    bucket_name, namespace))
        else:
            return self.conn.get(
                url='object/bucket/{0}/lock'.format(bucket_name))

    def lock_bucket(self, bucket_name, is_locked='true', namespace=None):
        """
        Locks the Bucket.
        Once is_locked is set to true no operation
        can be performed on the bucket.

        Required role(s):

        SYSTEM_ADMIN
        TENANT_ADMIN
        RESTRICTED_SYSTEM_ADMIN

        Example JSON result from the API:

        TODO: Add JSON sample

        :param bucket_name: Example: bobsbucket
        :param lock: Example: 'true' or 'false'
        :param namespace: Example: namespace1 (optional)
        """

        payload = {}

        if namespace:
            payload = {
                "namespace": namespace
            }

        return self.conn.put(
            url='object/bucket/{0}/lock/{1}'.format(bucket_name, is_locked),
            json_payload=payload
        )
