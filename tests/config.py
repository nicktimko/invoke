from spec import Spec, skip, eq_

from invoke.vendor.etcaetera.adapter import File

from invoke.config import Config


class Config_(Spec):
    class init:
        "__init__"

        def can_be_empty(self):
            eq_(Config().__class__, Config) # derp

        def configure_global_location_prefix(self):
            # This is a bit funky but more useful than just replicating the
            # same test in Executor?
            c = Config(global_path='meh')
            ok_(any(isinstance(x, File) and x.filepath == 'meh', c.adapters))

        def default_global_prefix_is_etc(self):
            skip()

        def configure_user_location_prefix(self):
            skip()

        def default_local_prefix_is_homedir(self):
            skip()

        def unknown_kwargs_turn_into_top_level_defaults(self):
            skip()

        def does_not_trigger_config_loading(self):
            skip()

    def allows_explicit_loading(self):
        skip()

    def allows_modification_of_defaults(self):
        # Something light which wraps self._config.defaults[k] = v
        skip()

    def allows_dict_and_attr_access(self):
        # TODO: combine with tests for Context probably
        skip()

    def nested_dict_values_also_allow_dual_access(self):
        # TODO: ditto
        skip()