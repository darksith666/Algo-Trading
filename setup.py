from setuptools import setup

setup(
    name='T.Bot',
    version='',
    packages=['app', 'util', 'env36.Lib.site-packages.idna', 'env36.Lib.site-packages.lxml',
              'env36.Lib.site-packages.lxml.html', 'env36.Lib.site-packages.lxml.includes',
              'env36.Lib.site-packages.lxml.isoschematron', 'env36.Lib.site-packages.pytz',
              'env36.Lib.site-packages.zope.interface', 'env36.Lib.site-packages.zope.interface.tests',
              'env36.Lib.site-packages.zope.interface.common', 'env36.Lib.site-packages.zope.interface.common.tests',
              'env36.Lib.site-packages.numpy', 'env36.Lib.site-packages.numpy.ma',
              'env36.Lib.site-packages.numpy.ma.tests', 'env36.Lib.site-packages.numpy.doc',
              'env36.Lib.site-packages.numpy.fft', 'env36.Lib.site-packages.numpy.fft.tests',
              'env36.Lib.site-packages.numpy.lib', 'env36.Lib.site-packages.numpy.lib.tests',
              'env36.Lib.site-packages.numpy.core', 'env36.Lib.site-packages.numpy.core.tests',
              'env36.Lib.site-packages.numpy.f2py', 'env36.Lib.site-packages.numpy.f2py.tests',
              'env36.Lib.site-packages.numpy.tests', 'env36.Lib.site-packages.numpy.compat',
              'env36.Lib.site-packages.numpy.compat.tests', 'env36.Lib.site-packages.numpy.linalg',
              'env36.Lib.site-packages.numpy.linalg.tests', 'env36.Lib.site-packages.numpy.random',
              'env36.Lib.site-packages.numpy.random.tests', 'env36.Lib.site-packages.numpy.testing',
              'env36.Lib.site-packages.numpy.testing.tests', 'env36.Lib.site-packages.numpy.testing._private',
              'env36.Lib.site-packages.numpy.distutils', 'env36.Lib.site-packages.numpy.distutils.tests',
              'env36.Lib.site-packages.numpy.distutils.command', 'env36.Lib.site-packages.numpy.distutils.fcompiler',
              'env36.Lib.site-packages.numpy.matrixlib', 'env36.Lib.site-packages.numpy.matrixlib.tests',
              'env36.Lib.site-packages.numpy.polynomial', 'env36.Lib.site-packages.numpy.polynomial.tests',
              'env36.Lib.site-packages.wrapt', 'env36.Lib.site-packages.pandas', 'env36.Lib.site-packages.pandas.io',
              'env36.Lib.site-packages.pandas.io.sas', 'env36.Lib.site-packages.pandas.io.json',
              'env36.Lib.site-packages.pandas.io.formats', 'env36.Lib.site-packages.pandas.io.msgpack',
              'env36.Lib.site-packages.pandas.io.clipboard', 'env36.Lib.site-packages.pandas.api',
              'env36.Lib.site-packages.pandas.api.types', 'env36.Lib.site-packages.pandas.api.extensions',
              'env36.Lib.site-packages.pandas.core', 'env36.Lib.site-packages.pandas.core.util',
              'env36.Lib.site-packages.pandas.core.tools', 'env36.Lib.site-packages.pandas.core.arrays',
              'env36.Lib.site-packages.pandas.core.dtypes', 'env36.Lib.site-packages.pandas.core.sparse',
              'env36.Lib.site-packages.pandas.core.groupby', 'env36.Lib.site-packages.pandas.core.indexes',
              'env36.Lib.site-packages.pandas.core.reshape', 'env36.Lib.site-packages.pandas.core.computation',
              'env36.Lib.site-packages.pandas.util', 'env36.Lib.site-packages.pandas._libs',
              'env36.Lib.site-packages.pandas._libs.tslibs', 'env36.Lib.site-packages.pandas.tests',
              'env36.Lib.site-packages.pandas.tests.io', 'env36.Lib.site-packages.pandas.tests.io.sas',
              'env36.Lib.site-packages.pandas.tests.io.json', 'env36.Lib.site-packages.pandas.tests.io.parser',
              'env36.Lib.site-packages.pandas.tests.io.formats', 'env36.Lib.site-packages.pandas.tests.io.msgpack',
              'env36.Lib.site-packages.pandas.tests.api', 'env36.Lib.site-packages.pandas.tests.util',
              'env36.Lib.site-packages.pandas.tests.frame', 'env36.Lib.site-packages.pandas.tests.tools',
              'env36.Lib.site-packages.pandas.tests.dtypes', 'env36.Lib.site-packages.pandas.tests.scalar',
              'env36.Lib.site-packages.pandas.tests.scalar.period',
              'env36.Lib.site-packages.pandas.tests.scalar.interval',
              'env36.Lib.site-packages.pandas.tests.scalar.timedelta',
              'env36.Lib.site-packages.pandas.tests.scalar.timestamp', 'env36.Lib.site-packages.pandas.tests.series',
              'env36.Lib.site-packages.pandas.tests.series.indexing', 'env36.Lib.site-packages.pandas.tests.sparse',
              'env36.Lib.site-packages.pandas.tests.sparse.frame', 'env36.Lib.site-packages.pandas.tests.sparse.series',
              'env36.Lib.site-packages.pandas.tests.tslibs', 'env36.Lib.site-packages.pandas.tests.generic',
              'env36.Lib.site-packages.pandas.tests.groupby', 'env36.Lib.site-packages.pandas.tests.groupby.aggregate',
              'env36.Lib.site-packages.pandas.tests.indexes', 'env36.Lib.site-packages.pandas.tests.indexes.period',
              'env36.Lib.site-packages.pandas.tests.indexes.interval',
              'env36.Lib.site-packages.pandas.tests.indexes.datetimes',
              'env36.Lib.site-packages.pandas.tests.indexes.timedeltas', 'env36.Lib.site-packages.pandas.tests.reshape',
              'env36.Lib.site-packages.pandas.tests.reshape.merge', 'env36.Lib.site-packages.pandas.tests.tseries',
              'env36.Lib.site-packages.pandas.tests.tseries.offsets', 'env36.Lib.site-packages.pandas.tests.indexing',
              'env36.Lib.site-packages.pandas.tests.indexing.interval', 'env36.Lib.site-packages.pandas.tests.plotting',
              'env36.Lib.site-packages.pandas.tests.extension', 'env36.Lib.site-packages.pandas.tests.extension.base',
              'env36.Lib.site-packages.pandas.tests.extension.json',
              'env36.Lib.site-packages.pandas.tests.extension.decimal',
              'env36.Lib.site-packages.pandas.tests.extension.category',
              'env36.Lib.site-packages.pandas.tests.internals', 'env36.Lib.site-packages.pandas.tests.categorical',
              'env36.Lib.site-packages.pandas.tests.computation', 'env36.Lib.site-packages.pandas.tools',
              'env36.Lib.site-packages.pandas.types', 'env36.Lib.site-packages.pandas.compat',
              'env36.Lib.site-packages.pandas.compat.numpy', 'env36.Lib.site-packages.pandas.errors',
              'env36.Lib.site-packages.pandas.formats', 'env36.Lib.site-packages.pandas.tseries',
              'env36.Lib.site-packages.pandas.plotting', 'env36.Lib.site-packages.pandas.computation',
              'env36.Lib.site-packages.quandl', 'env36.Lib.site-packages.quandl.model',
              'env36.Lib.site-packages.quandl.utils', 'env36.Lib.site-packages.quandl.errors',
              'env36.Lib.site-packages.quandl.operations', 'env36.Lib.site-packages.certifi',
              'env36.Lib.site-packages.chardet', 'env36.Lib.site-packages.chardet.cli',
              'env36.Lib.site-packages.tzlocal', 'env36.Lib.site-packages.urllib3',
              'env36.Lib.site-packages.urllib3.util', 'env36.Lib.site-packages.urllib3.contrib',
              'env36.Lib.site-packages.urllib3.contrib._securetransport', 'env36.Lib.site-packages.urllib3.packages',
              'env36.Lib.site-packages.urllib3.packages.backports',
              'env36.Lib.site-packages.urllib3.packages.ssl_match_hostname', 'env36.Lib.site-packages.DateTime',
              'env36.Lib.site-packages.DateTime.tests', 'env36.Lib.site-packages.dateutil',
              'env36.Lib.site-packages.dateutil.tz', 'env36.Lib.site-packages.dateutil.parser',
              'env36.Lib.site-packages.dateutil.zoneinfo', 'env36.Lib.site-packages.requests',
              'env36.Lib.site-packages.schedule', 'env36.Lib.site-packages.matplotlib',
              'env36.Lib.site-packages.matplotlib.tri', 'env36.Lib.site-packages.matplotlib.axes',
              'env36.Lib.site-packages.matplotlib.cbook', 'env36.Lib.site-packages.matplotlib.style',
              'env36.Lib.site-packages.matplotlib.compat', 'env36.Lib.site-packages.matplotlib.testing',
              'env36.Lib.site-packages.matplotlib.testing._nose',
              'env36.Lib.site-packages.matplotlib.testing._nose.plugins',
              'env36.Lib.site-packages.matplotlib.testing.jpl_units', 'env36.Lib.site-packages.matplotlib.backends',
              'env36.Lib.site-packages.matplotlib.backends.qt_editor', 'env36.Lib.site-packages.matplotlib.sphinxext',
              'env36.Lib.site-packages.matplotlib.projections', 'env36.Lib.site-packages.simplejson',
              'env36.Lib.site-packages.simplejson.tests', 'env36.Lib.site-packages.mpl_toolkits.mplot3d',
              'env36.Lib.site-packages.mpl_toolkits.axes_grid', 'env36.Lib.site-packages.mpl_toolkits.axes_grid1',
              'env36.Lib.site-packages.mpl_toolkits.axisartist', 'env36.Lib.site-packages.requests_ftp',
              'env36.Lib.site-packages.googlefinance', 'env36.Lib.site-packages.yahoo_finance',
              'env36.Lib.site-packages.more_itertools', 'env36.Lib.site-packages.more_itertools.tests',
              'env36.Lib.site-packages.pandas_datareader', 'env36.Lib.site-packages.pandas_datareader.io',
              'env36.Lib.site-packages.pandas_datareader.iex', 'env36.Lib.site-packages.pandas_datareader.mstar',
              'env36.Lib.site-packages.pandas_datareader.tests', 'env36.Lib.site-packages.pandas_datareader.tests.io',
              'env36.Lib.site-packages.pandas_datareader.tests.mstar',
              'env36.Lib.site-packages.pandas_datareader.tests.yahoo',
              'env36.Lib.site-packages.pandas_datareader.tests.google',
              'env36.Lib.site-packages.pandas_datareader.yahoo', 'env36.Lib.site-packages.pandas_datareader.compat',
              'env36.Lib.site-packages.pandas_datareader.google', 'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.req',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.vcs',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.utils',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.compat',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.models',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.distlib',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.distlib._backport',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.colorama',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib._trie',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib.filters',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib.treewalkers',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib.treeadapters',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib.treebuilders',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.lockfile',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.progress',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.chardet',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3.util',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3.contrib',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3.packages',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.packaging',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.cachecontrol',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.cachecontrol.caches',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.webencodings',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.pkg_resources',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.commands',
              'env36.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.operations', 'tests', 'trading', 'technical'],
    url='',
    license='',
    author='suman',
    author_email='',
    description=''
)