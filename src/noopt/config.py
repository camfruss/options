class _Config:

    def __init__(self):
        self._params = {
            'use_cache': True,
            'verbose': False,
            'write_on_response': True
        }

    @property
    def use_cache(self):
        """
        All files in the 'cache' must start with a function name corresponding to 
        a function that uses said file. For example, def foo(): ... uses foo*.* 
        saved in /data
        """
        return self._params.get('use_cache')

    @property
    def verbose(self):
        return self._params.get('verbose')

    @property
    def write_on_response(self):
        return self._params.get('write_on_response')

    def configure(self, **kwargs):
        for k, v in kwargs.items():
            if self._params.get(k) is None:
                raise ValueError(f'Unsupported configuation option {k}={v}')
            self._params[k] = v

config = _Config()
__all__ = ['config']

