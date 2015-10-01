{
    'variables': { 'target_arch%': 'ia32' },

  'target_defaults': {
    'default_configuration': 'Debug',
    'configurations': {
      'Debug': {
        'defines': [ 'DEBUG', '_DEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 1, # static debug
          },
        },
      },
      'Release': {
        'defines': [ 'NDEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 0, # static release
          },
        },
      }
    },
    'msvs_settings': {
      'VCLinkerTool': {
        'GenerateDebugInformation': 'true',
      },
    },
    'include_dirs': [
       # platform and arch-specific headers
       '../config/<(OS)/<(target_arch)'
     ],
  },

    "targets": [
        {
            "target_name": "libpng",
            'dependencies': [
              '../gyp-zlib/bindings/zlib.gyp:zlib'
            ],

	    #'product_prefix': 'lib',
            "type": "static_library",
            "include_dirs": [
                "../libpng",
                "../gyp-zlib/zlib/",
            ],
            'defines': [ 'PNG_NO_CONFIG_H' ],
            "sources": [
                "../libpng/arm/arm_init.c",
                "../libpng/arm/filter_neon_intrinsics.c",
                "../libpng/png.c",
                "../libpng/pngerror.c",
                "../libpng/pngget.c",
                "../libpng/pngmem.c",
                "../libpng/pngpread.c",
                "../libpng/pngread.c",
                "../libpng/pngrio.c",
                "../libpng/pngrtran.c",
                "../libpng/pngrutil.c",
                "../libpng/pngset.c",
                #"../libpng/pngtest.c",
                "../libpng/pngtrans.c",
                "../libpng/pngwio.c",
                "../libpng/pngwrite.c",
                "../libpng/pngwtran.c",
                "../libpng/pngwutil.c"
            ],
            "conditions": [
                [
                    "OS==\"linux\"",
                    {
                        "include_dirs": [
                            "platform-includes/linux/libpng"
                        ]
                    }
                ],
                [
                    "OS==\"mac\"",
                    {
                        "include_dirs": [
                            "platform-includes/mac/libpng"
                        ]
                    }
                ],
                [
                    "OS==\"win\"",
                    {
                        "defines": [
                            "USE_MSDOS_MEMMGR"
                        ],
                        "include_dirs": [
                            "platform-includes/win/libpng"
                        ]
                    }
                ]
            ]
        }
    ]
}
