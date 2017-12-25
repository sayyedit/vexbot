extensions = {'pip_install': {'path': 'vexbot.extensions.admin:install',
                              'short': 'Install packages using pip',},
              'pip_uninstall': {'path': 'vexbot.extensions.admin:uninstall',
                                'short': 'Uninstall packages using pip'},
              'pip_update': {'path': 'vexbot.extensions.admin:update',
                             'short': 'Update packages using pip'},
              'get_commands': {'path': 'vexbot.extensions.admin:get_commands',
                               'short': 'Get commands from command observer'},
              'get_command_modules': {'path': 'vexbot.extensions.admin:get_command_modules',
                                      'short': 'Get all the module names for the commands that are available'},
              'get_disabeled': {'path': 'vexbot.extensions.admin:get_disabled',
                                'short': 'Get all disabled commands from command observer'},
              'disable': {'path': 'vexbot.extensions.admin:disable',
                          'short': 'remove a command from the commands'},
              'get_cache': {'path': 'vexbot.extensions.admin:get_cache',
                            'short': 'Get the values of the configuration cache'},
              'get_code': {'path': 'vexbot.extensions.develop:get_code',
                           'short': 'Get the source code from a method using the inspect module'},
              'get_method_names': {'path': 'vexbot.extensions.develop:get_members',
                                   'short': 'Get all the method names from a class using inspect module'},
              'get_size': {'path': 'vexbot.extensions.digitalocean:get_size',
                           'short': 'Get the size of a digital ocean droplet',
                           'extras': ['digitalocean',]},
              'power_off': {'path': 'vexbot.extensions.digitalocean:power_off',
                            'short': 'Power off a digital ocean droplet',
                           'extras': ['digitalocean',]},
              'power_on': {'path': 'vexbot.extensions.digitalocean:power_on',
                           'short': 'Power on a digital ocean droplet',
                           'extras': ['digitalocean',]},
              'get_all_droplets': {'path': 'vexbot.extensions.digitalocean:get_all_droplets',
                                   'short': 'Get all droplets from digital ocean',
                                   'extras': ['digitalocean',]},
              'add_extensions': {'path': 'vexbot.extensions.extensions:add_extensions',
                                 'short': 'Add an extension to a command observer'},
              'get_extensions': {'path': 'vexbot.extensions.extensions:get_extensions',
                                 'short': 'Get all the extensions from an observer instance'},
              'remove_extension': {'path': 'vexbot.extensions.extensions:remove_extension',
                                    'short': 'Remove an extension from an observer instance'},
              'get_installed_extensions': {'path': 'vexbot.extensions.extensions:get_installed_extensions',
                                           'short': 'See all installed extensions for Vexbot'},
              'add_extensions_from_dict': {'path': 'vexbot.extensions.extensions:add_extensions_from_dict',
                                           'short': 'Used to intialize command observers efficient'},
              'help': {'path': 'vexbot.extensions.help:help',
                       'short': 'Get the help from a method'},
              'hidden': {'path': 'vexbot.extensions:hidden',
                         'short': 'Get all hidden method methods'},
              'bot_intents': {'path': 'vexbot.extensions.intents:get_intents',
                              'short': 'Get the intents from the bot'},
              'bot_intent': {'path': 'vexbot.extensions.intents:get_intent'},
              'get_google_trends': {'path': 'vexbot.extensions.news:get_hot_trends',
                                    'short': 'Get the google trends',
                                    'extras': ['summarization']},
              'get_news_urls': {'path': 'vexbot.extensions.news:get_popular_urls',
                                'extras': ['summarization']},
              'summarize_news_url': {'path': 'vexbot.extensions.news:summarize_article',
                                     'extras': ['summarization']},
              # extras -> pydbus
              'start_process': {'path': 'vexbot.extensions.subprocess:start',
                                'extras': ['pydbus']},
              'stop_process': {'path': 'vexbot.extensions.subprocess:stop',
                                'extras': ['pydbus']},
              'restart_process': {'path': 'vexbot.extensions.subprocess:restart',
                                  'extras': ['pydbus']},
              'status_process': {'path': 'vexbot.extensions.subprocess:status',
                                 'extras': ['pydbus']},
              'cpu_count': {'path': 'vexbot.extensions.system:cpu_count',
                            'extras': ['system']},
              'virtual_memory_percent': {'path': 'vexbot.extensions.system:virtual_memory_percent',
                                         'extras': ['system']},
              'virtual_memory_total': {'path': 'vexbot.extensions.system:virtual_memory_total',
                                       'extras': ['system']},
              'virtual_memory_used': {'path': 'vexbot.extensions.system:virtual_memory_used',
                                      'extras': ['system']},
              'swap': {'path': 'vexbot.extensions.system:swap',
                       'extras': ['system']}}
