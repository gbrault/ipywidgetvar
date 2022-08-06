import ipywidgets as widgets
from traitlets import Unicode

# See js/lib/example.js for the frontend counterpart to this file.

@widgets.register
class IpywidgetVar(widgets.DOMWidget):
    """An example widget."""

    # Name of the widget view class in front-end
    _view_name = Unicode('IpywidgetVarView').tag(sync=True)

    # Name of the widget model class in front-end
    _model_name = Unicode('IpywidgetVarModel').tag(sync=True)

    # Name of the front-end module containing widget view
    _view_module = Unicode('ipywidgetvar').tag(sync=True)

    # Name of the front-end module containing widget model
    _model_module = Unicode('ipywidgetvar').tag(sync=True)

    # Version of the front-end module containing widget view
    _view_module_version = Unicode('^0.1.10').tag(sync=True)
    # Version of the front-end module containing widget model
    _model_module_version = Unicode('^0.1.10').tag(sync=True)

    # Widget specific property.
    # Widget properties are defined as traitlets. Any property tagged with `sync=True`
    # is automatically synced to the frontend *any* time it changes in Python.
    # It is synced back to Python from the frontend *any* time the model is touched.
    value = Unicode('IpywidgetVar--').tag(sync=True)
    id = Unicode('id1').tag(sync=True)
    tojs = Unicode('tojsvalue').tag(sync=True)
    topython = Unicode('topythonvalue').tag(sync=True)
